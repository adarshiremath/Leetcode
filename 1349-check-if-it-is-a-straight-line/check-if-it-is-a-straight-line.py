class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        vector_1 = [coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]]

        for i in range(2,len(coordinates)):
            vector_2 = [coordinates[i][0] - coordinates[0][0], coordinates[i][1] - coordinates[0][1]]

            if (vector_1[0]*vector_2[1]) - (vector_1[1]*vector_2[0]) != 0:
                return False

        return True