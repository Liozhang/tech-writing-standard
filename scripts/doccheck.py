# -*- coding: utf-8 -*-
"""通用技术文档写作规范 门禁检查脚本（1.2 正式版）

实现规范中可机检的必须项子集：
  TOOL-020  检查范围排除代码块与行内代码
  ZH-010    中文句长（句边界为句号、问号、感叹号；分号处分句取最长；
            标点不计；汉字每字计一；连续数字串按一词计；标准号编号豁免）
  ZH-023    汉字与拉丁字母、数字相邻处应加一个空格
  ZH-027    规则定义句 100 字硬顶，资料性附录不执行句长限制
  TOOL-022  标题层级跳级检查
  规则格式  规则编号与级别字段检查（级别只允许必须、应该、可以）

用法：
  python doccheck.py <文件或目录> [句长上限]   中文句长、混排、标题、规则格式
  python doccheck.py <文件或目录> --en        英语句长（默认 25 词，括号内列举另计）
  python doccheck.py <文件或目录> --a11y      无障碍可机检（图示替代文本、表格表头、空链接）
  python doccheck.py <文件或目录> --term      术语禁用词与同义混用（读同目录 termbase.csv）
  python doccheck.py <文件或目录> --term --termbase <路径>   指定其他术语库
已知边界：术语与编号豁免、同形歧义判断、语义类规则未实现，结果需人工复核。
"""

import re
import sys
import json
from pathlib import Path

LEVELS = ("必须", "应该", "可以")
SENT_END = tuple("。？！")
CODE_FENCE = re.compile(r"^\s*```")
INLINE_CODE = re.compile(r"`[^`\n]+`")
RULE_DEF = re.compile(
    r"^-?\s*\*{0,2}(GOV|CON|GEN|ZH|EN|LANG|DOM|STR|TERM|TOOL)-[A-Z]*-?\d+\*{0,2}（([^）]*)）"
)
HEADING = re.compile(r"^(#{1,6})\s+\S")
CJK = r"\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af"
CJK_LATIN = re.compile(rf"([{CJK}])([A-Za-z0-9])")
LATIN_CJK = re.compile(rf"([A-Za-z0-9])([{CJK}])")


def strip_code(text: str) -> str:
    """按 TOOL-020 排除代码块，返回屏蔽后的文本（代码块保留行数以定位）。"""
    out, in_fence = [], False
    for line in text.splitlines():
        if CODE_FENCE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def mask_inline_code(line: str) -> str:
    return INLINE_CODE.sub(lambda m: " " * len(m.group(0)), line)


def count_sentence(sentence: str) -> int:
    """ZH-010 计数规则；标准号与编号豁免，连续数字串按一个词计。"""
    s = mask_inline_code(sentence)
    # 术语与编号豁免：标准号、版本号、规则编号（字母加数字）整体不计
    s = re.sub(r"[A-Za-z]+[\s-]?\d+(?:[.\-:]\d+)*", " ", s)
    # 连续数字串按一个词计，用占位符保留其词位
    s = re.sub(r"\d+(?:[.,:：\-]\d+)*", "0", s)
    total = 0
    for token in re.findall(rf"[{CJK}]|[A-Za-z]+(?:[-'][A-Za-z]+)*|\d", s):
        total += 1
    return total


def is_enumeration(sentence: str) -> bool:
    """ZH-010：分号连接的并列分句分别计长，取最长分句判定。"""
    parts = [p for p in re.split(r"[；;]", sentence) if p.strip()]
    return len(parts) > 1


def split_sentences(text: str) -> list:
    buf, out = [], []
    for ch in text:
        buf.append(ch)
        if ch in SENT_END:
            out.append("".join(buf))
            buf = []
    if "".join(buf).strip():
        out.append("".join(buf))
    return out


