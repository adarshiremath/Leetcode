class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            start,destination=destination,start
        if sum(distance[start:destination])<sum(distance[destination:])+sum(distance[:start]):
            return sum(distance[start:destination])
        else:
            return sum(distance[destination:])+sum(distance[:start])