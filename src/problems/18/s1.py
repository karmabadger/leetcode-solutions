from typing import List, Dict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dic: dict[int, dict[tuple[int, int], int]] = {}

        indexes_set: set[tuple[int, int]] = set()

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    if i < j:
                        if (i, j) in indexes_set:
                            continue
                        else:
                            indexes_set.add((i, j))
                    else:
                        if (i, j) in indexes_set:
                            continue
                        else:
                            indexes_set.add((j, i))

                    sum_ij = num1 + num2

                    if sum_ij in dic:
                        if num1 < num2:
                            # if not find_and(num1, num2, dic[sum_ij]):
                            if (num1, num2) in dic[sum_ij]:
                                dic[sum_ij][(num1, num2)] += 1
                            else:
                                dic[sum_ij][(num1, num2)] = 1
                        else:
                            # if not find_and(num2, num1, dic[sum_ij]):
                            if (num2, num1) in dic[sum_ij]:
                                dic[sum_ij][(num2, num1)] += 1
                            else:
                                dic[sum_ij][(num2, num1)] = 1
                    else:
                        if num1 < num2:
                            dic[sum_ij] = {(num1, num2): 1}
                        else:
                            dic[sum_ij] = {(num2, num1): 1}

        res = []
        res_dict = {}
        for key, item in dic.items():
            diff = target - key
            if diff != key:
                for num1, num2 in item:
                    other = dic[diff]
                    lres = list(
                        filter(
                            lambda x: x[0] != num1 and x[1] != num2,
                            other,
                        )
                    )

                    if len(lres) > 0:
                        for r in lres:
                            r2 = [num1, num2, r[0], r[1]]
                            r2.sort()

                            r2_tuple = (r2[0], r2[1], r2[2], r2[3])
                            if not r2_tuple in res_dict:
                                res_dict[r2_tuple] = True
                                res.append(r2)
            else:
                for (num1, num2), c in item.items():
                    if c > 1:
                        r2 = [num1, num2, num1, num2]
                        r2.sort()

                        r2_tuple = (r2[0], r2[1], r2[2], r2[3])
                        if not r2_tuple in res_dict:
                            res_dict[r2_tuple] = True
                            res.append(r2)

        return res


def find_and(i: int, j: int, l: List[tuple[int, int]]):
    for x, y in l:
        if i == x and j == y:
            return (x, y)
    return None


def main():
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([2, 2, 2, 2, 2], 8))


if __name__ == "__main__":
    main()
