class Solution:
    calcs = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n not in self.calcs.keys():
            self.calcs[n] = self.fib(n-1) + self.fib(n-2)
        return self.calcs[n]