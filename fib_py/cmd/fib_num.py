import argparse

from fib_py.fib_calcs.fib_num import recurring_fibonacci_number

# trigger publish test


def fib_num() -> None:
    parser = argparse.ArgumentParser(description="Calculate Fibonacci numbers")
    parser.add_argument(
        "--number",
        action="store",
        type=int,
        required=True,
        help="Fibonacci number to be calculated",
    )
    args = parser.parse_args()
    print(
        f"Your Fibonacci number is: "
        f"{recurring_fibonacci_number(number=args.number)}"
    )
