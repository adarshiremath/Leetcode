class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_possible(time):
            total_cars = 0
            for r in ranks:
                total_cars += int((time // r) ** 0.5)
            return total_cars >= cars

        left, right = 1, max(ranks) * cars * cars
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
