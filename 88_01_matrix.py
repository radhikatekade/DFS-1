# Time complexity - O(m * n) (traverse) + O(m * n) (for bfs)
# Space complexity - O(m * n) (worse case: entire matrix except one element is 0, so everything
# gets added to the queue)

# Approach - Initially traverse the matrix and start adding location of 0s to the queue and converting 1s 
# to (-1)s because later we need distinction between 1 as element versus 1 as distance. Maintain a level
# variable to compute distance.

from queue import Queue
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat is None or len(mat) == 0:
            return mat
        m = len(mat)
        n = len(mat[0])
        q = Queue()
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.put((i, j))
                else:
                    # temporary state change
                    mat[i][j] = -1
        
        lvl = 0        
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                for d in dirs:
                    nr = curr[0] + d[0]
                    nc = curr[1] + d[1]

                    if nr >= 0 and nr < m and nc >= 0 and nc < n and mat[nr][nc] == -1:
                        q.put((nr, nc))
                        mat[nr][nc] = lvl + 1
            lvl += 1
        
        return mat