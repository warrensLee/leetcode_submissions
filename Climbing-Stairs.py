from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        # C(n-k,k) sum over all values of k, for choosing 1 steps or 2 steps
        # utilizes basic discrete mathematics and combinatorics methods 
        return sum(comb(n - k, k) for k in range(n // 2 + 1)) 
