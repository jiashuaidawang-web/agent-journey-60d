"""
Day 66: 模拟面试脚本 - 模拟 AI 架构师面试流程

功能：
1. 自我介绍（2 分钟）
2. 技术面试题（随机抽取）
3. 综合面试题
4. 评分反馈

示例：
    python 01_mock_interview.py
    python 01_mock_interview.py --role ai-architect

实际实现需要：
- openai（AI 面试官）

作者：Agent Journey 60D
日期：Day 66
"""

import argparse
import random
import time
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class InterviewQuestion:
    """面试题"""
    category: str
    question: str
    key_points: list[str] = field(default_factory=list)
    difficulty: int = 1  # 1-5


@dataclass
class InterviewAnswer:
    """面试答案"""
    question: InterviewQuestion
    answer: str
    score: int = 0  # 0-100
    feedback: str = ""


# 技术面试题库
TECH_QUESTIONS = [
    InterviewQuestion(
        category="LLM Foundation",
        question="请解释 Token 是什么？中英文 Token 化有什么区别？",
        key_points=["Token 定义", "英文 Token 化", "中文 Token 化", "对 Agent 的影响"],
        difficulty=2,
    ),
    InterviewQuestion(
        category="LLM Foundation",
        question="Context Window 是什么？为什么不能无限大？",
        key_points=["Context Window 定义", "计算复杂度", "显存限制", "成本", "Lost in the Middle"],
        difficulty=2,
    ),
    InterviewQuestion(
        category="LangGraph",
        question="State 为什么是一等公民？",
        key_points=["所有节点共享", "自动合并", "类型安全", "可序列化", "ApplicationContext 类比"],
        difficulty=3,
    ),
    InterviewQuestion(
        category="LangGraph",
        question="条件边和普通边有什么区别？",
        key_points=["普通边固定连接", "条件边动态决策", "适用场景", "Agent 循环"],
        difficulty=3,
    ),
    InterviewQuestion(
        category="RAG",
        question="向量数据库如何选型？",
        key_points=["PGVector", "Milvus", "Qdrant", "Chroma", "选型建议"],
        difficulty=3,
    ),
    InterviewQuestion(
        category="RAG",
        question="文档拆分有哪些策略？",
        key_points=["递归拆分", "语义拆分", "固定长度拆分", "中文专属拆分", "关键参数"],
        difficulty=3,
    ),
    InterviewQuestion(
        category="MCP / A2A",
        question="MCP 协议的核心概念是什么？",
        key_points=["Server", "Client", "Transport", "Tool", "Resource", "标准化优势"],
        difficulty=3,
    ),
    InterviewQuestion(
        category="Multi-Agent",
        question="Supervisor 模式的核心思想是什么？",
        key_points=["Supervisor 协调", "Worker 执行", "职责分离", "可扩展", "适用场景"],
        difficulty=4,
    ),
    InterviewQuestion(
        category="Spring AI",
        question="Spring AI 的核心概念是什么？",
        key_points=["AiClient", "Prompt", "Embedding", "VectorStore", "FunctionCallback", "RAG"],
        difficulty=3,
    ),
    InterviewQuestion(
        category="Memory",
        question="Agent 的记忆体系是怎样的？",
        key_points=["Short-term", "Long-term", "Session", "记忆管理策略"],
        difficulty=3,
    ),
    InterviewQuestion(
        category="微调",
        question="LoRA 微调的核心思想是什么？",
        key_points=["冻结参数", "低秩矩阵", "参数高效", "显存友好", "可组合"],
        difficulty=4,
    ),
    InterviewQuestion(
        category="多模态",
        question="多模态 Agent 的核心能力是什么？",
        key_points=["VLM", "Whisper", "TTS", "文生图", "输入路由器"],
        difficulty=4,
    ),
]

# 综合面试题库
GENERAL_QUESTIONS = [
    InterviewQuestion(
        category="自我介绍",
        question="请用 2 分钟自我介绍，重点介绍你的 AI 学习经历。",
        key_points=["背景", "学习成果", "项目经验", "优势"],
        difficulty=2,
    ),
    InterviewQuestion(
        category="架构设计",
        question="设计一个企业级 Agent 平台，你会怎么做？",
        key_points=["分层架构", "Agent Orchestrator", "Tool Registry", "Memory Layer", "Observability"],
        difficulty=5,
    ),
    InterviewQuestion(
        category="学习总结",
        question="60 天学习中，你最深刻的 3 个知识点是什么？",
        key_points=["知识点 1", "知识点 2", "知识点 3", "实际应用"],
        difficulty=3,
    ),
    InterviewQuestion(
        category="职业规划",
        question="为什么选择 AI 方向？未来的职业规划是什么？",
        key_points=["动机", "短期目标", "长期目标", "持续学习"],
        difficulty=2,
    ),
    InterviewQuestion(
        category="薪资谈判",
        question="50W+ 岗位如何谈薪？你的期望薪资是多少？",
        key_points=["市场调研", "底线", "期望范围", "优势", "项目经验"],
        difficulty=3,
    ),
]


