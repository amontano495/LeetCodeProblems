class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _min = float('inf')
        smallestStr = ""
        for s in strs:
            if len(s) < _min:
                _min = len(s)
                smallestStr = s
        
        longestPrefix = ""
        longestPrefixFound = False
        i = 0
        while( longestPrefixFound == False and i < len(smallestStr)):
            longestPrefix = longestPrefix + smallestStr[i]
            for s in strs:
                if not self.IsPrefix(longestPrefix,s):
                    longestPrefix = longestPrefix[:len(longestPrefix)-1]
                    longestPrefixFound = True
            i += 1
        
        return longestPrefix
    
    def IsPrefix(self,p,s):
        i = 0
        for i in range(len(p)):
            if p[i] != s[i]:
                return False
        return True