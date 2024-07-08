class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        x = {a for a,_ in trust} # not judges
        c = Counter(b for _,b in trust) # person: num of trusters
        for a, f in c.items():
            if f == n-1 and a not in x:
                return a
        
        return -1