""" tests for merge.py
"""
import unittest
from heapq import merge as hm
from merge import merge


class TestMerge(unittest.TestCase):
    """merge function tests"""

    def test_merge_integers_one(self):
        """example from task description"""
        actual = list(merge([1, 5, 9], [2, 5], [1, 6, 10, 11]))
        expected = list(hm([1, 5, 9], [2, 5], [1, 6, 10, 11]))
        self.assertEqual(actual, expected)

    def test_merge_integers_two(self):
        """example from: https://github.com/python/cpython/blob/main/Lib/heapq.py"""
        actual = list(merge([1, 3, 5, 7], [0, 2, 4, 8], [5, 10, 15, 20], [], [25]))
        expected = list(hm([1, 3, 5, 7], [0, 2, 4, 8], [5, 10, 15, 20], [], [25]))
        self.assertEqual(actual, expected)

    def test_merge_strings_one(self):
        """example from: https://github.com/sweeneyde/multimerge"""
        actual = list(merge(["dog", "horse"], ["cat", "fish", "kangaroo"], key=len))
        expected = list(hm(["dog", "horse"], ["cat", "fish", "kangaroo"], key=len))
        self.assertEqual(actual, expected)

    def test_merge_performance_one(self):
        """example from: https://github.com/sweeneyde/multimerge"""
        interleaved = [
            # (0,16,32,...), (1,17,33,...), (2,18,34,...), ...
            list(map(int, range(x, 16_000, 16)))
            for x in range(16)
        ]
        actual = list(merge(interleaved))
        expected = list(hm(interleaved))
        self.assertEqual(actual, expected)

    def test_merge_performance_two(self):
        """example from: https://github.com/sweeneyde/multimerge"""
        no_overlap = [
            # (0..999), (1_000..1_999), (2_000..2_999), ...
            list(map(int, range(x, x + 1_000)))
            for x in range(0, 16_000, 1_000)
        ]
        actual = list(merge(no_overlap))
        expected = list(hm(no_overlap))
        self.assertEqual(actual, expected)

    def test_merge_reverse(self):
        """example to test reverse function"""
        actual = list(merge([1], [2], [3], reverse=True))
        expected = list(hm([1], [2], [3], reverse=True))
        self.assertEqual(actual, expected)
