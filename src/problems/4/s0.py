class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        return recur(nums1, nums2)


def recur(nums1, nums2):
    if len(nums1) == 1 and len(nums2) == 1:
        return (nums1[0] + nums2[0]) / 2

    mid1 = len(nums1) // 2
    mod1 = len(nums1) % 2
    med1 = (nums1[mid1] + nums1[mid1 - 1]) / 2 if mod1 == 0 else nums1[mid1]

    mid2 = len(nums2) // 2
    mod2 = len(nums2) % 2
    med2 = (nums2[mid2] + nums2[mid2 - 1]) / 2 if mod2 == 0 else nums2[mid2]

    if med1 == med2:
        return med1
    elif med1 > med2:
        return recur(nums1[: mid1 + mod1], nums2[mid2:])
    elif med1 < med2:
        return recur(nums1[mid1:], nums2[: mid2 + mod2])


def main():
    solution = Solution()
    # nums1 = [1, 3]
    # nums2 = [2]
    # print(solution.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays(nums2, nums1))


if __name__ == "__main__":
    main()
