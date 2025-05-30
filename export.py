def print_tikz(graph):
    n = len(graph)
    print("\\begin{tikzpicture}[every node/.style={circle,draw}, scale=2]")
    for i in range(n):
        angle = 360 * i / n
        print(f"\\node (v{i}) at ({angle}:2) {{{i}}};")
    drawn = set()
    for i, neighbors in enumerate(graph):
        for j in neighbors:
            if (j, i) not in drawn:
                print(f"\\draw (v{i}) -- (v{j});")
                drawn.add((i, j))
    print("\\end{tikzpicture}")