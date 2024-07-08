class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lis = []
        s = list(s)
        for i in s:
            if i.isalpha():
                lis.append(i)  
        lis = lis[::-1]
        j = 0
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = lis[j]
                j += 1
            i += 1
        return "".join(s)