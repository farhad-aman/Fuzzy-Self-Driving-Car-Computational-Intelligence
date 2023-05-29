def calculate_close_L(x):
    if 0 <= x <= 50:
        return 1 - (x / 50)
    return 0


def calculate_close_R(x):
    if 0 <= x <= 50:
        return 1 - (x / 50)
    return 0


def calculate_far_L(x):
    if 100 >= x >= 50:
        return (x / 50) - 1
    return 0


def calculate_far_R(x):
    if 100 >= x >= 50:
        return (x / 50) - 1
    return 0


def calculate_moderate_L(x):
    if 35 <= x <= 50:
        return (x / 15) - (7 / 3)
    elif 65 >= x >= 50:
        return (13 / 3) - (x / 15)
    return 0


def calculate_moderate_R(x):
    if 35 <= x <= 50:
        return (x / 15) - (7 / 3)
    elif 65 >= x >= 50:
        return (13 / 3) - (x / 15)
    return 0


def calculate_high_left(x):
    if 20 <= x <= 50:
        return (-x / 30) + (5 / 3)
    if 20 >= x >= 5:
        return (-1 / 3) + (x / 15)
    return 0


def calculate_high_right(x):
    if -50 <= x <= -20:
        return (x / 30) + (5 / 3)
    if -20 <= x <= -5:
        return (-1 / 3) - (x / 15)
    return 0


def calculate_low_left(x):
    if 10 <= x <= 20:
        return (-x / 10) + 2
    if 10 >= x >= 0:
        return x / 10
    return 0


def calculate_low_right(x):
    if -10 >= x >= -20:
        return (x / 10) + 2
    if -10 <= x <= 0:
        return -x / 10
    return 0


def calculate_nothing(x):
    if -10 <= x <= 0:
        return (x / 10) + 1
    if 10 >= x >= 0:
        return 1 - (x / 10)
    return 0


class FuzzyController:

    def __init__(self):
        self.nothing = 0
        self.high_right = 0
        self.high_left = 0
        self.low_right = 0
        self.low_left = 0

    def max_min(self, x):
        return max(min(self.low_right, calculate_low_right(x)),
                   min(self.high_right, calculate_high_right(x)),
                   min(self.low_left, calculate_low_left(x)),
                   min(self.high_left, calculate_high_left(x)),
                   min(self.nothing, calculate_nothing(x)))

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

    def decide(self, left_dist, right_dist):

        self.low_left = min(calculate_moderate_L(left_dist), calculate_close_R(right_dist))
        self.low_right = min(calculate_close_L(left_dist), calculate_moderate_R(right_dist))
        self.high_left = min(calculate_far_L(left_dist), calculate_close_R(right_dist))
        self.high_right = min(calculate_close_L(left_dist), calculate_far_R(right_dist))
        self.nothing = min(calculate_moderate_L(left_dist), calculate_moderate_R(right_dist))

        return self.integral(-50, 50, 0.1)
