import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a BOLD text node", TextType.BOLD)
        node2 = TextNode("This is a PLAIN text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a BOLD text node", TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)

        self.assertNotEqual(node, node2)

    def test_default_empty_URL(self):
        node = TextNode("This url is empty by default", TextType.LINK)

        self.assertEqual(node.url, None)

    def test_can_change_URL(self):
        node = TextNode("The URL will NOT equal None", TextType.LINK, "www.goesNoWhere.com")

        self.assertNotEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()