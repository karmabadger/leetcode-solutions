from typing import List
import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited_nodes = {}
        node_to_group: List[int] = [-1] * len(bombs)
        groups = []


        group = -1 # number of nodes in current group

        # stack is 0 to len(bombs) - 1
        bomb_nodes = [BombNode(bomb[0], bomb[1], bomb[2]) for bomb in bombs]
        
        # for each bomb node, find all neighbors
        for i, bomb1 in enumerate(bomb_nodes):
            for j, bomb2 in enumerate(bomb_nodes):
                if (i != j):
                    if dist(bomb1.x, bomb1.y, bomb2.x, bomb2.y) <= bomb1.r:
                        bomb1.neighbors.append(bomb2)

        stack = bomb_nodes
        while stack:
            bomb1 = stack.pop()
            if not bomb1.visited:
                bomb1.visited = True
                for bomb2 in bomb1.neighbors:
                    if not bomb2.visited:
                        stack.append(bomb2)
                        
                

class BombNode:
    def __init__(self, x: int, y: int, r: int):
        self.visited = False
        self.neighbors: List[BombNode] = []
        self.x = x
        self.y = y
        self.r = r



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