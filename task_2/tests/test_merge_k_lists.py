import unittest
from task_2.src.merge_k_lists import merge_k_lists


class MergeKListsTest(unittest.TestCase):
    def test_merge_k_lists(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        result = merge_k_lists(lists)
        self.assertEqual(result, expected)

    def test_empty_lists(self):
        lists = []
        expected = []
        result = merge_k_lists(lists)
        self.assertEqual(result, expected)

    def test_single_list(self):
        lists = [[1, 2, 3]]
        expected = [1, 2, 3]
        result = merge_k_lists(lists)
        self.assertEqual(result, expected)

    def test_lists_with_empty(self):
        lists = [[], [1, 2], []]
        expected = [1, 2]
        result = merge_k_lists(lists)
        self.assertEqual(result, expected)
