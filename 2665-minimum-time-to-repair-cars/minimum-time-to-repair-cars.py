class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_ , max_ = 0, max(ranks) * (cars**2)
        ans = max_

        while  min_ <= max_:
            mid = (min_ + max_) // 2
            index = 0
            count = 0
            while index < len(ranks): 
                count += int((mid// ranks[index]) ** 0.5)
                index += 1
            
            if count >= cars:
                ans = mid
                max_ = mid - 1 
            else:
                min_ = mid + 1
        
        return ans