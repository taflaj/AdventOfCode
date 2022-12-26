# day08_test.py

import day08, unittest

class TestPart1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day08.part1(['30373', '25512', '65332', '33549', '35390'], 5, 5), 21)
        self.assertEqual(day08.part1(['30373', '65512', '65332', '73549', '35390'], 5, 5), 21)

    def test_part2(self):
        self.assertEqual(day08.part2(['30373', '25512', '65332', '33549', '35390'], 5, 5), 8)