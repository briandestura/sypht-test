import argparse
import datetime


class InvalidInputException(Exception):
    pass


class Date:
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

        if not 1901 <= self.year <= 2999:
            raise InvalidInputException(f'Invalid year on date: {self.year}-{self.month}-{self.day}')
 
        if not 1 <= self.month <= 12:
            raise InvalidInputException(f'Invalid month on date: {self.year}-{self.month}-{self.day}')

        max_month_day = self.month_days[self.month] 
        if self.month == 2:
            max_month_day += 1 if Date.is_leap_year(self.year) else 0

        if not 1 <= self.day <= max_month_day:
            raise InvalidInputException(f'Invalid day on date: {self.year}-{self.month}-{self.day}')

    def _days_since_year(self):
        leap_years_since = len([i for i in range(0, self.year) if Date.is_leap_year(i)])
        return self.year * 365 + leap_years_since

    def _days_since_month(self):
        cumulative_days = sum(self.month_days[:self.month])
        cumulative_days += 1 if self.month > 2 and Date.is_leap_year(self.year) else 0
        return cumulative_days

    def total_days(self):
        return self._days_since_year() + self._days_since_month() + self.day

    def __sub__(self, other):
        return abs(self.total_days() - other.total_days()) - 1


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'd1', help='First date (Y-m-d format)', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    parser.add_argument(
        'd2', help='Second date (Y-m-d format)', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    return parser.parse_args()


def main(d1, d2):
    d1 = Date(d1.year, d1.month, d1.day)
    d2 = Date(d2.year, d2.month, d2.day)
    print(d1 - d2)
    return d1 - d2


if __name__ == '__main__':
    args = parse_arguments()
    main(args.d1, args.d2)
