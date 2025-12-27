from collections import deque

# Graph is represented as adjacency list (dictionary)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    steps = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            steps.append(list(visited))

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return steps


def dfs(graph, start):
    visited = set()
    steps = []

    def dfs_helper(node):
        if node not in visited:
            visited.add(node)
            steps.append(list(visited))
            for neighbor in graph[node]:
                dfs_helper(neighbor)

    dfs_helper(start)
    return steps