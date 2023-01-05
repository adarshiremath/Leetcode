class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if(len(pattern) != len(s)): return False
        dit ={}
        for x,y in zip(pattern, s):
            if x in dit and y != dit[x]: return False
            dit[x] = y

        flipped={}
        for key,value in dit.items():
            if value in flipped: return False
            flipped[value] = key
        return True
        
