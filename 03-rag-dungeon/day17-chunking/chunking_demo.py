"""
Day 17: Chunking Demo.

演示文档分块策略。

Usage:
    python chunking_demo.py
"""


def fixed_size_chunking(text: str, chunk_size: int = 200, overlap: int = 20) -> list[str]:
    """固定大小分块。"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def recursive_chunking(text: str, chunk_size: int = 200, separators: list[str] = None) -> list[str]:
    """递归分块：按段落、句子、词逐级切分。"""
    if separators is None:
        separators = ["\n\n", "\n", ". ", " "]

    if len(text) <= chunk_size:
        return [text]

    # 尝试用每个分隔符切分
    for sep in separators:
        if sep in text:
            parts = text.split(sep)
            chunks = []
            for part in parts:
                if len(part) > chunk_size:
                    chunks.extend(recursive_chunking(part, chunk_size, separators[1:]))
                else:
                    chunks.append(part)
            return chunks

    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


def semantic_chunking(text: str, max_chunk_size: int = 300) -> list[str]:
    """语义分块：按语义边界切分（简化版）。"""
    # 按段落切分
    paragraphs = text.split("\n\n")

    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) > max_chunk_size and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = para
        else:
            current_chunk += "\n\n" + para if current_chunk else para

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def document_chunking(text: str) -> list[str]:
    """文档结构分块：按标题层级切分。"""
    import re

    # 按标题切分（Markdown 风格）
    pattern = r"(^#{1,3}\s+.+$)"
    parts = re.split(pattern, text, flags=re.MULTILINE)

    chunks = []
    current_title = ""
    current_content = ""

    for part in parts:
        if part.startswith("#"):
            if current_title:
                chunks.append(f"{current_title}\n{current_content.strip()}")
            current_title = part
            current_content = ""
        else:
            current_content += part

    if current_title:
        chunks.append(f"{current_title}\n{current_content.strip()}")

    return chunks


def chunking_demo():
    """分块演示。"""
    print("=" * 60)
    print("Chunking Demo")
    print("=" * 60)

    # 示例文档
    doc = """
# 第一章：贵州茅台

贵州茅台酒股份有限公司是中国白酒行业的龙头企业。公司成立于1999年，总部位于贵州省仁怀市茅台镇。

## 1.1 主营业务

茅台酒系列产品的生产与销售。主打产品包括飞天茅台、茅台1935等。

## 1.2 财务数据

2023年，公司实现营业收入1505亿元，同比增长18%。净利润747亿元，同比增长19%。

# 第二章：行业分析

中国白酒行业呈现高端化、品牌化趋势。茅台作为高端白酒龙头，具有强大的品牌壁垒。

## 2.1 竞争格局

白酒行业CR5持续提升，头部企业市场份额不断扩大。
    """.strip()

    print(f"\n📄 原始文档长度: {len(doc)} 字符")

    # Fixed Size
    print("\n--- Fixed Size (chunk_size=200) ---")
    chunks = fixed_size_chunking(doc, chunk_size=200, overlap=20)
    print(f"   分块数: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"   [{i}] {len(chunk)} 字符: {chunk[:50]}...")

    # Recursive
    print("\n--- Recursive ---")
    chunks = recursive_chunking(doc, chunk_size=200)
    print(f"   分块数: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"   [{i}] {len(chunk)} 字符: {chunk[:50]}...")

    # Semantic
    print("\n--- Semantic ---")
    chunks = semantic_chunking(doc, max_chunk_size=300)
    print(f"   分块数: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"   [{i}] {len(chunk)} 字符: {chunk[:50]}...")

    # Document
    print("\n--- Document Structure ---")
    chunks = document_chunking(doc)
    print(f"   分块数: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"   [{i}] {len(chunk)} 字符: {chunk[:50]}...")


if __name__ == "__main__":
    chunking_demo()
