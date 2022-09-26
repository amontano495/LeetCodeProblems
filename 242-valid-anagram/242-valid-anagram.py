class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqmap = {}
        for c in s:
            if c not in freqmap.keys():
                freqmap[c] = 1
            else:
                freqmap[c] += 1
        for c in t:
            if c not in freqmap.keys():
                return False
            else:
                freqmap[c] -= 1
        for k,v in freqmap.items():
            if v > 0:
                return False
        return True