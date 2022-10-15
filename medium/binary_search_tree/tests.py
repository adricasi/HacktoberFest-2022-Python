import unittest
import utility
import solution

class Test(unittest.TestCase):
    "Binary Search Tree Test"
    def test_binary_search_tree_test_a(self):
        "Normal Test 1"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search(4), True, "Test 1 Failed")

    def test_binary_search_tree_test_b(self):
        "Normal Test 2"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search(15), True, "Test 2 Failed")

    def test_binary_search_tree_test_c(self):
        "Normal Test 3"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search(0), True, "Test 3 Failed")

    def test_binary_search_tree_test_d(self):
        "Normal Test 4"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search(3), False, "Test 4 Failed")

    def test_binary_search_tree_test_e(self):
        "Normal Test 5"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search(30), False, "Test 5 Failed")

    def test_binary_search_tree_test_e(self):
        "Normal Test 6"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search(-4), False, "Test 6 Failed")

    def test_binary_search_tree_test_i(self):
        "Exception Test 1"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search(), -1, "Test 7 Failed")

    def test_binary_search_tree_test_k(self):
        "Exception Test 2"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search("a"), -1, "Test 8 Failed")

    def test_binary_search_tree_test_l(self):
        "Exception Test 3"
        tree = solution.binary_search_tree()
        tree.insert_list([8,2,4,1,10,0,15])
        self.assertEqual(tree.search(1.5), -1, "Test 9 Failed")


if __name__ == "__main__":
    utility.main()