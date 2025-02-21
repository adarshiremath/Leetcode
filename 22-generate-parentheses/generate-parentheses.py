class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(ans, open_p, closed_p):
            if len(ans) == 2 * n:
                res.append(ans)
                return
            
            if open_p < n:
                generate(ans + "(", open_p + 1, closed_p)
            
            if closed_p < open_p:
                generate(ans + ")", open_p, closed_p + 1)
            
        generate("", 0, 0)
        return res