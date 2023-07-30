from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1

        r = counts[0]
        g = counts[1]
        b = counts[2]

        for i in range(r):
            nums[i] = 0

        end = r + g
        for i in range(r, end):
            nums[i] = 1

        for i in range(end, end + b):
            nums[i] = 2


data = [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([2, 0, 1], [0, 1, 2]),
]

for input, output in data:
    Solution().sortColors(input)
    print(input, output)