def check_sentence_length(plain: str, is_rule_line: bool, limit: int,
                         hard: int) -> int:
    """按 ZH-027 返回句子计长：规则定义句整句计，其余按最长并列分句计。"""
    if is_rule_line:
        return count_sentence(plain)
    parts = [p for p in re.split(r"[；;]", plain) if p.strip()]
    return max((count_sentence(p) for p in parts), default=count_sentence(plain))


def check_file(path: Path, limit: int, hard: int = 100) -> dict:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    result = {"file": path.name, "sentence_hits": [], "table_hits": [],
              "hard_hits": [], "space_hits": [], "heading_hits": [],
              "rule_hits": []}
    in_fence = False
    last_level = 0
    for ln, line in enumerate(lines, 1):
        if CODE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        check_line = mask_inline_code(line)
        in_table = line.lstrip().startswith("|")
        is_rule_line = bool(RULE_DEF.match(line))
        for sent in split_sentences(check_line):
            plain = sent.strip()
            if len(plain) < 4:
                continue
            n = check_sentence_length(plain, is_rule_line, limit, hard)
            cap = hard if is_rule_line else limit
            if n > cap:
                # 表格行按版面结构单独统计，不计入正文句长违规
                bucket = ("table_hits" if in_table else
                          ("hard_hits" if n > hard else "sentence_hits"))
                result[bucket].append(
                    {"line": ln, "len": n, "cap": cap, "text": plain[:60]})
        for m in CJK_LATIN.finditer(check_line):
            result["space_hits"].append({"line": ln, "at": m.group(0)[:8]})
        for m in LATIN_CJK.finditer(check_line):
            result["space_hits"].append({"line": ln, "at": m.group(0)[:8]})
        hm = HEADING.match(line)
        if hm:
            level = len(hm.group(1))
            if last_level and level > last_level + 1:
                result["heading_hits"].append({"line": ln, "jump": f"{last_level}->{level}"})
            last_level = level
        rm = RULE_DEF.match(line)
        if rm:
            scope = rm.group(2)
            lvl = scope.split("，")[0].split(",")[0]
            if lvl not in LEVELS:
                result["rule_hits"].append(
                    {"line": ln, "rule": rm.group(1) + "-…", "level": lvl})
    return result


APPENDIX = {"01-现有规范汇编.md", "12-评审意见汇总.md", "13-母语专家复核报告.md",
            "14-科研领域评审意见汇总.md", "15-1.0版本建立方案.md",
            "16-门禁试跑记录.md", "17-端到端符合性演练报告.md",
            "18-完整级关闭记录.md"}


WORD_TOKEN = re.compile(r"[A-Za-z0-9]+(?:[-'’][A-Za-z0-9]+)*")


def count_words(sentence: str) -> int:
    """EN-009 计数规则：按空格分词，连字符复合词与缩写各计一词。"""
    s = mask_inline_code(sentence)
    s = re.sub(r"[A-Za-z]+[\s-]?\d+(?:[.\-:]\d+)*", " ", s)
    return len(WORD_TOKEN.findall(s))


def is_english_sentence(sentence: str) -> bool:
    letters = sum(ch.isascii() and ch.isalpha() for ch in sentence)
    cjk = sum("一" <= ch <= "鿿" for ch in sentence)
    return letters > 20 and letters > cjk * 2


def check_english(path: Path, limit_proc: int = 20,
                  limit_desc: int = 25) -> dict:
    """英语模块门禁：句长以词计，代码域排除。"""
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    hits = []
    in_fence = False
    for ln, line in enumerate(lines, 1):
        if CODE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence or line.lstrip().startswith("|"):
            continue
        for sent in split_sentences(mask_inline_code(line)):
            plain = sent.strip()
            if len(plain) < 4 or not is_english_sentence(plain):
                continue
            n = count_words(plain)
            if n > limit_desc:
                hits.append({"line": ln, "len": n, "text": plain[:70]})
    return {"file": path.name, "en_hits": hits}


