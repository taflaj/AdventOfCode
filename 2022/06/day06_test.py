# day06_test.py

import day06, unittest

class TestPart1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day06.part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4), 7)
        self.assertEqual(day06.part1('bvwbjplbgvbhsrlpgdmjqwftvncz', 4), 5)
        self.assertEqual(day06.part1('nppdvjthqldpwncqszvftbrmjlhg', 4), 6)
        self.assertEqual(day06.part1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4), 10)
        self.assertEqual(day06.part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4), 11)

    def test_part2(self):
        self.assertEqual(day06.part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14), 19)
        self.assertEqual(day06.part1('bvwbjplbgvbhsrlpgdmjqwftvncz', 14), 23)
        self.assertEqual(day06.part1('nppdvjthqldpwncqszvftbrmjlhg', 14), 23)
        self.assertEqual(day06.part1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14), 29)
        self.assertEqual(day06.part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14), 26)