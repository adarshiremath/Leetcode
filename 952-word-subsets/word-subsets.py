class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dit = {}
        for word in words2:
            count = {}
            for ele in word:
                count[ele] = count.get(ele, 0) + 1
            for k, v in count.items():
                dit[k] = max(dit.get(k, 0) , v)
        res= []
        for word in words1:
            count = {}
            for ele in word:
                count[ele] = count.get(ele, 0) + 1
            for k, v in dit.items():
                if k not in count:
                    break
                count[k] -= v
                if count[k] < 0:
                    break
            else:
                res.append(word)
        
        return res