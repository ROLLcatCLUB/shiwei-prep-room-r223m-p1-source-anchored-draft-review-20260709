# R223M-P1 Source Anchor Table

```text
stage_id=1013R_R223M_P1_SOURCE_ANCHORED_TEACHER_DRAFT_HARDENING
status=source_anchor_table
formal_ui=blocked
```

## Source Files

| Source ID | File | Role |
| --- | --- | --- |
| S1 | `12.15《我为文具代言》.docx` | 大单元设计、单元结构、单元评价表、完整阶段链 |
| S2 | `上交教案.docx` | 第三阶段“智造新朋友”课时教案、活动流程、话术、设计意图 |
| S3 | `学习手册.docx` | 学习单、毛笔工序、十万个为什么问题 |
| P2 | `R223L_P2_overall_reasoning_chain_product.md` | 推理链产品视图 |
| M | `R223M_teacher_readable_integrated_draft.md` | 已通过形式审核的教师可读整合稿 |

## Anchor Status Legend

```text
confirmed_from_uploaded_gold_sample_docx = 原始 docx 明确出现
reconstructed_from_prior_audit = 前序 R221/R223 审计复原
system_reasoning = 系统根据链条生成的表达或连接
teacher_adjusted = 根据本轮教师审核意见强化或转写
```

## Field Anchors

| Field | Source Status | Evidence | P1 Use |
| --- | --- | --- | --- |
| 大观念 | confirmed_from_uploaded_gold_sample_docx | S1/S2: “体验传统工艺，带着好奇心和想象力设计改进文具从而改善学习生活。” | 保留为教学依据首段 |
| 基本问题 | confirmed_from_uploaded_gold_sample_docx | S1/S2: “怎样全方面了解文具，并感受它的重要性？” | 转成本课核心问题 |
| 单元目标 | confirmed_from_uploaded_gold_sample_docx | S1/S2: 观察外形、色彩、功能、材质；改进设计；感受中国制造到中国智造和传统工艺价值 | 支撑目标和课时定位 |
| 表现性任务 | confirmed_from_uploaded_gold_sample_docx | S1/S2: “形成《一年级购买文具建议书》、《文具课堂使用指南》。” | 进入评价与单元连接 |
| 第三阶段责任 | confirmed_from_uploaded_gold_sample_docx | S1: “智造·新朋友”；S2: 本阶段引导学生选择综合材料和制作技法优化改造文具并开展交流会 | 作为课时定位核心 |
| 忆一忆：毛笔的诞生 | confirmed_from_uploaded_gold_sample_docx | S1/S2/S3 均出现 | 保留为导入与学习单任务 |
| 探一探：关键的结构 | confirmed_from_uploaded_gold_sample_docx | S1/S2 出现 | 保留为观察环节 |
| 交流会：十万个为什么 | confirmed_from_uploaded_gold_sample_docx | S2/S3: 彩铅衣服、毛笔小尾巴、水彩笔笔盖、圆珠笔笔尖等问题 | 恢复为课堂问题群 |
| 设计会：像设计师一样思考 | confirmed_from_uploaded_gold_sample_docx | S1/S2 出现；S2 提到握笔皮圈、笔夹、橡皮笔套、磁吸白板笔 | 恢复为设计意识转折 |
| 1+1 合作小设计 | confirmed_from_uploaded_gold_sample_docx | S1/S2: “一支铅笔+一块粘土能有多少种设计呢？” | 保留为支架活动 |
| 1+n 文具大变身 | confirmed_from_uploaded_gold_sample_docx | S1/S2: 选择合适材料，用 1-2 种技法，智造一支“新朋友” | 保留为创作主任务 |
| 细细长长软软的线可以缠绕、盘圈 | confirmed_from_uploaded_gold_sample_docx | S1/S2: 线形材料共同特性和“盘”技法 | 恢复到技法归纳 |
| 笔友汇 | confirmed_from_uploaded_gold_sample_docx | S1/S2: 展示架、词云图关键词、点评“新朋友” | 保留为分享评价 |
| 赠笔礼 | confirmed_from_uploaded_gold_sample_docx | S1/S2: 互赠笔墨仪式，送给他人或自己 | 保留为仪式收束 |
| 评价证据 | confirmed_from_uploaded_gold_sample_docx | S1 评价表: 发现新材料特性、新使用技法；合作完成学习任务；展示会自信表达 | 进入评价与证据 |
| 组件嵌入 | system_reasoning + teacher_adjusted | R222D/R223M 组件原则，S2 中已有圈画、投屏、词云、学习单等动作 | 不作为卡片，嵌入教学动作 |

## Boundary

```text
This table anchors teacher draft content only.
It does not authorize UI, R97B, runtime, model, prompt, database, or formal apply.
```

