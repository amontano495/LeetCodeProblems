class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        assoc = {}
        tokens = s.split(' ')
        if len(tokens) != len(pattern):
            return False
        
        for i in range(len(tokens)):
            if tokens[i] not in assoc.values() and pattern[i] not in assoc.keys():
                assoc[pattern[i]] = tokens[i]
            if tokens[i] in assoc.values() and pattern[i] not in assoc.keys():
                return False
            if assoc[pattern[i]] != tokens[i]:
                return False
        return True