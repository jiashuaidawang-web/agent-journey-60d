# 子 Agent 任务说明

> 你是"新手村保姆级教学"重构项目的子 Agent。请严格按以下步骤改造你负责的模块。

## 你的任务

改造 **<MODULE_NAME>** 模块的 **全部 day 文件夹**（共 <N> 个），统一到 01-newbie-village 风格。

## 参照模板

- `templates/LEARNING_FLOW_TEMPLATE.md` — LEARNING_FLOW.md 的结构模板
- `templates/README_APPENDIX_TEMPLATE.md` — README 需追加的 3 章节模板
- `01-newbie-village/day01-llm-foundation/` — 完整样例（7 个 day 都是参照标准）

## 每个 day 文件夹的工作清单

### 步骤 1：读取现有内容
- 读取 `README.md`（理解该 day 的主题、Boss 题目数量、编码任务）
- 列出该 day 的全部 `.py` 文件
- 读取 `99_boss_answer.md` 或 `boss-answer.md`（了解 Boss 题目数量）

### 步骤 2：重命名文件
- `boss-answer.md` → `99-boss-answer.md`（用 `git mv` 保持历史）
- 所有 `.py` 文件按**字母顺序**加数字前缀：`00_`、`01_`、`02_`...
  - 例外：`requirements.txt`、`output/` 目录、子目录内部文件不改名
- 示例：
  - `embedding_demo.py` → `00_embedding_demo.py`
  - `similarity_demo.py` → `01_similarity_demo.py`

### 步骤 3：新建 `LEARNING_FLOW.md`
- 参照 `templates/LEARNING_FLOW_TEMPLATE.md`
- **动态生成**"学习顺序"步骤：每个 `.py` 文件一个 Step，写清文件名、时间、理解目标
- 时间分配表：阅读文档 7min + 代码文件 + Boss 30min + 学习总结 15min
- 验证清单：4-6 条能力 + 最后一条"能回答 Boss X 题"
- 快速导航：每个 .py 一行 + 最后一行 99-boss-answer.md

### 步骤 4：改造 `README.md`
- **保留**原有章节（🎯📚🔗🧠💻🐉🎤⭐🔓）
- **追加** 3 章节（🤖📝📊）— 参照 `templates/README_APPENDIX_TEMPLATE.md`
- **同步更新**"文件结构"代码块为新文件名
- 检查"快速导航"表（如有）同步更新

### 步骤 5：内部一致性检查
- README 的"文件结构"代码块 vs 实际文件名 → 必须一致
- LEARNING_FLOW 的"快速导航" vs 实际文件名 → 必须一致
- LEARNING_FLOW 的"验证清单"最后一条"能回答 Boss X 题" vs 实际 Boss 题目数 → 必须一致

## 命名规范（强制）

| 项目 | 规范 | 示例 |
|------|------|------|
| Boss 答案 | `99-boss-answer.md`（短横线，99- 前缀） | `99-boss-answer.md` |
| 代码文件 | `NN_<name>.py`（数字前缀 + 下划线 + 原名） | `00_embedding_demo.py` |
| 学习流程 | `LEARNING_FLOW.md`（固定） | `LEARNING_FLOW.md` |

## 注意事项

1. **用 `git mv` 重命名**，不要 `mv`（保持 git 历史）
2. **不要删除**任何文件
3. **保留** README 原有内容，只追加不修改
4. **动态生成**：LEARNING_FLOW 必须基于该 day 的实际文件，不能套空模板
5. **完成所有 day 后再报告**，不要每个 day 单独报告

## 完成后输出

报告格式：
```
✅ <MODULE_NAME> 改造完成

- 改造 day 数：X
- 新建 LEARNING_FLOW.md：X 个
- 重命名 boss-answer.md：X 个
- 重命名 .py 文件：X 个
- 追加 README 3 章节：X 个

文件清单：
<列出 git status 的关键变更>
```