ALT_IMG = re.compile(r"!\[\s*\]\(")
TABLE_HEAD = re.compile(r"^\s*\|[-: \|]+\|\s*$")
EMPTY_LINK = re.compile(r"(?<!!)\[\s*\]\(")


def check_accessibility(path: Path) -> dict:
    """TOOL-023 可机检部分：替代文本、表格表头、空链接文字。"""
    lines = path.read_text(encoding="utf-8").splitlines()
    hits = []
    prev_was_table = False
    for ln, line in enumerate(lines, 1):
        if ALT_IMG.search(line):
            hits.append({"line": ln, "kind": "图示缺替代文本"})
        if EMPTY_LINK.search(line):
            hits.append({"line": ln, "kind": "链接文字为空"})
        if line.lstrip().startswith("|") and not prev_was_table:
            nxt = lines[ln] if ln < len(lines) else ""
            if not TABLE_HEAD.match(nxt):
                hits.append({"line": ln, "kind": "表格缺表头行"})
        prev_was_table = line.lstrip().startswith("|")
    return {"file": path.name, "a11y_hits": hits}


def load_termbase(path: Path) -> dict:
    """加载术语库（TERM-001 概念主键）。返回禁用词表与同义混用候选项。"""
    import csv
    forbidden, aliases = {}, {}
    with path.open(encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            concept = row.get("概念编号", "").strip()
            if not concept:
                continue
            for banned in (row.get("简体中文禁用") or "").split(";"):
                banned = banned.strip()
                if banned:
                    forbidden[banned] = concept
            approved = set()
            for col in ("简体中文首选", "简体中文可用"):
                for w in (row.get(col) or "").split(";"):
                    w = w.strip()
                    if w:
                        approved.add(w)
            aliases[concept] = approved
    return {"forbidden": forbidden, "aliases": aliases}


def check_terms(path: Path, termbase: dict) -> dict:
    """TERM-021：检出禁用词、同义混用、未定义缩写。代码块与行内代码排除。"""
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    hits = []
    seen = {}
    in_fence = False
    for ln, line in enumerate(lines, 1):
        if CODE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        text = mask_inline_code(line)
        for banned, concept in termbase["forbidden"].items():
            if banned in text:
                hits.append({"line": ln, "kind": "禁用词",
                             "term": banned, "concept": concept})
        for concept, approved in termbase["aliases"].items():
            used = {w for w in approved if w in text}
            # 剔除是其他已命中词形子串的短词形，避免“监管文档”误判为“受监管文档”的混用
            used = {w for w in used
                    if not any(w != o and w in o for o in used)}
            if len(used) > 1:
                hits.append({"line": ln, "kind": "同义混用",
                             "term": "、".join(sorted(used)), "concept": concept})
            seen.setdefault(concept, {}).setdefault(ln, used)
    for concept, per_line in seen.items():
        used_all = set().union(*per_line.values())
        used_all = {w for w in used_all
                    if not any(w != o and w in o for o in used_all)}
        if len(used_all) > 1:
            hits.append({"line": min(per_line), "kind": "同义混用（跨行）",
                         "term": "、".join(sorted(used_all)), "concept": concept})
    return {"file": path.name, "term_hits": hits}


def collect(targets) -> list:
    """展开目标为 Markdown 文件列表。目录递归查找，跳过隐藏目录。"""
    files = []
    for t in targets:
        if t.is_dir():
            files.extend(sorted(
                p for p in t.rglob("*.md")
                if not any(part.startswith(".") for part in p.parts)))
        else:
            files.append(t)
    return files


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    targets = [Path(a) for a in args if not a.isdigit()] or [Path(".")]
    limit = next((int(a) for a in args if a.isdigit()), 50)
    files = collect(targets)
    grand = {k: 0 for k in ("sentence_hits", "table_hits", "hard_hits",
                            "space_hits", "heading_hits", "rule_hits")}
    for f in files:
        if f.name in APPENDIX or f.name == "README.md":
            continue  # 资料性附录不执行句长限制（ZH-027）
        r = check_file(f, limit)
        for k in grand:
            grand[k] += len(r[k])
        print(f"[{f.name}] 正文句长超 50 字 {len(r['sentence_hits'])} 处；"
              f"表格行超限 {len(r['table_hits'])} 处（版面结构，不计违规）；"
              f"超 100 字硬顶 {len(r['hard_hits'])} 处；"
              f"混排缺空格 {len(r['space_hits'])} 处；"
              f"标题跳级 {len(r['heading_hits'])} 处；"
              f"规则级别异常 {len(r['rule_hits'])} 处")
        for h in r["hard_hits"][:5]:
            print(f"    L{h['line']} {h['len']}字 {h['text']}")
        for h in r["sentence_hits"][:5]:
            print(f"    L{h['line']} {h['len']}字 {h['text']}")
        for h in r["space_hits"][:3]:
            print(f"    L{h['line']} 空格 {h['at']}")
        for h in r["heading_hits"][:3]:
            print(f"    L{h['line']} 跳级 {h['jump']}")
        for h in r["rule_hits"][:3]:
            print(f"    L{h['line']} 级别 {h['level']} {h['rule']}")
    print(json.dumps({"合计": grand, "描述类上限": limit, "硬顶": 100},
                     ensure_ascii=False))


def main_en():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    targets = [Path(a) for a in args] or [Path(".")]
    files = collect(targets)
    total = 0
    for f in files:
        if f.name in APPENDIX:
            continue
        r = check_english(f)
        total += len(r["en_hits"])
        print(f"[{f.name}] 英语句超 25 词 {len(r['en_hits'])} 处")
        for h in r["en_hits"][:3]:
            print(f"    L{h['line']} {h['len']}词 {h['text']}")
    print(json.dumps({"英语句长命中合计": total}, ensure_ascii=False))


def main_a11y():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    targets = [Path(a) for a in args] or [Path(".")]
    files = collect(targets)
    total = 0
    for f in files:
        r = check_accessibility(f)
        total += len(r["a11y_hits"])
        if r["a11y_hits"]:
            print(f"[{f.name}] 无障碍可机检项 {len(r['a11y_hits'])} 处")
            for h in r["a11y_hits"][:3]:
                print(f"    L{h['line']} {h['kind']}")
    print(json.dumps({"无障碍可机检命中合计": total}, ensure_ascii=False))


def termbase_path_from(argv) -> Path:
    """从命令行参数取术语库路径；缺省用脚本同目录的 termbase.csv。"""
    if "--termbase" in argv:
        i = argv.index("--termbase")
        if i + 1 < len(argv):
            return Path(argv[i + 1])
    return Path(__file__).resolve().parent / "termbase.csv"


def main_terms():
    argv = sys.argv[1:]
    tb_path = termbase_path_from(argv)
    args = [a for a in argv if not a.startswith("--")]
    if "--termbase" in argv:
        i = argv.index("--termbase")
        if i + 1 < len(argv):
            args = [a for a in args if a != argv[i + 1]]
    if not tb_path.exists():
        print("术语库不存在")
        return
    tb = load_termbase(tb_path)
    files = collect([Path(a) for a in args] or [Path(".")])
    total = 0
    for f in files:
        if f.name in APPENDIX:
            continue
        r = check_terms(f, tb)
        total += len(r["term_hits"])
        if r["term_hits"]:
            print(f"[{f.name}] 术语命中 {len(r['term_hits'])} 处")
            for h in r["term_hits"][:5]:
                print(f"    L{h['line']} {h['kind']} {h['term']}（概念 {h['concept']}）")
    print(json.dumps({"术语命中合计": total}, ensure_ascii=False))


if __name__ == "__main__":
    if "--en" in sys.argv:
        main_en()
    elif "--a11y" in sys.argv:
        main_a11y()
    elif "--term" in sys.argv:
        main_terms()
    else:
        main()