class MockInterview:
    """模拟面试"""

    def __init__(self, role: str = "ai-architect"):
        self.role = role
        self.answers: list[InterviewAnswer] = []

    def self_introduction(self) -> None:
        """自我介绍"""
        print("\n" + "=" * 60)
        print("📝 自我介绍（2 分钟）")
        print("=" * 60)
        print("请介绍：")
        print("1. 你的背景（如 10 年 Java 经验）")
        print("2. 学习成果（完成 Agent Journey 60D 全部课程）")
        print("3. 项目经验（企业级 Agent 平台 / 投研平台）")
        print("4. 你的优势（Java + AI 复合背景）")
        print("=" * 60)

    def technical_interview(self, num_questions: int = 5) -> None:
        """技术面试"""
        print("\n" + "=" * 60)
        print("🔧 技术面试")
        print("=" * 60)

        # 随机抽取题目
        questions = random.sample(TECH_QUESTIONS, num_questions)

        for i, q in enumerate(questions, 1):
            print(f"\n📌 问题 {i}/{num_questions}：{q.question}")
            print(f"   类别：{q.category} | 难度：{'⭐' * q.difficulty}")
            print(f"   关键点：{', '.join(q.key_points)}")
            print("-" * 40)

            # TODO: 获取用户输入的答案
            # answer = input("你的答案：")
            # 这里应该调用 AI 评分
            # score, feedback = self._evaluate_answer(q, answer)
            # self.answers.append(InterviewAnswer(q, answer, score, feedback))

    def general_interview(self, num_questions: int = 3) -> None:
        """综合面试"""
        print("\n" + "=" * 60)
        print("🎤 综合面试")
        print("=" * 60)

        questions = random.sample(GENERAL_QUESTIONS, num_questions)

        for i, q in enumerate(questions, 1):
            print(f"\n📌 问题 {i}/{num_questions}：{q.question}")
            print(f"   类别：{q.category}")
            print("-" * 40)

    def evaluate(self) -> dict:
        """评估面试结果

        Returns:
            评估结果
        """
        if not self.answers:
            return {"total_score": 0, "feedback": "未答题"}

        total_score = sum(a.score for a in self.answers) / len(self.answers)

        return {
            "total_score": total_score,
            "answers_count": len(self.answers),
            "feedback": self._generate_feedback(total_score),
        }

    def _generate_feedback(self, score: float) -> str:
        """生成反馈

        Args:
            score: 总分

        Returns:
            反馈
        """
        if score >= 90:
            return "优秀！你已具备 AI 架构师的能力。"
        elif score >= 75:
            return "良好！基础知识扎实，部分深度有待提升。"
        elif score >= 60:
            return "及格！需要加强某些模块的学习。"
        else:
            return "需要加强！建议重新复习相关模块。"

    def print_report(self) -> None:
        """打印面试报告"""
        result = self.evaluate()

        print("\n" + "=" * 60)
        print("📊 面试报告")
        print("=" * 60)
        print(f"角色：{self.role}")
        print(f"答题数：{result['answers_count']}")
        print(f"总分：{result['total_score']:.1f}")
        print(f"反馈：{result['feedback']}")
        print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="模拟面试")
    parser.add_argument("--role", type=str, default="ai-architect", help="面试角色")
    parser.add_argument("--tech-count", type=int, default=5, help="技术面试题数")
    parser.add_argument("--general-count", type=int, default=3, help="综合面试题数")
    args = parser.parse_args()

    interview = MockInterview(role=args.role)

    print("🎤 模拟面试开始")
    print(f"角色：{args.role}")

    # 自我介绍
    interview.self_introduction()

    # 技术面试
    interview.technical_interview(num_questions=args.tech_count)

    # 综合面试
    interview.general_interview(num_questions=args.general_count)

    # 打印报告
    interview.print_report()


if __name__ == "__main__":
    main()
