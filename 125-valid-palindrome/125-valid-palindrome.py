class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([c for c in s if c.isalpha() or c.isnumeric()])
        i = 0
        j = len(s) - 1
        if len(s) == 1 or len(s) == 0:
            return True
        while(i < j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True