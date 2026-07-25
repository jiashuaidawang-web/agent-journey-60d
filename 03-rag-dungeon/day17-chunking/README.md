# Day 17: Chunking（文档分块）

> **今日目标**: 掌握文档分块策略
> **核心问题**: 为什么文档不能直接塞进向量库？

---

## 🎯 今日目标

1. 理解分块的必要性
2. 掌握 4 种分块策略
3. 实现分块对比实验
4. 理解 Chunk Size 的影响

---

## 📚 必学知识

### 1. 为什么要分块？

- Context Window 有限（如 4096 tokens）
- 长文档无法直接嵌入
- 小块更容易精确匹配
- 减少 Token 消耗

### 2. 分块策略

| 策略 | 说明 | 适用 |
|------|------|------|
| Fixed Size | 固定大小切分 | 通用 |
| Recursive | 按段落递归切长 | 结构化文档 |
| Semantic | 按语义切分 | 高质量需求 |
| Document | 按文档结构切分 | 有标题层级 |

### 3. 关键参数

- **Chunk Size**：每个块的大小（如 512 tokens）
- **Chunk Overlap**：块之间的重叠（如 50 tokens）
- 重叠可以防止信息在边界被切断

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangChain Text Splitters | https://python.langchain.com/docs/concepts/text_splitters/ |
| LlamaIndex Chunking | https://docs.llamaindex.ai/en/stable/optimizing/building_rag_best_practices/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 4 种分块策略
- [ ] Chunk Size 选择
- [ ] Overlap 的作用

---

## 💻 今日编码任务

### 文件结构

```
day17-chunking/
├── README.md
├── LEARNING_FLOW.md
├── 00_chunking_demo.py          # 分块演示
└── 99-boss-answer.md
```

### Task 1: chunking_demo.py（45min）

实现 4 种分块策略：
- Fixed Size
- Recursive
- Semantic
- Document

### Task 2: chunk_experiment.py（45min）

对比不同 Chunk Size 的效果

---

## 🐉 今日 Boss

1. **为什么文档要分块？**
2. **Chunk Size 如何影响检索效果？**
3. **Overlap 的作用是什么？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| chunking_demo.py | 45分 |
| chunk_experiment.py | 35分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 18: Dense Retrieval**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释文档分块的必要性（Context Window、嵌入模型限制）
- 解释不同分块策略的适用场景
- 帮你调试代码报错
- 对比不同 Chunk Size 对检索效果的影响

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 Java 经验，Python 的文本切分逻辑不太熟，请解释一下 Recursive Chunking 的递归逻辑，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的文档分块系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
03-rag-dungeon/
└── day17-chunking/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_chunking_demo.py  # 分块演示
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 17 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Chunking | ... | ... |
| Overlap | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 03-rag-dungeon/day17-chunking/
git commit -m "feat(day17): Chunking - 文档分块策略完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangChain Text Splitters 文档
- [ ] 写了 00_chunking_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
