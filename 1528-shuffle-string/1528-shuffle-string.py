class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        j = 0
        s_arr = list(s)
        for i in indices:
            s_arr[i] = s[j]
            j+=1
        return ''.join(s_arr)