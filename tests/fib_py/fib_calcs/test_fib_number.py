from unicodedata import name
from unittest import main, TestCase

from fib_py.fib_calcs.fib_num import recurring_fibonacci_number


class RecurringFibNumberTest(TestCase):
    def test_zero(self):
        self.assertEqual(0, recurring_fibonacci_number(0))

    def test_negative(self):
        with self.assertRaises(ValueError) as raised_error:
            self.assertEqual(
                str(raised_error),
                str(recurring_fibonacci_number(-1)),
            )

    def test_one(self):
        self.assertEqual(1, recurring_fibonacci_number(1))

    def test_two(self):
        self.assertEqual(1, recurring_fibonacci_number(2))

    def test_twenty(self):
        self.assertEqual(6765, recurring_fibonacci_number(20))


if name == "__main__":
    main()
