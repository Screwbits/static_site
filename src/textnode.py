from enum import Enum

class TextType(Enum):
    TEXT = "text (plain)"
    BOLD = "**Bold Text**"
    ITALIC = "_Italic Text_"
    CODE = "`Code Text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        # 1st - always check if both obects are the same
        if not isinstance(other, TextNode):
            return False

        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
            