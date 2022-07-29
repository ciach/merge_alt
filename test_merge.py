import unittest
from merge import merge
from heapq import merge as hm


class TestMerge(unittest.TestCase):
    def test_merge_integers_one(self):
        actual = merge([1, 5, 9], [2, 5], [1, 6, 10, 11])
        expected = list(hm([1, 5, 9], [2, 5], [1, 6, 10, 11]))
        self.assertEqual(actual, expected)

    def test_merge_integers_two(self):
        actual = merge([1, 3, 5, 7], [0, 2, 4, 8], [5, 10, 15, 20], [], [25])
        expected = list(hm([1, 3, 5, 7], [0, 2, 4, 8], [5, 10, 15, 20], [], [25]))
        self.assertEqual(actual, expected)

    def test_merge_strings_one(self):
        actual = merge(["dog", "horse"], ["cat", "fish", "kangaroo"], key=len)
        expected = list(hm(["dog", "horse"], ["cat", "fish", "kangaroo"], key=len))
        self.assertEqual(actual, expected)
