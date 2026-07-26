# Day 63 Boss 答案

## 1. 多模态模型有哪 5 种方向？各自的应用场景是什么？

多模态模型按照输入输出方向可以分为 5 种：

**文生图（Text-to-Image）**：输入文本，输出图像。典型模型 Stable Diffusion / DALL·E 3 / Midjourney，应用于海报设计、电商主图、概念图生成。

**文生视频（Text-to-Video）**：输入文本，输出视频。典型模型 Sora / Kling / 可灵，应用于短视频、广告、创意视频。

**图生视频（Image-to-Video）**：输入图像，输出视频。典型模型 Runway / Pika，应用于创意视频、动态海报。

**图生文（Image-to-Text / VLM）**：输入图像，输出文本。典型模型 LLaVA / Qwen-VL / GPT-4o，应用于 OCR、图表理解、财报分析。

**视觉问答（VQA）**：输入图像 + 文本，输出文本。典型模型 GPT-4o / Gemini，应用于多模态 Agent、智能客服。

**对 Agent 的意义**：多模态 Agent 需要根据用户输入类型（文本/图像/语音/PDF）调用对应的多模态工具，实现"看、听、说、画"的完整能力。

## 2. VLM 调用方式和普通 LLM 调用有什么区别？

**普通 LLM 调用**：
- Message 的 content 是纯文本字符串
- 只处理文本信息

**VLM 调用**：
- Message 的 content 是一个**数组**，包含多个部分（Part）
- 每个部分可以是文本（type: text）或图像（type: image_url）
- 图像支持 URL 或 Base64 编码

**代码对比**：
```python
# 普通 LLM
{"role": "user", "content": "这张图片是什么？"}

# VLM
{"role": "user", "content": [
    {"type": "text", "text": "这张图片是什么？"},
    {"type": "image_url", "image_url": {"url": "https://..."}}
]}
```

**本质区别**：
- VLM 在模型内部融合了视觉编码器（ViT）和语言模型
- 图像被编码为视觉 Token，和文本 Token 一起输入 Transformer
- 因此 VLM 能"看到"图像内容并生成文本描述

**对 Agent 的启示**：Agent 的 User Message 不再只是文本，可以包含截图、照片、PDF 图像等多模态信息。

## 3. Whisper + TTS 完整链路是什么？延迟要求是多少？

**完整链路**：
```
用户语音
    ↓
Whisper（STT，语音转文字）
    ↓
文本
    ↓
Agent 处理（LLM + 工具）
    ↓
回复文本
    ↓
TTS（文字转语音）
    ↓
语音回复
```

**Whisper（Speech-to-Text）**：
- OpenAI 开源，支持 99 种语言
- 中文效果好，支持粤语、方言
- 模型大小：tiny / base / small / medium / large
- 延迟：large 模型约 300ms（GPU）

**TTS（Text-to-Speech）**：
- OpenAI TTS：音质好，支持多种声音
- Azure TTS：企业级，支持自定义声音
- Edge TTS：免费，基于 Edge
- ChatTTS：本地部署，中文效果好

**延迟要求**：
- STT < 300ms（用户说完到文字输出）
- 首字 TTS < 200ms（开始语音输出）
- 端到端 < 1s（用户说完到听到回复）

**对 Agent 的启示**：语音 Agent 的延迟是用户体验的关键，需要优化 STT/TTS 模型和流式输出。

## 4. 多模态 Agent 架构中，输入路由器应该如何设计？

**输入路由器（Input Router）** 是多模态 Agent 的核心组件，负责根据输入类型分发到不同的处理模块：

**设计要点**：
1. **类型识别**：自动识别输入类型（文本/图像/语音/PDF/视频）
2. **分发策略**：
   - 文本 → 直接给 LLM
   - 图像 → VLM 理解
   - 语音 → Whisper 转文字 → LLM
   - PDF → OCR 提取 → LLM
   - 视频 → 抽帧 → VLM 理解
3. **多模态混合**：支持多种输入同时存在（如文本 + 图像）
4. **Fallback**：无法识别时，提示用户

**伪代码**：
```python
def input_router(user_input):
    if user_input.type == "text":
        return llm.process(user_input.content)
    elif user_input.type == "image":
        return vlm.describe(user_input.content)
    elif user_input.type == "audio":
        text = whisper.transcribe(user_input.content)
        return llm.process(text)
    elif user_input.type == "pdf":
        text = ocr.extract(user_input.content)
        return llm.process(text)
```

**对 Agent 的启示**：输入路由器让 Agent 具备"多感官"能力，是通用 Agent 的基础。

## 5. PDF 财报 OCR 需要哪些核心能力？A 股投研场景如何应用？

**PDF 财报 OCR 核心能力**：

1. **表格识别**：提取资产负债表、利润表、现金流量表
2. **版面分析**：识别标题、段落、表格、图表位置
3. **OCR 文字识别**：识别印刷体和手写体文字
4. **结构化输出**：输出 JSON / Excel 等结构化数据

**OCR 引擎**：
- **PaddleOCR**：百度开源，中文效果好
- **Tesseract**：Google 开源，多语言
- **商业 OCR**：百度/腾讯/阿里 OCR API（精度高）
- **多模态 OCR**：GPT-4o 直接理解 PDF 截图（最先进）

**A 股投研场景应用**：
- **公告 PDF**：提取增减持、重大合同、重组等关键事件
- **研报**：提取评级、目标价、核心逻辑、风险提示
- **财报**：提取营业收入、净利润、毛利率、ROE 等核心指标
- **K 线截图**：技术面分析（支撑位、压力位、MACD、KDJ）

**实际案例**：
- 每天自动扫描 100+ 份公告 PDF，提取关键事件
- 自动生成财报摘要，对比同行业公司
- 结合 K 线图分析，给出投资建议

**对 Agent 的启示**：多模态 Agent 在金融领域的应用非常广泛，OCR 是基础能力。
