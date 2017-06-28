import PerfectNumber
import unittest

class TestPerfectNumber(unittest.TestCase):
    def test_is_perfect_1(self):
        self.assertEqual(PerfectNumber.is_perfect(6), True)
    def test_is_perfect_2(self):
        self.assertEqual(PerfectNumber.is_perfect(28), True)
    def test_is_perfect_3(self):
        self.assertEqual(PerfectNumber.is_perfect(10), False)

if __name__ == '__main__':
    unittest.main()
