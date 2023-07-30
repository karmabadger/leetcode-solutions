from typing import List, Tuple, Dict, Set


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        num_map = {}
        for i, num in enumerate(nums):
            if not num in num_map:
                num_map[num] = [i]
            else:
                num_map[num].append(i)

        tset = set()
        for i, num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                num3 = -num1 - num2
                if num3 in num_map:
                    k = next(filter(lambda x: x != i and x != j, num_map[num3]), None)
                    if k != None:
                        if k < i:
                            res2_tuple = (num3, num1, num2)
                        elif k > j:
                            res2_tuple = (num1, num2, num3)
                        else:
                            res2_tuple = (num1, num3, num2)

                        if not res2_tuple in tset:
                            tset.add(res2_tuple)

        return list(tset)


data = [
    # ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    # ([0, 1, 1], []),
    # ([0, 0, 0], [[0, 0, 0]]),
]

for input, output in data:
    print(Solution().threeSum(input), output)
