class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0 
        i= 0
        for col in range(len(strs[0])):
            ord1 = 0

            for str1 in strs:
                if ord1 == 0:
                    ord1 = ord(str1[col])
                elif ord1 > ord(str1[col]):
                    count += 1
                    break
                else:
                    ord1 = ord(str1[col])
        return count

        # Alternative solution using zip()

        count = 0
        for i in sip(*strs):
            if list(i) != sorted(i):
                count += 1
        return count 



