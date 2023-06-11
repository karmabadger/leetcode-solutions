from typing import List, Dict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dic: dict[int, List[tuple[int, int]]] = {}

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    sum_ij = num1 + num2
                    if sum_ij in dic:
                        if i < j:
                            # if not find_and(i, j, dic[sum_ij]):
                            dic[sum_ij].append((i, j))
                        else:
                            # if not find_and(j, i, dic[sum_ij]):
                            dic[sum_ij].append((j, i))
                    else:
                        if i < j:
                            dic[sum_ij] = [(i, j)]
                        else:
                            dic[sum_ij] = [(j, i)]

        res = []
        res_dict = {}
        for key, item in dic.items():
            diff = target - key
            if diff != key:
                for i, j in item:
                    other = dic[diff]
                    lres = list(
                        filter(
                            lambda x: x[0] != i and x[1] != j,
                            other,
                        )
                    )

                    if len(lres) > 0:
                        r2 = [nums[i], nums[j], nums[r[0]], nums[r[1]]]
                        r2.sort()

                        r2_tuple = (r2[0], r2[1], r2[2], r2[3])
                        if not r2_tuple in res_dict:
                            res_dict[r2_tuple] = True
                            res.append(r2)
            else:
                

        return res


def find_and(i: int, j: int, l: List[tuple[int, int]]):
    for x, y in l:
        if i == x and j == y:
            return (x, y)
    return None


def main():
    # print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([2, 2, 2, 2, 2], 8))


if __name__ == "__main__":
    main()
