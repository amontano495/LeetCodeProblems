class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqMap = {}
        
        for c in magazine:
            if c not in freqMap.keys():
                freqMap[c] = 1
            else:
                freqMap[c] += 1
        
        for c in ransomNote:
            if c not in freqMap.keys():
                return False
            else:
                freqMap[c] -= 1
        
        for k,v in freqMap.items():
            if v < 0:
                return False
        
        return True