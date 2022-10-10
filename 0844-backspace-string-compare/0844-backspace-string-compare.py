class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_final = self.evalStr(s)
        t_final = self.evalStr(t)
        
        return s_final == t_final
        
    def evalStr(self, s):
        s_final = []
        for c in s:
            if c == '#':
                if len(s_final) < 1:
                    pass
                else:
                    s_final.pop()
            else:
                s_final.append(c)
        return ''.join(s_final)
                