from FibClock import FibClock
from datetime import datetime as dt


def test_decimal_to_fibonacci():
    assert FibClock.decimal_to_fibonacci(0) == []
    assert FibClock.decimal_to_fibonacci(1) == [1]
    assert FibClock.decimal_to_fibonacci(2) == [2]
    assert FibClock.decimal_to_fibonacci(3) == [3]
    assert FibClock.decimal_to_fibonacci(4) == [3, 1]
    assert FibClock.decimal_to_fibonacci(5) == [5]
    assert FibClock.decimal_to_fibonacci(6) == [5, 1]
    assert FibClock.decimal_to_fibonacci(7) == [5, 2]
    assert FibClock.decimal_to_fibonacci(8) == [5, 3]
    assert FibClock.decimal_to_fibonacci(9) == [5, 3, 1]
    assert FibClock.decimal_to_fibonacci(10) == [5, 3, 2]
    assert FibClock.decimal_to_fibonacci(11) == [5, 3, 2, 1]


def test_time_to_fibonacci():
    assert FibClock.time_to_fibonacci(dt.fromisoformat('2024-01-01T00:00')) == ([], [])


def test_arange_fields():
    assert FibClock.arange_fields([5, 3, 2], [5, 3]) == ([2], [], [5, 3])

def test_fibonacci_clock():
    assert str(FibClock(dt.fromisoformat('2024-01-01T10:40'))) == "R 3 2 | G 3 | B 5"


# Run the tests
test_decimal_to_fibonacci()
test_time_to_fibonacci()
test_arange_fields()
test_fibonacci_clock()