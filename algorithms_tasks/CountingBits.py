# https://leetcode.com/problems/counting-bits/submissions/

class Solution:
    def countBits(self, n: int) -> List[int]:
        # lst = []
        # for i in range(n + 1):
        #     # divmode(1, 2) = (0, 1)
        #     # divmode(3, 2) = (1, 1)
        #     count = 0
        #     num = i
        #     while True:
        #         num, ost = divmod(num, 2)
        #         if ost == 1:
        #             count += 1
        #         if num == 0:
        #             break
        #     lst.append(count)
        # return lst

        lst = []

        for i in range(n + 1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            lst.append(count)

        return lst

