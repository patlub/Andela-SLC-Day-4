import unittest

from binary_search import BinarySearch


class BinarySearchTest(unittest.TestCase):
    """Get the index of the item with an expected number of loops in\
     array [1, 2 . . . 20]
       Returns a dictionary containing {count: value, index: value}
    """

    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)

    def test_small_list(self):
        search = self.one_to_twenty.search(16)
        self.assertGreater(
            5,
            search['count'],
            msg='should return {count: 4, index: 15} for 16'
        )
        self.assertEqual(
            15,
            search['index'],
            msg='should return {count: 4, index: 15} for 16'
        )

    def test_medium_list_search(self):
        search1 = self.two_to_forty.search(16)
        search2 = self.two_to_forty.search(40)
        search3 = self.two_to_forty.search(33)
        self.assertGreater(
            5,
            search1['count'],
            msg='should return {count: 4, index: 7} for 16'
        )
        self.assertEqual(
            7,
            search1['index'],
            msg='should return {count: 4, index: 7} for 16'
        )
        self.assertEqual(
            0,
            search2['count'],
            msg='should return {count: 0, index: 19} for 40'
        )
        self.assertEqual(
            19,
            search2['index'],
            msg='should return {count: 5, index: 19} for 40'
        )

        self.assertGreater(
            4,
            search3['count'],
            msg='should return {count: 3, index: -1} for 33'
        )
        self.assertEqual(
            -1,
            search3['index'],
            msg='should return {count: 3, index: -1} for 33'
        )
