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