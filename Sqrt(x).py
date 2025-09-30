import math

class Solution:
    # I will implement the Newton-Raphson method of square root aproximation
    # start with an initial guess r, and repeatedly refine it using the formula r = (r + n/r) / 2
    def mySqrt(self, x: int) -> int:
        r = 2
        if x == 0:
            return 0
        for i in range(100):
            r = (r + x / r) / 2

        return int(math.floor(r))
        