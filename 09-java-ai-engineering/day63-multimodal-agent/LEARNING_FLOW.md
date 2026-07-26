# Day 63: Multimodal Agent - 学习流程

> **今日目标**: 打通多模态 Agent 的完整链路：文生图/图生文/语音/视频
> **核心问题**: 如何让 Agent 同时"看、听、说、画"？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_vlm_demo.py（40分钟）
    ↓ 理解：VLM 调用方式 + 图像分析
Step 4: 运行 01_pdf_ocr.py（50分钟）
    ↓ 理解：PDF 财报 OCR + 表格识别
Step 5: 运行 02_multimodal_agent.py（60分钟）
    ↓ 理解：多模态 Agent 架构 + 输入路由
Step 6: 运行 03_tts_stt.py（40分钟）
    ↓ 理解：Whisper + TTS 完整链路
Step 7: 完成 99-boss-answer.md（30分钟）
    ↓
Step 8: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-6 | 4 个代码文件 | 190min |
| 7 | Boss 问题 | 30min |
| 8 | 学习总结 | 15min |
| **总计** | | **约 4h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释多模态模型的 5 种方向
- [ ] 解释 VLM 调用方式和普通 LLM 的区别
- [ ] 解释 Whisper + TTS 完整链路
- [ ] 解释多模态 Agent 架构设计
- [ ] 能独立实现 PDF 财报 OCR
- [ ] 能回答 Boss 5 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_vlm_demo.py](00_vlm_demo.py) | VLM 调用演示 | ⭐⭐ |
| [01_pdf_ocr.py](01_pdf_ocr.py) | PDF 财报 OCR | ⭐⭐⭐ |
| [02_multimodal_agent.py](02_multimodal_agent.py) | 多模态 Agent | ⭐⭐⭐⭐ |
| [03_tts_stt.py](03_tts_stt.py) | 语音链路 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
