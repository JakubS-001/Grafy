def find_eulerian_cycle(graph):
    n = len(graph)
    for neighbors in graph:
        if len(neighbors) % 2 != 0:
            print("Graf nie ma cyklu Eulera (nie wszystkie stopnie są parzyste).")
            return

    def dfs(u, graph_copy, path):
        while graph_copy[u]:
            v = graph_copy[u].pop()
            graph_copy[v].remove(u)
            dfs(v, graph_copy, path)
        path.append(u)

    graph_copy = [neighbors.copy() for neighbors in graph]
    path = []
    dfs(0, graph_copy, path)
    print("Cykl Eulera:", path[::-1])

def find_hamiltonian_cycle(graph):
    n = len(graph)
    path = []

    def backtrack(v, visited):
        #print("Exploring path:", path)
        if len(path) == n:
            return path[0] in graph[v]  # Sprawdza, czy ostatni wierzchołek łączy się z pierwszym
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                if backtrack(neighbor, visited):
                    return True
                path.pop()
                visited[neighbor] = False
        return False

    for start in range(n):
        visited = [False] * n
        visited[start] = True
        path = [start]
        if backtrack(start, visited):
            print("Cykl Hamiltona:", path + [path[0]])
            return
    print("Brak cyklu Hamiltona.")