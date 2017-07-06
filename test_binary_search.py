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
