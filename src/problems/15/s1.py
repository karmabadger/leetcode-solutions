from typing import List, Tuple, Dict, Set


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if nums[0] == nums[len(nums) - 1]:
            if nums[0] == 0:
                return [[0, 0, 0]]
            else:
                return []

        total = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                abc = a + nums[l] + nums[r]
                if abc < 0:
                    l += 1
                elif abc > 0:
                    r -= 1
                else:
                    total.append([a, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return total


data = [
    ([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4], []),
    ([1, 1, -2], [1, 1, -2]),
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    # ([0, 1, 1], []),
    # ([0, 0, 0], [[0, 0, 0]]),
]

for input, output in data:
    print(Solution().threeSum(input), output)
