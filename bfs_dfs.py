graph = {}

n = int(input("Enter Number of vertices: "))

for i in range(n):
    graph[input(f"Enter vertex {i+1}: ")] = []

e = int(input("Enter number of edges: "))

print("Enter edges (v1 v2): ")

for i in range(e):

    u, v = input(f"Enter edge{i+1}: ").split()

    graph[u].append(v)
    graph[v].append(u)

# DFS
def dfs(start, visited=None):

    if visited is None:
        visited = []

    visited.append(start)

    print(start, end=" ")

    for nbr in graph[start]:

        if nbr not in visited:
            dfs(nbr, visited)

# BFS
def bfs(start):

    queue = [start]
    visited = [start]

    while queue:

        start = queue.pop(0)

        print(start, end=" ")

        for nbr in graph[start]:

            if nbr not in visited:

                visited.append(nbr)
                queue.append(nbr)

start = input("Starting vertex: ")

print("\nDFS Traversal:")
dfs(start)

print("\nBFS Traversal:")
bfs(start)