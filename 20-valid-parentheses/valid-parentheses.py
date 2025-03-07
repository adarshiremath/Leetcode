class Solution:
    def isValid(self, s: str) -> bool:
        dit = {'(' : ')', '{' : '}', '[' : ']'}
        if len(s) % 2 != 0: return False
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if stack:
                    top = stack.pop()
                    if dit[top] != i:
                        return False
                else:
                    return False
        if stack:
            return False
        return True