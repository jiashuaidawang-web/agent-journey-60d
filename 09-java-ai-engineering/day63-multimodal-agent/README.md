# Day 63: Multimodal Agent

> **今日目标**: 打通多模态 Agent 的完整链路：文生图/图生文/语音/视频
> **核心问题**: 如何让 Agent 同时"看、听、说、画"？

---

## 🎯 今日目标

1. 理解多模态模型分类：文生图/文生视频/图生视频/图生文/视觉问答
2. 掌握 VLM 视觉语言模型（LLaVA / Qwen-VL / GPT-4o）的调用方式
3. 实现 Whisper 语音转文字 + TTS 文字转语音的完整链路
4. 设计多模态 Agent 架构（输入路由 + 多模态工具）
5. 实战 PDF/财报 OCR（表格识别 + 版面分析）
6. 落地 A 股投研场景（公告 PDF / 研报 / 财报 / K 线截图）

---

## 📚 必学知识

### 1. 多模态模型概览

| 模态方向 | 输入 | 输出 | 典型模型 | 应用场景 |
|----------|------|------|----------|----------|
| 文生图 | 文本 | 图像 | Stable Diffusion / DALL·E 3 / Midjourney | 海报、设计稿 |
| 文生视频 | 文本 | 视频 | Sora / Kling / 可灵 | 短视频、广告 |
| 图生视频 | 图像 | 视频 | Runway / Pika | 创意视频 |
| 图生文 | 图像 | 文本 | LLaVA / Qwen-VL / GPT-4o | OCR、图表理解 |
| 视觉问答 | 图像 + 文本 | 文本 | GPT-4o / Gemini | 多模态 Agent |

### 2. VLM 视觉语言模型

**VLM（Vision-Language Model）** 是 Agent "看世界"的核心：

- **LLaVA**：开源，LLaMA + ViT，学术常用
- **Qwen-VL**：阿里开源，中文场景强，支持 OCR
- **GPT-4o**：闭源最强，支持图像 + 文本 + 音频
- **Gemini**：Google 多模态，原生支持视频

**调用方式**：
```python
# 图像 URL / Base64 作为 User Message 的一部分
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "这张图片是什么？"},
            {"type": "image_url", "image_url": {"url": "https://..."}}
        ]}
    ]
)
```

### 3. 语音链路：Whisper + TTS

**完整链路**：
```
用户语音 → Whisper(STT) → 文本 → Agent → 回复文本 → TTS → 语音
```

- **Whisper**：OpenAI 开源 STT，支持 99 种语言，中文效果好
- **TTS**：OpenAI TTS / Azure TTS / Edge TTS / 本地 ChatTTS
- **延迟要求**：STT < 300ms，首字 TTS < 200ms

### 4. 多模态 Agent 架构

```
用户输入（文本/图像/语音/PDF）
    ↓
输入路由器（Input Router）
    ↓
┌─────────────────────────────────┐
│  文本 → LLM                     │
│  图像 → VLM 理解                │
│  语音 → Whisper → 文本 → LLM    │
│  PDF  → OCR → 文本 → LLM        │
│  图表 → VLM 分析                │
└─────────────────────────────────┘
    ↓
Agent 决策
    ↓
┌─────────────────────────────────┐
│  文本回复                       │
│  图像生成（文生图）             │
│  语音回复（TTS）                │
│  图表生成（matplotlib/plotly）  │
└─────────────────────────────────┘
```

### 5. PDF/财报 OCR 实战

**核心能力**：
- **表格识别**：提取财报中的资产负债表、利润表
- **版面分析**：识别标题、段落、表格、图表位置
- **OCR 引擎**：PaddleOCR / Tesseract / 商业 OCR（百度/腾讯）
- **多模态 OCR**：GPT-4o 直接理解 PDF 截图

**A 股投研场景**：
- 公告 PDF → 提取关键事件（增减持、重大合同）
- 研报 → 提取评级、目标价、核心逻辑
- 财报 → 提取核心财务指标
- K 线截图 → 技术面分析

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| OpenAI Vision API | https://platform.openai.com/docs/guides/vision |
| OpenAI Whisper | https://platform.openai.com/docs/guides/speech-to-text |
| OpenAI TTS | https://platform.openai.com/docs/guides/text-to-speech |
| LLaVA 论文 | https://llava-vl.github.io/ |
| Qwen-VL | https://github.com/QwenLM/Qwen-VL |
| Stable Diffusion | https://github.com/CompVis/stable-diffusion |
| PaddleOCR | https://github.com/PaddlePaddle/PaddleOCR |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] 多模态模型分类（5 种方向）
- [ ] VLM 调用方式（图像作为 Message）
- [ ] Whisper + TTS 完整链路
- [ ] 多模态 Agent 架构设计
- [ ] PDF OCR 实战（表格识别）
- [ ] A 股投研场景应用

### 只需理解（L3）
- [ ] Stable Diffusion 原理（扩散模型）
- [ ] Whisper 模型结构（Encoder-Decoder）
- [ ] TTS 声学模型
- [ ] 视频生成模型原理

