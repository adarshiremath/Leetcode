class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        dit = {}

        for i in range(len(groupSizes)):
            if groupSizes[i] in dit:
                dit[groupSizes[i]].append(i)
            else:
                dit[groupSizes[i]] = [i]
        result = []
        for key, value in dit.items():
            while(value):
                result.append(value[:key])
                value = value[key:]
        return result