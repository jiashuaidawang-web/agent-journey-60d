"""
Day 61: LoRA/QLoRA 微调实战 - 数据准备

本文件演示微调数据的获取和清洗流程：
- 加载开源数据集（Alpaca）
- 数据清洗（去重、去噪、长度过滤）
- 格式统一
- 保存处理后的数据

数据格式：
{
    "instruction": "翻译成英文",
    "input": "你好世界",
    "output": "Hello World"
}
"""

import json
import random
from typing import List, Dict
from collections import Counter


# === 模拟数据集 ===

def generate_mock_alpaca_data(num_samples: int = 1000) -> List[Dict]:
    """生成模拟 Alpaca 数据集"""
    instructions = [
        "翻译成英文",
        "翻译成中文",
        "总结以下内容",
        "回答问题",
        "写一首诗",
        "解释概念",
        "列出步骤",
        "提供建议",
    ]
    data = []
    for i in range(num_samples):
        instruction = random.choice(instructions)
        data.append({
            "id": i,
            "instruction": instruction,
            "input": f"示例输入 {i}",
            "output": f"示例输出 {i}"
        })
    return data


# === 数据清洗 ===

class DataCleaner:
    """
    数据清洗器
    - 去重
    - 去噪
    - 长度过滤
    - 格式统一
    """

    def __init__(self, min_length: int = 10, max_length: int = 2048):
        self.min_length = min_length
        self.max_length = max_length

    def deduplicate(self, data: List[Dict]) -> List[Dict]:
        """去重：基于 instruction + input"""
        seen = set()
        unique_data = []
        for item in data:
            key = f"{item['instruction']}_{item['input']}"
            if key not in seen:
                seen.add(key)
                unique_data.append(item)
        return unique_data

    def remove_noise(self, data: List[Dict]) -> List[Dict]:
        """去噪：删除低质量样本"""
        clean_data = []
        noise_patterns = ["http://", "https://", "广告", "推广", "点击领取"]
        for item in data:
            text = f"{item['instruction']} {item['input']} {item['output']}"
            # 检查是否包含噪声模式
            if any(pattern in text for pattern in noise_patterns):
                continue
            # 检查是否为空
            if not item['instruction'] or not item['output']:
                continue
            clean_data.append(item)
        return clean_data

    def filter_by_length(self, data: List[Dict]) -> List[Dict]:
        """长度过滤"""
        filtered_data = []
        for item in data:
            total_length = len(item['instruction']) + len(item['input']) + len(item['output'])
            if self.min_length <= total_length <= self.max_length:
                filtered_data.append(item)
        return filtered_data

    def unify_format(self, data: List[Dict]) -> List[Dict]:
        """格式统一"""
        unified_data = []
        for item in data:
            unified_data.append({
                "instruction": str(item['instruction']).strip(),
                "input": str(item.get('input', '')).strip(),
                "output": str(item['output']).strip()
            })
        return unified_data

    def clean(self, data: List[Dict]) -> List[Dict]:
        """完整清洗流程"""
        print(f"   📦 原始数据: {len(data)} 条")

        # 去重
        data = self.deduplicate(data)
        print(f"   🧹 去重后: {len(data)} 条")

        # 去噪
        data = self.remove_noise(data)
        print(f"   🧹 去噪后: {len(data)} 条")

        # 长度过滤
        data = self.filter_by_length(data)
        print(f"   🧹 长度过滤后: {len(data)} 条")

        # 格式统一
        data = self.unify_format(data)
        print(f"   🧹 格式统一后: {len(data)} 条")

        return data


# === 主函数 ===

def main():
    """
    主函数：演示数据准备流程

    运行方式：
        python 01_data_preparation.py

    预期输出：
        📦 加载数据集: 1000 条
        🧹 去重后: 950 条
        🧹 去噪后: 940 条
        🧹 长度过滤后: 940 条
        💾 保存到: processed_data.json
    """
    print("=" * 60)
    print("📦 数据准备演示")
    print("=" * 60)
    print()

    # 生成模拟数据
    print("📦 加载数据集：")
    raw_data = generate_mock_alpaca_data(1000)
    print(f"   加载完成: {len(raw_data)} 条")
    print()

    # 添加一些重复和噪声数据（模拟真实场景）
    print("🔧 添加模拟噪声数据：")
    # 添加重复
    raw_data.extend(raw_data[:50])
    # 添加噪声
    for i in range(20):
        raw_data.append({
            "id": len(raw_data),
            "instruction": "点击领取优惠",
            "input": "http://spam.com",
            "output": "广告内容"
        })
    print(f"   添加后总数: {len(raw_data)} 条")
    print()

    # 数据清洗
    print("🧹 数据清洗：")
    cleaner = DataCleaner(min_length=10, max_length=2048)
    clean_data = cleaner.clean(raw_data)
    print()

    # 数据统计
    print("📊 数据统计：")
    instruction_counter = Counter([item['instruction'] for item in clean_data])
    print(f"   指令类型分布：")
    for instruction, count in instruction_counter.most_common(5):
        print(f"   - {instruction}: {count} 条")
    print()

    # 保存数据
    print("💾 保存处理后的数据：")
    output_file = "processed_data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(clean_data[:10], f, ensure_ascii=False, indent=2)  # 只保存前 10 条作为示例
    print(f"   已保存到: {output_file}（示例 10 条）")
    print()

    print("✅ 数据准备演示完成")
    print()
    print("注意：这是一个占位文件，使用模拟数据演示")
    print("实际运行时需要加载真实数据集（如 Alpaca）")


if __name__ == "__main__":
    main()
