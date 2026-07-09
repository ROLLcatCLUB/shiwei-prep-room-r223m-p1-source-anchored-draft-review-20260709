#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223M_P1_teacher_readable_integrated_draft_v2.md",
    "R223M_P1_teacher_readable_integrated_draft_v2.html",
    "R223M_P1_source_anchor_table.md",
    "R223M_P1_gold_sample_language_recovery_notes.md",
    "R223M_P1_teacher_talk_polish_notes.md",
    "R223M_P1_evidence_alignment_notes.md",
    "R223M_P1_before_after_compare_with_R223M.md",
    "R223M_P1_report.md",
    "README_FOR_GPT_REVIEW.md",
    "README.md",
]

GOLD_LANGUAGE = [
    "智造·新朋友",
    "忆一忆：毛笔的诞生",
    "探一探：关键的结构",
    "交流会：十万个为什么",
    "设计会：像设计师一样思考",
    "1+1 合作小设计",
    "1+n 文具大变身",
    "细细长长软软的线",
    "缠绕、盘圈",
    "笔友汇",
    "赠笔礼",
    "购买文具建议书",
    "文具课堂使用指南",
]

MAIN_SECTIONS = [
    "一、课时定位",
    "二、教学依据",
    "三、教学目标",
    "四、教学重难点",
    "五、教学准备",
    "六、教学过程",
    "七、评价与证据",
    "八、板书 / 大屏结构",
    "九、附：生成依据与推理链说明",
]

SOURCE_STATUS = [
    "confirmed_from_uploaded_gold_sample_docx",
    "reconstructed_from_prior_audit",
    "system_reasoning",
    "teacher_adjusted",
]

EVALUATION_ANCHORS = [
    "我能发现新材料特性、新使用技法",
    "我能和小伙伴一起合作完成学习任务",
    "我能在展示会中自信表达自己的想法",
]

FORBIDDEN = [
    "正式 UI 已放行",
    "formal UI approved",
    "R97B route implemented",
    "provider call enabled",
    "database write enabled",
    "R224 started",
]


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def main():
    checks = []
    failures = []

    def check(name, passed, detail=""):
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        if not passed:
            failures.append({"name": name, "detail": detail})

    for name in REQUIRED_FILES:
        p = ROOT / name
        check(f"required_file:{name}", p.exists(), str(p))
        if p.exists():
            check(f"non_empty:{name}", p.stat().st_size > 0, str(p.stat().st_size))

    main_md = read("R223M_P1_teacher_readable_integrated_draft_v2.md")
    html = read("R223M_P1_teacher_readable_integrated_draft_v2.html")
    anchors = read("R223M_P1_source_anchor_table.md")
    recovery = read("R223M_P1_gold_sample_language_recovery_notes.md")
    talk = read("R223M_P1_teacher_talk_polish_notes.md")
    evidence = read("R223M_P1_evidence_alignment_notes.md")
    compare = read("R223M_P1_before_after_compare_with_R223M.md")
    report = read("R223M_P1_report.md")
    readme = read("README_FOR_GPT_REVIEW.md")

    for marker in MAIN_SECTIONS:
        check(f"main_section:{marker}", marker in main_md)

    for phrase in GOLD_LANGUAGE:
        check(f"gold_language_in_main:{phrase}", phrase in main_md)
        check(f"gold_language_in_recovery:{phrase}", phrase in recovery or phrase in anchors)

    for status in SOURCE_STATUS:
        check(f"source_status:{status}", status in anchors)

    for ev in EVALUATION_ANCHORS:
        check(f"evaluation_anchor:{ev}", ev in evidence and ev in main_md)

    check("html_stage_id", "1013R_R223M_P1_SOURCE_ANCHORED_TEACHER_DRAFT_HARDENING" in html)
    check("html_formal_ui_false", 'data-formal-ui="false"' in html)
    check("html_card_wall_false", 'data-card-wall="false"' in html)
    check("html_source_anchored_true", 'data-source-anchored="true"' in html)
    check("main_table_count_low", main_md.count("|") <= 2, str(main_md.count("|")))
    check("html_card_classes_absent", "component-card" not in html and "chain-node" not in html and "deep-card" not in html)
    check("teacher_talk_has_questions", "为什么彩铅" in main_md and "一支铅笔 + 一块粘土" in main_md)
    check("component_embedded_not_card_wall", "组件仍然只以内嵌教学动作出现" in main_md)
    check("source_files_named", "12.15《我为文具代言》.docx" in report and "上交教案.docx" in report and "学习手册.docx" in report)
    check("compare_keeps_output_form", "accepted teacher-readable" in compare or "teacher-readable" in compare)
    check("readme_blocks_formal_ui", "FORMAL_UI = BLOCKED" in readme or "formal UI = blocked" in readme)

    for label, content in [
        ("main", main_md),
        ("html", html),
        ("anchors", anchors),
        ("recovery", recovery),
        ("talk", talk),
        ("evidence", evidence),
        ("compare", compare),
        ("report", report),
        ("readme", readme),
    ]:
        for phrase in FORBIDDEN:
            check(f"forbidden_absent:{label}:{phrase}", phrase not in content)

    screenshot = ROOT / "R223M_P1_teacher_readable_integrated_draft_v2_screenshot.png"
    check("screenshot_exists", screenshot.exists())
    if screenshot.exists():
        check("screenshot_non_empty", screenshot.stat().st_size > 1000, str(screenshot.stat().st_size))

    smoke_path = ROOT / "R223M_P1_screenshot_smoke_result.json"
    if smoke_path.exists():
        try:
            smoke = json.loads(smoke_path.read_text(encoding="utf-8"))
            check("smoke_json_valid", True)
            check("smoke_no_horizontal_overflow", smoke.get("no_horizontal_overflow") is True)
            check("smoke_not_card_wall", smoke.get("card_like_count", 0) == 0, str(smoke.get("card_like_count")))
            check("smoke_key_sections_present", smoke.get("key_sections_present") is True)
        except Exception as exc:
            check("smoke_json_valid", False, repr(exc))

    result = {
        "passed": not failures,
        "check_count": len(checks),
        "failed": len(failures),
        "failures": failures,
        "checks": checks,
    }
    (ROOT / "validate_1013R_R223M_P1_source_anchored_teacher_draft_hardening_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"passed": result["passed"], "check_count": result["check_count"], "failed": result["failed"]}, ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

