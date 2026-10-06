# -*- coding: utf-8 -*-
"""doccheck.py 单元测试。

验证 ZH-010 计数规则、ZH-023 混排检测、ZH-027 列举句识别、
规则格式检查与 check_file 端到端行为。运行：python test_doccheck.py
"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from doccheck import (count_sentence, is_enumeration, split_sentences,
                      mask_inline_code, RULE_DEF, check_file, count_words,
                      is_english_sentence, check_english, check_accessibility,
                      load_termbase, check_terms, collect, termbase_path_from)

CASES = []


def case(name):
    def deco(fn):
        CASES.append((name, fn))
        return fn
    return deco


@case("汉字每字计一")
def _():
    assert count_sentence("这是十个汉字的测试句子内容") == 13


@case("标点不计入")
def _():
    assert count_sentence("测试，句子。") == count_sentence("测试句子")


@case("连续数字串按一个词计")
def _():
    assert count_sentence("版本 12 发布") == count_sentence("版本 一 发布")
    assert count_sentence("第 1 步") == count_sentence("第甲步")


@case("标准号与编号按术语豁免")
def _():
    plain = count_sentence("日期用 ISO 8601 数字格式")
    assert plain == count_sentence("日期用 数字格式"), plain


@case("缩写按一个词计")
def _():
    assert count_sentence("调用 API 接口") == 5


@case("行内代码被屏蔽")
def _():
    assert count_sentence("运行 `docker compose up` 命令") == count_sentence("运行 命令")


@case("分号不构成句边界")
def _():
    assert len(split_sentences("甲；乙。丙")) == 2


@case("句末标点构成句边界")
def _():
    assert len(split_sentences("甲。乙？丙！")) == 3


@case("分号处分句，两个及以上分句即列举")
def _():
    assert is_enumeration("甲；乙；丙。")
    assert is_enumeration("甲；乙。")
    assert not is_enumeration("甲乙丙。")


@case("列举句按最长分句判定，超限被拦")
def _():
    enum = "；".join(["乙" * 20] * 2 + ["字" * 60]) + "。"
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(enum + "\n")
        path = Path(fh.name)
    r = check_file(path, limit=50, hard=100)
    path.unlink()
    assert len(r["sentence_hits"]) == 1, r["sentence_hits"]


@case("规则定义句是唯一放宽句类，整句超 100 字被拦")
def _():
    rule = "GEN-001（必须）" + "甲" * 110 + "。"
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(rule + "\n")
        path = Path(fh.name)
    r = check_file(path, limit=50, hard=100)
    path.unlink()
    assert len(r["hard_hits"]) == 1, r["hard_hits"]


@case("汉字与拉丁相邻检出缺空格")
def _():
    assert CJK_LATIN_SEARCH("中文English混排")


@case("拉丁与汉字相邻检出缺空格")
def _():
    assert LATIN_CJK_SEARCH("API接口")


@case("已加空格不检出")
def _():
    assert not CJK_LATIN_SEARCH("中文 English 混排")
    assert not LATIN_CJK_SEARCH("API 接口")


@case("规则定义行可识别")
def _():
    assert RULE_DEF.match("GEN-030（必须）一步只含一个动作单元。")
    assert RULE_DEF.match("- LANG-021（必须）嵌入内容保持从左向右。")


@case("非三档级别被检出")
def _():
    m = RULE_DEF.match("GEN-999（尽量）做到清晰。")
    assert m and m.group(2) not in ("必须", "应该", "可以")


@case("端到端：各类违规计数正确")
def _():
    long_plain = "甲" * 60 + "。"
    long_enum = "；".join(["乙" * 20] * 4) + "。"
    ok = "短句。"
    text = (f"{long_plain}\n{long_enum}\n{ok}\n"
            "中文English缺空格一句。\n# 标题\n### 跳级标题\n")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(text)
        path = Path(fh.name)
    r = check_file(path, limit=50, hard=100)
    path.unlink()
    assert len(r["sentence_hits"]) == 1, r["sentence_hits"]
    assert len(r["hard_hits"]) == 0, r["hard_hits"]
    # 一处缺失空格在两侧边界各产生一条命中
    assert len(r["space_hits"]) == 2, r["space_hits"]
    assert len(r["heading_hits"]) == 1, r["heading_hits"]


@case("英语按词计数，连字符复合词计一词")
def _():
    assert count_words("This is a well-known rule for writers.") == 7
    assert count_words("Use the API and HTML standards.") == 6


@case("英语句超 25 词被检出")
def _():
    long_en = " ".join(["word"] * 28) + "."
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(long_en + chr(10))
        path = Path(fh.name)
    r = check_english(path)
    path.unlink()
    assert len(r["en_hits"]) == 1, r["en_hits"]


@case("中文句不进入英语门禁")
def _():
    assert not is_english_sentence("这是一段完全中文的句子，不含英文内容。")
    assert is_english_sentence("This sentence is written entirely in English.")


@case("无障碍可机检项：图示缺替代文本与表格缺表头")
def _():
    text = chr(10).join(["![](img.png)", "", "| 列一 | 列二 |", "| --- | --- |", "| 值 | 值 |", ""])
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(text)
        path = Path(fh.name)
    r = check_accessibility(path)
    path.unlink()
    assert len(r["a11y_hits"]) == 1, r["a11y_hits"]


@case("术语门禁：禁用词命中，批准词形与代码豁免")
def _():
    tb = load_termbase(Path(__file__).resolve().parent / "termbase.csv")
    assert "急停开关" in tb["forbidden"]
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(chr(10).join(["按下急停开关停机。", "命令：`sideload install` 不译。", ""]))
        path = Path(fh.name)
    r = check_terms(path, tb)
    path.unlink()
    kinds = [(h["kind"], h["term"]) for h in r["term_hits"]]
    assert ("禁用词", "急停开关") in kinds
    assert not any("sideload" in t2 for _, t2 in kinds)


@case("术语门禁：同义混用检出")
def _():
    tb = load_termbase(Path(__file__).resolve().parent / "termbase.csv")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(chr(10).join(["先用急停按钮停机。", "再按紧急停止按钮复位。", ""]))
        path = Path(fh.name)
    r = check_terms(path, tb)
    path.unlink()
    assert any(h["kind"].startswith("同义混用") for h in r["term_hits"]), r["term_hits"]


@case("术语门禁：短词形是长词形子串时不判混用")
def _():
    tb = load_termbase(Path(__file__).resolve().parent / "termbase.csv")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(chr(10).join(["受监管文档必须适用完整级。", ""]))
        path = Path(fh.name)
    r = check_terms(path, tb)
    path.unlink()
    assert not r["term_hits"], r["term_hits"]


@case("目录收集：递归查找且跳过隐藏目录")
def _():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "子目录").mkdir()
        (root / ".git").mkdir()
        (root / "顶层.md").write_text("测试。", encoding="utf-8")
        (root / "子目录" / "嵌套.md").write_text("测试。", encoding="utf-8")
        (root / ".git" / "配置.md").write_text("测试。", encoding="utf-8")
        (root / "非文本.txt").write_text("测试。", encoding="utf-8")
        found = collect([root])
        names = sorted(p.relative_to(root).as_posix() for p in found)
        assert names == ["子目录/嵌套.md", "顶层.md"], names


@case("术语库参数：--termbase 指定路径，缺省走脚本同目录")
def _():
    given = termbase_path_from(["--term", "--termbase", "自定义库.csv", "目标.md"])
    assert given == Path("自定义库.csv"), given
    fallback = termbase_path_from(["--term", "目标.md"])
    assert fallback.name == "termbase.csv", fallback
    missing_value = termbase_path_from(["--term", "--termbase"])
    assert missing_value.name == "termbase.csv", missing_value


CJK_LATIN_SEARCH = None
LATIN_CJK_SEARCH = None

if __name__ == "__main__":
    import re
    from doccheck import CJK_LATIN, LATIN_CJK
    CJK_LATIN_SEARCH = re.compile(CJK_LATIN).search
    LATIN_CJK_SEARCH = re.compile(LATIN_CJK).search
    passed = failed = 0
    for name, fn in CASES:
        try:
            fn()
            passed += 1
            print(f"通过  {name}")
        except AssertionError as exc:
            failed += 1
            print(f"失败  {name}  {exc}")
    print(f"\n合计 {passed + failed} 项，通过 {passed} 项，失败 {failed} 项")
    sys.exit(1 if failed else 0)
