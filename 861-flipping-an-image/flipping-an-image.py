class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = [1 if i==0 else 0 for i in image[i][::-1]]
        return image