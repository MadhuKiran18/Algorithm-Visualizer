import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    visited_steps = []

    while open_set:
        _, current = heapq.heappop(open_set)
        visited_steps.append(current)

        if current == end:
            break

        r, c = current
        neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                temp_g = g_score[current] + 1
                neighbor = (nr, nc)

                if temp_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g
                    f_score[neighbor] = temp_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    # Reconstruct path
    path = []
    cur = end
    while cur in came_from:
        path.append(cur)
        cur = came_from[cur]
    path.append(start)
    path.reverse()

    return {
        "visited": visited_steps,
        "path": path
    }