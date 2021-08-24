import unittest
import datetime

from date_calculator import Date, InvalidInputException


class TestDate(unittest.TestCase):
    def test_data_default(self):
        self.assertEqual(
            Date(1983, 6, 22) - Date(1983, 6, 2),
            (datetime.date(1983, 6, 22) - datetime.date(1983, 6, 2)).days - 1
        )
        self.assertEqual(
            Date(1984, 12, 25) - Date(1984, 7, 4),
            (datetime.date(1984, 12, 25) - datetime.date(1984, 7, 4)).days - 1
        )
        self.assertEqual(
            Date(1989, 1, 3) - Date(1983, 8, 3),
            (datetime.date(1989, 1, 3) - datetime.date(1983, 8, 3)).days - 1
        )

    def test_invalid_inputs_raises(self):
        with self.assertRaises(InvalidInputException) as e:
            Date(1000, 1, 1)
        self.assertEqual(str(e.exception), 'Invalid year')

        with self.assertRaises(InvalidInputException) as e:
            Date(1901, 13, 1)
        self.assertEqual(str(e.exception), 'Invalid month')

        with self.assertRaises(InvalidInputException) as e:
            Date(1901, 2, 31)
        self.assertEqual(str(e.exception), 'Invalid day')

        # should not raise
        Date(2000, 2, 29)

        with self.assertRaises(InvalidInputException) as e:
            Date(2000, 2, 30)
        self.assertEqual(str(e.exception), 'Invalid day')

    def test_swap_dates_return_same_results(self):
        self.assertEqual(
            Date(2000, 6, 1) - Date(2000, 1, 6),
            (datetime.date(2000, 6, 1) - datetime.date(2000, 1, 6)).days - 1
        )

        self.assertEqual(
            Date(2000, 1, 6) - Date(2000, 6, 1),
            (datetime.date(2000, 6, 1) - datetime.date(2000, 1, 6)).days - 1
        )

    def test_days_since_year_returns_valid(self):
        self.assertEqual(Date(2000, 1, 1)._days_since_year(), 730485)

    def test_days_since_month_returns_valid(self):
        self.assertEqual(Date(2000, 3, 1)._days_since_month(), 60)


if __name__ == '__main__':
    unittest.main()
