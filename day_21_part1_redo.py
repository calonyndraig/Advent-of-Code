from collections import defaultdict, deque

def build_keypad_graph(layout):
    graph = defaultdict(list)
    rows = layout.splitlines()
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == " ":
                continue
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(rows) and 0 <= nj < len(rows[0]) and rows[ni][nj] != " ":
                    graph[char].append(rows[ni][nj])
    return graph

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path + [node]
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [node]))
    return []

def calculate_complexity(codes, numeric_graph, directional_graph):
    complexities = []
    for code in codes:
        numeric_part = int(code.lstrip("0A"))  # Extract numeric part
        current = 'A'
        total_moves = 0

        for digit in code:
            path = bfs_shortest_path(numeric_graph, current, digit)
            total_moves += len(path) - 1  # Count steps to the target
            current = digit

        complexities.append(total_moves * numeric_part)
    return sum(complexities)

# Define layouts
numeric_layout = """
789
456
123
 0A
"""

directional_layout = """
 ^
< v >
 A
"""

# Build graphs
numeric_graph = build_keypad_graph(numeric_layout)
directional_graph = build_keypad_graph(directional_layout)

# Input codes
codes = ["029A", "980A", "179A", "456A", "379A"]

# Calculate complexity
result = calculate_complexity(codes, numeric_graph, directional_graph)
print("Total complexity:", result)
