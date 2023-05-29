def calculate_close(x):
    if 0 <= x <= 50:
        return (-x / 50) + 1
    return 0


def calculate_moderate(x):
    if 40 <= x <= 50:
        return (x / 10) - 4
    if 50 <= x <= 100:
        return (-x / 50) + 2
    return 0


def calculate_far(x):
    if 90 <= x <= 200:
        return (x / 110) - (9 / 11)
    if x >= 200:
        return 1
    return 0


def calculate_low_speed(x):
    if 0 <= x <= 5:
        return x / 5
    if 5 <= x <= 10:
        return (-x / 5) + 2
    return 0


def calculate_medium_speed(x):
    if 0 <= x <= 15:
        return x / 15
    if 15 <= x <= 30:
        return (-x / 15) + 2
    return 0


def calculate_high_speed(x):
    if 25 <= x <= 30:
        return (x / 5) - 5
    if 30 <= x <= 90:
        return (-x / 60) + (3 / 2)
    return 0


class FuzzyGasController:

    def __init__(self):
        self.high = 0
        self.medium = 0
        self.low = 0

    def max_min(self, x):
        return max(min(self.low, calculate_low_speed(x)),
                   min(self.high, calculate_high_speed(x)),
                   min(self.medium, calculate_medium_speed(x)))

    def integral(self, start, limit, interval):
        x = start
        num = 0
        den = 0
        while x < limit:
            den += self.max_min(x) * interval
            num += self.max_min(x) * interval * x
            x += interval
        if den != 0:
            return float(num) / float(den)
        return 0

    def decide(self, center_dist):

        self.low = calculate_close(center_dist)
        self.medium = calculate_moderate(center_dist)
        self.high = calculate_far(center_dist)

        return self.integral(0, 90, 0.01)


