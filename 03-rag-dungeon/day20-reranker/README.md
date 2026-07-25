# Day 20: Reranker（重排序）

> **今日目标**: 实现重排序，提升检索精度
> **核心问题**: 为什么检索后还需要重排序？

---

## 🎯 今日目标

1. 理解重排序的必要性
2. 掌握 bge-reranker 使用
3. 实现两阶段检索（召回 + 精排）
4. 理解 Cross-Encoder vs Bi-Encoder

---

## 📚 必学知识

### 1. 为什么需要重排序？

- 召回阶段：快速但粗糙（Top 20）
- 精排阶段：精确但慢（Top 5）
- 两阶段平衡效率和精度

### 2. 两阶段检索

```
查询
    ↓
[召回阶段] → Top 20（Bi-Encoder / 混合检索）
    ↓
[精排阶段] → Top 5（Reranker / Cross-Encoder）
    ↓
返回给 LLM
```

### 3. Cross-Encoder vs Bi-Encoder

| 维度 | Bi-Encoder | Cross-Encoder |
|------|------------|---------------|
| 原理 | 分别编码查询和文档 | 拼接查询+文档一起编码 |
| 速度 | 快 | 慢 |
| 精度 | 中等 | 高 |
| 阶段 | 召回 | 精排 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| bge-reranker | https://huggingface.co/BAAI/bge-reranker-v2-m3 |
| Reranker 论文 | https://arxiv.org/abs/2309.07568 |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 两阶段检索
- [ ] Cross-Encoder 原理
- [ ] bge-reranker 使用

---

## 💻 今日编码任务

### 文件结构

```
day20-reranker/
├── README.md
├── LEARNING_FLOW.md
├── 00_two_stage_retrieval.py    # 两阶段检索
└── 99-boss-answer.md
```

### Task 1: reranker_demo.py（45min）

实现 Reranker 演示

### Task 2: two_stage_retrieval.py（60min）

实现两阶段检索（召回 + 精排）

---

## 🐉 今日 Boss

1. **为什么需要重排序？**
2. **Cross-Encoder 和 Bi-Encoder 的区别？**
3. **两阶段检索的优势？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| reranker_demo.py | 40分 |
| two_stage_retrieval.py | 40分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 21: Query Rewrite / HyDE**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释重排序的必要性（召回阶段的局限）
- 解释 Cross-Encoder 和 Bi-Encoder 的区别
- 帮你调试代码报错
- 对比不同 Reranker 模型的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解数据库的二级索引，但 Cross-Encoder 不太熟，请解释一下它和 Bi-Encoder 的本质区别，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的重排序系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
03-rag-dungeon/
└── day20-reranker/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_two_stage_retrieval.py # 两阶段检索
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 20 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Reranker | ... | ... |
| Cross-Encoder | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 03-rag-dungeon/day20-reranker/
git commit -m "feat(day20): Reranker - 两阶段检索与重排序完成"
```

---

## 📊 今日检查清单

- [ ] 读了 bge-reranker 相关资料
- [ ] 写了 00_two_stage_retrieval.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
