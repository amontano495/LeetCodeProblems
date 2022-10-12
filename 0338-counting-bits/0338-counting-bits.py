class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = ['']*(n+1)
        for i in range(n+1):
            ans[i] = len(bin(i).replace('0','').replace('b',''))
        return ans