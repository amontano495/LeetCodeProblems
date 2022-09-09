class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        k = 1
        coins = n
        finished_rows = 0
        while True:
            coins -= k
            if coins >= 0:
                k += 1
                finished_rows += 1
            else:
                break
            
        return finished_rows