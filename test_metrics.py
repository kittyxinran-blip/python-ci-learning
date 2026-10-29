import unittest
from metrics import conversion_rate


class ConversionRateTests(unittest.TestCase):
    def test_normal_conversion(self):
        self.assertEqual(conversion_rate(200, 10), 5.0)

    def test_rounding(self):
        self.assertEqual(conversion_rate(3, 1), 33.33)

    def test_no_traffic(self):
        self.assertEqual(conversion_rate(0, 0), 0.0)

    def test_no_purchases(self):
        self.assertEqual(conversion_rate(100, 0), 0.0)

    def test_all_convert(self):
        self.assertEqual(conversion_rate(10, 10), 100.0)

    def test_invalid_counts(self):
        for visitors, purchases in [(-1, 0), (10, -1), (10, 11), (0, 1)]:
            with self.subTest(visitors=visitors, purchases=purchases):
                with self.assertRaises(ValueError):
                    conversion_rate(visitors, purchases)

    def test_invalid_types(self):
        for visitors, purchases in [(10.5, 1), (10, '1'), (True, 1)]:
            with self.subTest(visitors=visitors, purchases=purchases):
                with self.assertRaises(TypeError):
                    conversion_rate(visitors, purchases)


if __name__ == '__main__':
    unittest.main()
