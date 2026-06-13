import unittest
from BST import BinarySearchTree

class TestCases(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertEqual(bst.inorder(), [3, 5, 7])

    def test_search(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertTrue(bst.search(3))
        self.assertFalse(bst.search(4))

    def test_delete(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.delete(3)
        self.assertEqual(bst.inorder(), [5, 7])

    def test_preorder(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertEqual(bst.preorder(), [5, 3, 7])

    def test_postorder(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertEqual(bst.postorder(), [3, 7, 5])

    def test_levelorder(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertEqual(bst.levelorder(), [5, 3, 7])

if __name__ == '__main__':
    unittest.main()