import unittest
from merge import merge
from heapq import merge as hm


class TestMerge(unittest.TestCase):
    def test_merge_one(self):
        actual = merge([1, 5, 9], [2, 5], [1, 6, 10, 11])
        expected = list(hm([1, 5, 9], [2, 5], [1, 6, 10, 11]))
        self.assertEqual(actual, expected)
