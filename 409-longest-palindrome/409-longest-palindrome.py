class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashTab = {}
        
        for c in s:
            if c not in hashTab.keys():
                hashTab[c] = 1
            else:
                hashTab[c] += 1
                
        oddVal = 0
        palLen = 0
        
        for k,v in hashTab.items():
            if v % 2 == 0:
                palLen += v
            else:
                palLen += v - 1
                oddVal = 1
                
        return palLen + oddVal