### 今天不深入（后面会讲）
- [ ] 多模态 Embedding
- [ ] 视频理解模型
- [ ] 实时语音对话
- [ ] 多模态 RAG

---

## 💻 今日编码任务

### 文件结构

```
day63-multimodal-agent/
├── README.md
├── LEARNING_FLOW.md
├── 00_vlm_demo.py              # VLM 调用演示
├── 01_pdf_ocr.py               # PDF 财报 OCR
├── 02_multimodal_agent.py      # 多模态 Agent
├── 03_tts_stt.py               # 语音链路
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: 00_vlm_demo.py（40min）

实现 VLM 调用：
- 支持图像 URL / Base64 输入
- 调用 GPT-4o / Qwen-VL 分析图像
- 输出图像描述 + 关键信息提取

**验收标准**：
```bash
python 00_vlm_demo.py --image "https://example.com/chart.png"
# 输出：
# 📷 图像分析结果：
# 这是一张 K 线图，显示某股票近 30 天走势...
# 关键信息：最新价 15.2，涨跌幅 +3.5%
```

### Task 2: 01_pdf_ocr.py（50min）

实现 PDF 财报 OCR：
- 读取 PDF 文件
- 提取表格（资产负债表）
- 提取关键财务指标
- 输出结构化 JSON

**验收标准**：
```bash
python 01_pdf_ocr.py --file "财报.pdf"
# 输出：
# 📄 财报分析结果：
# 公司名称：XX科技
# 营业收入：10.5 亿（同比 +15%）
# 净利润：1.2 亿（同比 +8%）
```

### Task 3: 02_multimodal_agent.py（60min）

实现多模态 Agent：
- 输入路由器（文本/图像/语音/PDF）
- 调用对应多模态工具
- 输出多模态回复

**验收标准**：
```bash
python 02_multimodal_agent.py
# 输出：
# 🤖 多模态 Agent 启动
# 请输入（支持文本/图像路径/语音/PDF）：
```

### Task 4: 03_tts_stt.py（40min）

实现语音链路：
- Whisper 语音转文字
- TTS 文字转语音
- 完整语音对话演示

**验收标准**：
```bash
python 03_tts_stt.py --audio "input.wav"
# 输出：
# 🎤 语音识别结果：请分析一下贵州茅台的财报
# 🔊 语音回复已生成：output.wav
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释多模态模型分类和适用场景
- 解释 VLM 调用方式（图像作为 Message）
- 帮你调试 OCR 代码报错
- 解释 Whisper + TTS 链路

### 今天 AI 不能帮你
- 替你理解多模态 Agent 架构（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 10 年 Java 经验，VLM 调用方式不太理解。请用 Java 的 InputStream 类比解释一下图像作为 Message 的传递方式。"

### 错误用法
> "帮我写一个完整的多模态 Agent。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day63-multimodal-agent/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_vlm_demo.py      # VLM 调用
    ├── 01_pdf_ocr.py       # PDF OCR
    ├── 02_multimodal_agent.py  # 多模态 Agent
    ├── 03_tts_stt.py       # 语音链路
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 63 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| VLM | ... | ... |
| Whisper | ... | ... |
| 多模态 Agent | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day63-multimodal-agent/
git commit -m "feat(day63): Multimodal Agent - 多模态完整链路打通"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **多模态模型有哪 5 种方向？各自的应用场景是什么？**
2. **VLM 调用方式和普通 LLM 调用有什么区别？**
3. **Whisper + TTS 完整链路是什么？延迟要求是多少？**
4. **多模态 Agent 架构中，输入路由器应该如何设计？**
5. **PDF 财报 OCR 需要哪些核心能力？A 股投研场景如何应用？**

### 验收标准
- 每个答案 **不少于 80 字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码运行结果** 来讲

---

## 🎤 面试题

1. **VLM 和普通 LLM 的本质区别是什么？**
2. **文生图模型（Stable Diffusion）的核心原理是什么？**
3. **语音 Agent 的延迟瓶颈在哪里？如何优化？**
4. **多模态 Agent 如何处理不同类型的输入？**
5. **PDF OCR 的难点是什么？如何提升表格识别准确率？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_vlm_demo.py | 20分 | 能调用 VLM + 分析图像 |
| 01_pdf_ocr.py | 20分 | 能提取表格 + 关键指标 |
| 02_multimodal_agent.py | 20分 | 能路由 + 多模态输出 |
| 03_tts_stt.py | 15分 | 能语音转文字 + 文字转语音 |
| README 学习总结 | 10分 | 有自己的理解，不是抄的 |
| Boss 答案 | 15分 | 5 题全部完成 + 用自己的话 |

---

## 🔓 解锁条件

- [ ] 4 个代码文件全部能运行
- [ ] Boss 5 题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 64: RAG 底层原理加深**

---

## 📊 今日检查清单

- [ ] 读了 OpenAI Vision 文档
- [ ] 读了 OpenAI Whisper 文档
- [ ] 读了 LLaVA / Qwen-VL 资料
- [ ] 写了 00_vlm_demo.py
- [ ] 写了 01_pdf_ocr.py
- [ ] 写了 02_multimodal_agent.py
- [ ] 写了 03_tts_stt.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
