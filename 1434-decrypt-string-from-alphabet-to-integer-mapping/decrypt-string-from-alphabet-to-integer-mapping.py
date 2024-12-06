class Solution:
    def freqAlphabets(self, s: str) -> str:
        word = ""
        i = 0 
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                word += chr(96 + int(s[i:i+2]))
                i += 3
            else:
                word += chr(96 + int(s[i]))
                i += 1
        return word