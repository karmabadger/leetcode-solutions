from typing import List, Tuple, Dict, Set


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        if nums[0] == nums[len(nums) - 1]:
            return nums[0] * 3

        closest = nums[0] + nums[1] + nums[2]
        best = abs(target - closest)
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                abc = a + nums[l] + nums[r]
                if abs(target - abc) < best:
                    closest = abc
                    best = abs(target - closest)
                if abc < target:
                    l += 1
                elif abc > target:
                    r -= 1
                else:
                    return target

        return closest


data = [
    (([-1, 2, 1, -4], 1), 2),
    (([0, 0, 0], 1), 0),
]

for input, output in data:
    print(Solution().threeSumClosest(input[0], input[1]), output)
