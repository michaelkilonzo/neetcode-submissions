class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        if grid[0][0] == 1 or grid[N - 1][M - 1] == 1:
            return -1 

        queue.append((0, 0))
        visited.add((0, 0))
        length = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft() 
                if r == N - 1 and c == M - 1:
                    return length
                
                neighbours = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

                for dr, dc in neighbours:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr == N or
                        nc < 0 or nc == M or
                        (nr, nc) in visited or
                        grid[nr][nc] == 1):
                        continue

                    visited.add((nr, nc))
                    queue.append((nr, nc))
                
            length += 1
            
        return -1 