from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -101
        count = 0
        start = -1
        for i, num in enumerate(nums):
            if num == prev:
                prev = num
                nums[i] = -101
                count += 1
                if start == -1:
                    start = i
            else:
                prev = num

        if start == -1:
            return len(nums)

        i = 0
        for u, num in enumerate(nums, start):
            if num != -101:
                if i != u:
                    nums[i] = num
                i += 1

        return len(nums) - count


# test it out
def main():
    solution = Solution()
    nums = [1, 1, 2]
    print(solution.removeDuplicates(nums), nums)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates(nums), nums)


if __name__ == "__main__":
    main()
