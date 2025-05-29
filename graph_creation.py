import random

def create_hamiltonian_graph(n, saturation):

    max_edges = n * (n - 1) // 2
    target_edges = int(max_edges * saturation)

    graph = [[] for _ in range(n)]
    
    nodes = list(range(n))
    random.shuffle(nodes)

    for i in range(n):
        a, b = nodes[i], nodes[(i + 1) % n]
        if b not in graph[a]:
            graph[a].append(b)
            graph[b].append(a)
    
    edges = set()
    for i in range(n):
        for j in graph[i]:
            if i < j:
                edges.add((i, j))
    
    while len(edges) < target_edges:
        a, b = random.sample(range(n), 2)
        if b not in graph[a]:
            graph[a].append(b)
            graph[b].append(a)
            edges.add((min(a, b), max(a, b)))

    for i in range(n):
        if len(graph[i]) % 2 != 0:
            for j in range(n):
                if i != j and j not in graph[i] and len(graph[j]) % 2 != 0:
                    graph[i].append(j)
                    graph[j].append(i)
                    break

    return graph

def create_non_hamiltonian_graph(n, saturation):
    graph = create_hamiltonian_graph(n, saturation)

    isolated = random.randint(0, n - 1)

    for neighbor in graph[isolated]:
        graph[neighbor].remove(isolated)
    graph[isolated] = []

    return graph