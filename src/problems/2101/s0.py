from typing import List
import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited_nodes = {}
        node_to_group: List[int] = [-1] * len(bombs)
        groups = []


        group = -1 # number of nodes in current group

        # stack is 0 to len(bombs) - 1
        # bomb_nodes = [BombNode(bomb[0], bomb[1], bomb[2]) for bomb in bombs]
        stack = list(range(len(bombs)))

        while stack:
            i = stack.pop()
            bomb1 = bombs[i]
            if i not in visited_nodes:
                visited_nodes[i] = True

                if node_to_group[i] == -1:
                    group += 1
                    node_to_group[i] = group
                    groups.append({i: True})

                    for j, bomb2 in enumerate(bombs):
                        if (i != j):
                            if dist(bomb1[0],bomb1[1], bomb2[0], bomb2[1]) <= bomb1[2]:
                                if node_to_group[j] == -1:
                                    node_to_group[j] = group
                                else:
                                    # merge groups
                                    for k in groups[node_to_group[j]]:
                                        node_to_group[k] = group
                                    groups[group].update(groups[node_to_group[j]])
                                    groups[node_to_group[j]] = None

                                groups[group][j] = True
                else:
                    # groups[group][i] = True

                    for j, bomb2 in enumerate(bombs):
                        if (i != j):
                            if dist(bomb1[0],bomb1[1], bomb2[0], bomb2[1]) <= bomb1[2]:
                                if node_to_group[j] == -1:
                                    node_to_group[j] = group
                                else:
                                    # merge groups
                                    for k in groups[node_to_group[j]]:
                                        node_to_group[k] = group
                                    groups[group].update(groups[node_to_group[j]])
                                    groups[node_to_group[j]] = None
                                    
                                groups[group][j] = True

        return max(groups) 

class BombNode:
    def __init__(self, x: int, y: int, r: int):
        self.visited = False
        self.neighbors: List[BombNode] = []

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
def dist(x1: int, y1: int, x2: int, y2:int) -> float:
    return math.sqrt(float((x1 - x2)**2 + (y1 - y2)**2))
    
if __name__ == "__main__":
    # print(Solution().maximumDetonation([[2, 1, 3], [6,1,4]]))
    # print(Solution().maximumDetonation([[1,1,5], [10,10,5]]))
    print(Solution().maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))