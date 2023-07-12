from typing import List

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(numCourses))

        children: List[List[int] | None] = [None] * numCourses
        deps_count = [0] * numCourses

        for dep in prerequisites:
            a, b = dep
            deps_count[a] += 1

            childrenb = children[b]
            if childrenb == None:
                children[b] = [a]
            else:
                childrenb.append(a)

        q = deque()
        for i, count in enumerate(deps_count):
            if count == 0:
                q.append(i)

        res = []
        while len(q) > 0:
            item = q.popleft()
            res.append(item)
            children_item = children[item]
            if children_item != None:
                for child in children_item:
                    deps_count[child] -= 1
                    if deps_count[child] == 0:
                        q.append(child)

        if len(res) != numCourses:
            return []
        return res


inputs = [
    (2, [[1, 0]]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    (1, []),
]

for input in inputs:
    print(Solution().findOrder(input[0], input[1]))
