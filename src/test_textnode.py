import unittest
from textnode import TextNode, TextType, text_node_to_html_node


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

    # This is for the conversion of Text Nodes to htmlNodes
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_with_tag(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_text_with_link(self):
        node = TextNode("click this", TextType.LINK, "www.loveit.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "click this")
        self.assertEqual(html_node.props, {"href": "www.loveit.com"})

    def test_text_with_image(self):
        node = TextNode("This is the alt text", TextType.IMAGE, "www.loveit.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.loveit.com", "alt": "This is the alt text"})

if __name__ == "__main__":
    unittest.main()