class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        else:
            result = self.myPow(x, n//2)
            result = result * result
            return result if n % 2 == 0 else result * x
