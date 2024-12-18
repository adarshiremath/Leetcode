class Solution:
    def reformat(self, s: str) -> str:
        num = []
        alpha = []
        
        for i in s:
            if i.isnumeric():
                num.append(i)
            else:
                alpha.append(i)
        if abs(len(num) - len(alpha)) > 1:
            return ""
        res = ""
        for i in range(min(len(num), len(alpha))):
            res += num[i] + alpha[i]
        
        if len(num) > len(alpha):
            res += num[-1]    
        elif len(num) < len(alpha):
            res = alpha[-1] + res
        return res