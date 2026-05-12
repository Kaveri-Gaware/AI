import heapq

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def heuristic(state):
    dist = 0

    for i in range(3):
        for j in range(3):
            val = state[i][j]

            if val != 0:
                x = (val - 1) // 3
                y = (val - 1) % 3

                dist += abs(x - i) + abs(y - j)

    return dist



def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j



def get_neighbors(state):
    x, y = find_zero(state)

    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbors = []

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = \
            new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors



def a_star(start):
    open_list = []

    heapq.heappush(open_list,
        (heuristic(start), 0, start, [start]))

    visited = set()

    while open_list:

        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path

        visited.add(str(current))

        for neighbor in get_neighbors(current):

            if str(neighbor) not in visited:

                heapq.heappush(open_list,
                    (
                        g + 1 + heuristic(neighbor),
                        g + 1,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None



start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = a_star(start)

if solution:

    for i, state in enumerate(solution):

        if i == 0:
            print("Initial State")
        else:
            print("Step", i)

        for row in state:
            print(row)

        print()

    print("Total steps required to reach the goal:",
          len(solution) - 1)

else:
    print("No solution found")
