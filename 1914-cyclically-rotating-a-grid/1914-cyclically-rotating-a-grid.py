class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        layers = min(m, n) // 2
        
        for i in range(layers):
            layer = []
            # Top row
            for j in range(i, n - 1 - i): layer.append(grid[i][j])
            # Right column
            for j in range(i, m - 1 - i): layer.append(grid[j][n - 1 - i])
            # Bottom row
            for j in range(n - 1 - i, i, -1): layer.append(grid[m - 1 - i][j])
            # Left column
            for j in range(m - 1 - i, i, -1): layer.append(grid[j][i])
            
            # Effective rotation
            rot = k % len(layer)
            layer = layer[rot:] + layer[:rot]
            
            idx = 0
            # Fill Top row
            for j in range(i, n - 1 - i):
                grid[i][j] = layer[idx]
                idx += 1
            # Fill Right column
            for j in range(i, m - 1 - i):
                grid[j][n - 1 - i] = layer[idx]
                idx += 1
            # Fill Bottom row
            for j in range(n - 1 - i, i, -1):
                grid[m - 1 - i][j] = layer[idx]
                idx += 1
            # Fill Left column
            for j in range(m - 1 - i, i, -1):
                grid[j][i] = layer[idx]
                idx += 1
                
        return grid