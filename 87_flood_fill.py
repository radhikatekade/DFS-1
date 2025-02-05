# Time complexity - O(m * n)
# Space complexity - O(m * n)

# Approach - dfs - recursively run through the matrix using dirs array, run dfs inside the for loop for dirs
# and base case will check out-of-bounds row and col idx and the color of the image[row][col].

from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        self.oldColor = image[sr][sc]
        self.m = len(image)
        self.n = len(image[0])
        self.dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        self.dfs(image, sr, sc, color)
        return image
    
    def dfs(self, image: List[List[int]], row: int, col: int, color: int) -> None:
        # base case
        if row < 0 or row == self.m or col < 0 or col == self.n or image[row][col] != self.oldColor:
            return

        # logic
        image[row][col] = color
        for d in self.dirs:
            nr = row + d[0]
            nc = col + d[1]
            self.dfs(image, nr, nc, color)