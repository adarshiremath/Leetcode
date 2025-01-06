class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        for i in range(len(boxes)):
            Sum = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    Sum += abs(i - j)
            answer.append(Sum)
        return answer