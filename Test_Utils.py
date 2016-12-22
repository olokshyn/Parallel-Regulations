from unittest import TestCase

import Utils


class TestUtils(TestCase):
    def test_get_all_combinations(self):
        source = [1, 2, 3, 6, 7]
        result = Utils.get_all_combinations(source, 3)

        self.assertEqual(10, len(result))
        self.assertEqual([1, 2, 3], result[0])
        self.assertEqual([1, 2, 6], result[1])
        self.assertEqual([1, 2, 7], result[2])
        self.assertEqual([1, 3, 6], result[3])
        self.assertEqual([1, 3, 7], result[4])
        self.assertEqual([1, 6, 7], result[5])
        self.assertEqual([2, 3, 6], result[6])
        self.assertEqual([2, 3, 7], result[7])
        self.assertEqual([2, 6, 7], result[8])
        self.assertEqual([3, 6, 7], result[9])
