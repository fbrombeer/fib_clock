from FibClock import FibClock

class FibClockGraphical(FibClock):
    COORDINATES = {
        1: (
            ((3, 5), (3, 5)), # upper
            ((3, 4), (3, 4))  # lower
        ),
        2: ((1, 4), (2, 5)),
        3: ((1, 1), (3, 3)),
        5: ((4, 1), (8, 5))
    }
    def clock_to_pixels(red: list, green: list, blue: list) -> str:
        pass


    def is_in_rectangle(point: tuple, rect: tuple) -> bool:
        pass