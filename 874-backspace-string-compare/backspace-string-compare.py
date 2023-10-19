class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        ts = []
        for ele in s:
            if ele == '#' and ss:
                ss.pop()
            elif ele != '#':
                ss.append(ele)
        
        for ele in t:
            if ele == '#' and ts:
                ts.pop()
            elif ele != '#':
                ts.append(ele)
        print("".join(ss), "".join(ts))
        if "".join(ss) == "".join(ts):
            return True
        return False        