"""
Day 60: Memory 深度体系 - PII 脱敏

本文件演示记忆中的 PII（个人可识别信息）脱敏。
PII 包括：姓名、电话、邮箱、身份证号、银行卡号等。

脱敏策略：
- 替换：将 PII 替换为占位符
- 掩码：部分字符用 * 替换
- 加密：敏感字段加密存储
- 删除：不存储 PII
"""

import re
from typing import Dict, List, Tuple


# === PII 脱敏器 ===

class PIIDesensitizer:
    """
    PII 脱敏器
    - 支持手机号、邮箱、身份证号、银行卡号脱敏
    - 支持自定义脱敏规则
    """

    def __init__(self):
        # 定义 PII 正则规则
        self.patterns: Dict[str, Tuple[str, str]] = {
            # 手机号：13812345678 → 138****5678
            "phone": (r'(?<!\d)(1[3-9]\d{9})(?!\d)', r'\1****\2'),
            # 邮箱：test@example.com → t***@example.com
            "email": (r'([a-zA-Z0-9._%+-]+)(@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', r'\1***\2'),
            # 身份证号：110101199001011234 → 110101********1234
            "id_card": (r'(?<!\d)(\d{6})(\d{8})(\d{4})(?!\d)', r'\1********\3'),
            # 银行卡号：6222021234567890 → 6222 **** **** 7890
            "bank_card": (r'(?<!\d)(\d{4})(\d{8,})(\d{4})(?!\d)', r'\1 **** **** \3'),
        }

        # 编译正则
        self.compiled_patterns = {
            name: re.compile(pattern)
            for name, (pattern, _) in self.patterns.items()
        }

    def desensitize(self, text: str) -> str:
        """
        对文本进行 PII 脱敏

        Args:
            text: 原始文本

        Returns:
            脱敏后的文本
        """
        result = text
        for name, pattern in self.compiled_patterns.items():
            if name == "phone":
                result = pattern.sub(self._mask_phone, result)
            elif name == "email":
                result = pattern.sub(self._mask_email, result)
            elif name == "id_card":
                result = pattern.sub(self._mask_id_card, result)
            elif name == "bank_card":
                result = pattern.sub(self._mask_bank_card, result)
        return result

    def _mask_phone(self, match) -> str:
        """手机号脱敏：13812345678 → 138****5678"""
        phone = match.group(0)
        return f"{phone[:3]}****{phone[7:]}"

    def _mask_email(self, match) -> str:
        """邮箱脱敏：test@example.com → t***@example.com"""
        email = match.group(0)
        local, domain = email.split("@", 1)
        return f"{local[0]}***@{domain}"

    def _mask_id_card(self, match) -> str:
        """身份证号脱敏：110101199001011234 → 110101********1234"""
        id_card = match.group(0)
        return f"{id_card[:6]}********{id_card[-4:]}"

    def _mask_bank_card(self, match) -> str:
        """银行卡号脱敏：6222021234567890 → 6222 **** **** 7890"""
        card = match.group(0)
        return f"{card[:4]} **** **** {card[-4:]}"

    def detect_pii(self, text: str) -> List[Dict[str, str]]:
        """
        检测文本中的 PII

        Args:
            text: 原始文本

        Returns:
            PII 列表，包含类型和位置
        """
        findings = []
        for name, pattern in self.compiled_patterns.items():
            for match in pattern.finditer(text):
                findings.append({
                    "type": name,
                    "value": match.group(0),
                    "start": match.start(),
                    "end": match.end()
                })
        return findings


# === 主函数 ===

def main():
    """
    主函数：演示 PII 脱敏

    运行方式：
        python 03_pii_desensitization.py

    预期输出：
        🔍 检测到 PII: 13812345678
        🔒 脱敏后: 138****5678
        🔍 检测到 PII: test@example.com
        🔒 脱敏后: t***@example.com
    """
    print("=" * 60)
    print("🔒 PII 脱敏演示")
    print("=" * 60)
    print()

    # 创建脱敏器
    desensitizer = PIIDesensitizer()

    # 测试用例
    test_cases = [
        "我的手机号是 13812345678，请联系我们",
        "邮箱地址是 zhangsan@example.com",
        "身份证号：110101199001011234",
        "银行卡号：6222021234567890",
        "联系人：张三，电话：13987654321，邮箱：zhangsan@gmail.com",
    ]

    print("🔍 PII 检测与脱敏：")
    print()

    for text in test_cases:
        print(f"   原文: {text}")

        # 检测 PII
        findings = desensitizer.detect_pii(text)
        for finding in findings:
            print(f"   🔍 检测到 PII: {finding['value']}（类型: {finding['type']}）")

        # 脱敏
        desensitized = desensitizer.desensitize(text)
        print(f"   🔒 脱敏后: {desensitized}")
        print()

    # 完整对话脱敏示例
    print("=" * 60)
    print("💬 完整对话脱敏示例：")
    print("=" * 60)
    print()

    conversation = [
        ("user", "你好，我是张三，手机号 13812345678"),
        ("assistant", "你好张三！请问有什么可以帮你？"),
        ("user", "我想查询我的订单，邮箱是 zhangsan@example.com"),
        ("assistant", "好的，请提供订单号"),
    ]

    print("   脱敏前：")
    for role, content in conversation:
        print(f"   [{role}] {content}")
    print()

    print("   脱敏后：")
    for role, content in conversation:
        desensitized = desensitizer.desensitize(content)
        print(f"   [{role}] {desensitized}")
    print()

    print("✅ PII 脱敏演示完成")


if __name__ == "__main__":
    main()
