class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dit = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord('a')] += 1
            dit[tuple(count)].append(st)
        return list(dit.values())