# Day 41 Boss 答案

## 1. RAGAS 提供哪些指标？

| 指标 | 说明 | 维度 |
|------|------|------|
| Faithfulness | 回答是否基于上下文 | 生成质量 |
| Answer Relevancy | 回答是否切题 | 生成质量 |
| Context Recall | 上下文是否覆盖答案所需信息 | 检索质量 |
| Context Precision | 上下文是否相关，没有噪声 | 检索质量 |

## 2. Faithfulness 和 Answer Relevancy 的区别？

| 维度 | Faithfulness | Answer Relevancy |
|------|--------------|------------------|
| 关注 | 回答是否基于上下文 | 回答是否切题 |
| 问题 | 幻觉 | 偏题 |
| 评估 | 回答与上下文的关系 | 回答与问题的关系 |

## 3. Context Recall 和 Context Precision 的区别？

| 维度 | Context Recall | Context Precision |
|------|----------------|-------------------|
| 关注 | 覆盖率 | 准确性 |
| 问题 | 漏掉相关信息 | 包含噪声 |
| 侧重 | 数量 | 质量 |
