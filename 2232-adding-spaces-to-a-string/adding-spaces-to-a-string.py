class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        news = ""
        i = 0
        j = 0
        flag = True
        while i < len(s):
            if flag and i == spaces[j]:
                news += " " + s[i]
                j += 1
                if j == len(spaces):
                    flag = False
            else:
                news += s[i]
            i += 1
        return news
        