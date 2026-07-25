export const meta = {
  name: 'restructure-modules',
  description: '并行改造 02-08 共 7 个模块、47 个 day 文件夹，统一到 01-newbie-village 保姆级教学结构',
  phases: [
    { title: '并行改造 7 个模块', detail: '7 个子 agent 同时处理 02-08 模块' },
    { title: '汇总报告', detail: '收集各 agent 结果，输出改造汇总' }
  ]
}

phase('并行改造 7 个模块')

const MODULES = [
  { name: '02-langchain-academy', days: 7 },
  { name: '03-rag-dungeon', days: 8 },
  { name: '04-mcp-a2a-multiagent', days: 9 },
  { name: '05-production-agent', days: 7 },
  { name: '06-evaluation-graphrag', days: 7 },
  { name: '07-llm-engineering', days: 5 },
  { name: '08-final-projects', days: 4 },
]

log('🚀 开始并行改造 7 个模块...')

const results = await parallel(
  MODULES.map(m => () => restructureModule(m))
)

phase('汇总报告')

log('\n\n📊 ===== 改造汇总 =====')
for (const r of results) {
  log(`\n${r}`)
}

return { results }

async function restructureModule(module) {
  const prompt = `
# 任务：改造 ${module.name} 模块为"新手村保姆级教学"结构

你是"新手村保姆级教学"重构项目的子 Agent。请改造 **${module.name}** 模块的全部 day 文件夹（共 ${module.days} 个）。

## 工作目录
项目根目录：/Users/null/PycharmProjects/Ai/agent-journey-60d
模块路径：/Users/null/PycharmProjects/Ai/agent-journey-60d/${module.name}

## 参照模板（务必先读取）
1. /Users/null/PycharmProjects/Ai/agent-journey-60d/templates/AGENT_INSTRUCTIONS.md — 详细任务说明
2. /Users/null/PycharmProjects/Ai/agent-journey-60d/templates/LEARNING_FLOW_TEMPLATE.md — LEARNING_FLOW.md 模板
3. /Users/null/PycharmProjects/Ai/agent-journey-60d/templates/README_APPENDIX_TEMPLATE.md — README 追加章节模板
4. /Users/null/PycharmProjects/Ai/agent-journey-60d/01-newbie-village/day01-llm-foundation/ — 完整样例

## 每个 day 文件夹的工作

### 1. 读取现有内容
- 读取 README.md、列出 .py 文件、读取 boss 答案文件

### 2. 重命名文件（用 git mv）
- boss-answer.md → 99-boss-answer.md
- 99_boss_answer.md → 99-boss-answer.md（统一短横线）
- .py 文件按字母顺序加 00_、01_、02_... 前缀
- 不改名：requirements.txt、output/ 目录、子目录内部文件

### 3. 新建 LEARNING_FLOW.md
- 动态生成学习顺序（每个 .py 一个 Step）
- 时间分配表（阅读 7min + 代码 + Boss 30min + 总结 15min）
- 验证清单（4-6 条 + 最后一条"能回答 Boss X 题"）
- 快速导航表

### 4. 改造 README.md
- 保留原有章节（🎯📚🔗🧠💻🐉🎤⭐🔓）
- 追加 3 章节（🤖📝📊）
- 同步更新"文件结构"代码块为新文件名

### 5. 内部一致性检查
- README 文件树 vs 实际文件 → 一致
- LEARNING_FLOW 快速导航 vs 实际文件 → 一致

## 注意事项
- 用 git mv 重命名，不用 mv
- 不要删除任何文件
- 保留 README 原有内容，只追加不修改
- LEARNING_FLOW 必须基于该 day 实际文件动态生成
- 完成所有 day 后再报告

## 完成后报告格式
✅ ${module.name} 改造完成

- 改造 day 数：X
- 新建 LEARNING_FLOW.md：X 个
- 重命名 boss 文件：X 个
- 重命名 .py 文件：X 个
- 追加 README 3 章节：X 个

关键变更：
（列出 git status 关键变更）
`

  return await agent(prompt, { label: `restructure-${module.name}` })
}
