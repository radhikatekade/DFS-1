# Time complexity - O(m * n) (traverse) + O(m * n) (for bfs)
# Space complexity - O(m * n) (worse case: entire matrix except one element is 0, so everything
# gets added to the queue)

# Approach - Only difference from the earlier approach is instead of utilizing level variable change 
# element's value to its distance from nearest 0.

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
                    mat[i][j] = -1
        
        while not q.empty():
            curr = q.get()
            for d in dirs:
                nr = curr[0] + d[0]
                nc = curr[1] + d[1]

                if nr >= 0 and nr < m and nc >= 0 and nc < n and mat[nr][nc] == -1:
                    q.put((nr, nc))
                    mat[nr][nc] = mat[curr[0]][curr[1]] + 1
        
        return mat