import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq_tag(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p")
        self.assertEqual(node, node2)

    def test_eq_value(self):
        node = HTMLNode(value="Some Text")
        node2 = HTMLNode(value="Some Text")
        self.assertEqual(node, node2)

    def test_eq_children(self):
        child_node = HTMLNode()
        node = HTMLNode(children=[child_node])
        node2 = HTMLNode(children=[child_node])
        self.assertEqual(node, node2)
        
    def test_eq_props(self):
        child_node = HTMLNode()
        node = HTMLNode(props={"href": "www.doesItWork.org"})
        node2 = HTMLNode(props={"href": "www.doesItWork.org"})
        self.assertEqual(node, node2)

    def test_not_eq_tag(self):
        node = HTMLNode("p")
        node2 = HTMLNode("b")
        self.assertNotEqual(node, node2)

    def test_not_eq_value(self):
        node = HTMLNode(value="Some Text")
        node2 = HTMLNode(value="Some OTHER Text")
        self.assertNotEqual(node, node2)

    def test_not_eq_children(self):
        child_node = HTMLNode()
        node = HTMLNode(children=[child_node])
        node2 = HTMLNode(children=[child_node, child_node, child_node])
        self.assertNotEqual(node, node2)
        
    def test_not_eq_props(self):
        child_node = HTMLNode()
        node = HTMLNode(props={"href": "www.doesItWork.org"})
        node2 = HTMLNode(props={"href": "www.hopeItDoes.edu"})
        self.assertNotEqual(node, node2)
    
    def test_outputs(self):
        child_node = [HTMLNode(value="Outputs lsit of other htmlNodes")]
        output_check = HTMLNode("tag", "Outputs the text", child_node, {"href": "www.doesItWork.org"})
        print(output_check)
    
    # Tests involving the leaf nodes
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafnode_raw_text(self):
        node = LeafNode(None, "Regular Text")
        self.assertEqual(node.to_html(), "Regular Text")

    def test_leafNode_attributes(self):
        node = LeafNode("a", "Click Here", {"href": "www.success.com"})
        self.assertEqual(node.to_html(), "<a href=\"www.success.com\">Click Here</a>")

    # Tests involving the Parent Node
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()