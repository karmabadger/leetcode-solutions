from typing import List
import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        neighbors = [[] for _ in range(len(bombs))]

        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, rj) in enumerate(bombs):
                if i != j and  dist2(xi, yi, xj, yj) <= ri**2:
                    neighbors[i].append(j)
        
        res = 0
        for i in range(len(bombs)):
            visited = set([i])
            dfs(i, visited, neighbors)
            res = max(res, len(visited))
        
        return res


def dfs(u: int, visited: set, neighbors: List[List[int]]) -> None:
    for v in neighbors[u]:
        if v not in visited:
            visited.add(v)
            dfs(v, visited, neighbors)

                



def memoize(f):
    fast = {}  
    def partner(x1: int, y1: int, x2: int, y2:int) -> float:
        if (x1,y1,x2,y2) not in fast: 
            tmp = f(x1,y1,x2,y2)
            fast[(x1,y1,x2,y2)] = f(x1,y1,x2,y2)
            return tmp
        return fast[(x1,y1,x2,y2)]  
    return partner

@memoize
def dist2(x1: int, y1: int, x2: int, y2:int) -> int:
    return (x1 - x2)**2 + (y1 - y2)**2
    
if __name__ == "__main__":
    # print(Solution().maximumDetonation([[2, 1, 3], [6,1,4]]))
    # print(Solution().maximumDetonation([[1,1,5], [10,10,5]]))
    print(Solution().maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))