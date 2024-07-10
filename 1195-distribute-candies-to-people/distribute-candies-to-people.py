class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = -1
        j = 0
        res = [0] * num_people
        while candies > 0:
            i += 1
            if i == num_people:
                i = 0
            j += 1
            candie = j if candies > j else candies
            candies -= j
            res[i] += candie
        return res