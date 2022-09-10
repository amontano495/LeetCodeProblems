class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freqMap = {}
        for c in t:
            if c not in freqMap.keys():
                freqMap[c] = 1
            else:
                freqMap[c] += 1
        for c in s:
            freqMap[c] -= 1
            
        for k,v in freqMap.items():
            if v > 0:
                return k