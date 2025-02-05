# Time complexity - O(m * n)
# Space complexity - O(m * n)

# Approach - bfs - For every row and col in-bounds with image[row][col] == oldColor will be added to the queue,
# the queue will start from the location given to us.

from queue import Queue
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        oldColor = image[sr][sc]
        q = Queue()
        q.put((sr, sc))
        m = len(image)
        n = len(image[0])
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        while not q.empty():
            curr = q.get()
            image[curr[0]][curr[1]] = color

            for d in dirs:
                if (curr[0] + d[0] >= 0) and (curr[0] + d[0] < m) and (curr[1] + d[1] >= 0) and (curr[1] + d[1] < n) and image[curr[0] + d[0]][curr[1] + d[1]] == oldColor:
                    q.put((curr[0] + d[0], curr[1] + d[1]))
        
        return image