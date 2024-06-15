class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dit = {5:0, 10:0, 20:0}
        
        for i in bills:
            dit[i] = dit.get(i, 0) + 1
            if i == 10:
                if dit[5] >= 1:
                    dit[5] -= 1
                else:
                    return False
            elif i == 20:
                if (dit[10] > 0 and dit[5]>0):
                    dit[10] -= 1
                    dit[5] -= 1
                elif dit[5] >= 3:
                    dit[5] -= 3
                else:
                    return False
        return True