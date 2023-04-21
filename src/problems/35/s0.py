from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if target < nums[start]:
            return 0
        if target > nums[end]:
            return end + 1
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start


# test it out
def main():
    # nums = [1,3,5,6]
    # target = 5
    # print(Solution().searchInsert(nums, target))

    nums = [1,3,5,6]
    target = 2
    print(Solution().searchInsert(nums, target))

    # nums = [1,3,5,6]
    # target = 7
    # print(Solution().searchInsert(nums, target))

    # nums = [1]
    # target = 1
    # print(Solution().searchInsert(nums, target))
    
    # nums = [1, 3]
    # target = 1
    # print(Solution().searchInsert(nums, target))


if __name__ == "__main__":
    main()
