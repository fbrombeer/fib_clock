import datetime as dt

class FibClock:
    def __init__(self, datetime: dt.datetime) -> None:
        self.datetime = datetime

    @staticmethod
    def decimal_to_fibonacci(decimal: int) -> list:
        fib_seq = (1, 1, 2, 3, 5)
        fibonacci_numbers = fib_seq
        decomposition = []
        remainder = decimal

        for num in reversed(fibonacci_numbers):
            if num <= remainder:
                decomposition.append(num)
                remainder -= num
        return decomposition

    @staticmethod
    def time_to_fibonacci(datetime: dt.datetime) -> tuple[tuple, tuple]:
        hour = datetime.hour
        if hour > 12:
            hour -= 12

        minute = datetime.minute
        minute = minute // 5

        return FibClock.decimal_to_fibonacci(hour), FibClock.decimal_to_fibonacci(minute)

    @staticmethod
    def arange_fields(hours: list, minutes: list) -> tuple:
        red = [] # hours
        green = [] # minutes
        blue = [] # both

        red = list(hours)
        green = list(minutes)
        
        for fib_number in red:
            if fib_number in green:
                blue.append(fib_number)
        
        for fib_number in blue:
            red.remove(fib_number)
            green.remove(fib_number)

        return red, green, blue


    def __str__(self) -> str:
        hour, minute = FibClock.time_to_fibonacci(self.datetime)
        red, green, blue = FibClock.arange_fields(hour, minute)

        return f"R {' '.join(str(x) for x in red)} | G {' '.join(str(x) for x in green)} | B {' '.join(str(x) for x in blue)}"
    

if __name__ == "__main__":
    import time
    while True:
        print(FibClock(dt.datetime.now()))
        time.sleep(300)