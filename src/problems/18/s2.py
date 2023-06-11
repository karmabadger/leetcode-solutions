from typing import List, Dict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        if n < 4:
            return []

        nums.sort()

        res = []

        for i in range(0, n - 3):
            # Check for skipping duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    sum1 = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum1 < target:
                        k += 1
                    elif sum1 > target:
                        l -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return res


def main():
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    # print(Solution().fourSum([2, 2, 2, 2, 2], 8))
    # print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
    print(Solution().fourSum([-4, -3, -2, -1, 0, 0, 1, 2, 3, 4], 0))


if __name__ == "__main__":
    main()
