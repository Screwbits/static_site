from enum import Enum
from inline_markdown import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODING = "coding"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown: str) -> list[str]:
    markdown_blocks = markdown.split("\n\n")

    for i in range(0, len(markdown_blocks)):
        markdown_blocks[i] = markdown_blocks[i].strip()
        markdown_blocks[i] = markdown_blocks[i].replace("\n        ", "\n")

    markdown_blocks = [block for block in markdown_blocks if block != "" and block != "\n"]

    return markdown_blocks

def block_to_block_type(markdown_block: str) -> BlockType:
    lines = markdown_block.split("\n")

    if markdown_block.startswith(("# ","## ", "### ", "#### ", "##### " "###### ")):
        return BlockType.HEADING

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODING
    
    if markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if markdown_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST
    
    if markdown_block.startswith("1. "):
        counter = 1
        for line in lines:
            if not line.startswith(f"{counter}. "):
                return BlockType.PARAGRAPH
            counter += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH




if __name__ == "__main__":
    unittest.main()