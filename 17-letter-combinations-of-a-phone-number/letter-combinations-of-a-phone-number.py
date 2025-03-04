class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, ans):
            if len(ans) == len(digits):
                res.append(ans)
                return

            for c in digitToChar[digits[i]]:
                backtrack(i+1, ans + c)
        
        if digits:
            backtrack(0, "")

        return res