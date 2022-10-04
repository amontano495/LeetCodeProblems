class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        if len(a) < len(b):
            a = '0'*(len(b) - len(a)) + a
        if len(b) < len(a):
            b = '0'*(len(a) - len(b)) + b
        
        i = len(a) - 1
        c_bit = 0
        s_bit = 0
        while(i > -1):
            a_bit = int(a[i])
            b_bit = int(b[i])
            s_bit = a_bit ^ b_bit ^ c_bit
            c_bit = (a_bit and b_bit) or (c_bit and(a_bit ^ b_bit))
            ans = str(s_bit) + ans
            i -= 1
        if c_bit > 0:
            ans = str(c_bit) + ans
        return ans
            