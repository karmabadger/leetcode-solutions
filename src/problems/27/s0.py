from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1

        for i, num in enumerate(nums):
            if num == val:
                while end > i and nums[end] == val:
                    end -= 1
                if end > i:
                    nums[i] = nums[end]
                    nums[end] = val
                    end -= 1
                elif end == i:
                    return i
              
        return end + 1


# test it out
def main():
    solution = Solution()
    # nums = [3, 2, 2, 3]
    # print(solution.removeElement(nums, 3), nums)
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # print(solution.removeElement(nums, 2), nums)
    # nums = [1]
    # print(solution.removeElement(nums, 1), nums)
    nums = [4,5]
    print(solution.removeElement(nums, 4), nums)


if __name__ == "__main__":
    main()
