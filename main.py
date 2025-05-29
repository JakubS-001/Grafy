import random
import sys
from find_cycle import *
from graph_creation import create_hamiltonian_graph, create_non_hamiltonian_graph


def print_graph(graph):
    for i, neighbors in enumerate(graph):
        print(f"{i}:", *neighbors)

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--hamilton", "--non-hamilton", "-h", "-n"]:
        print("Użycie: python program.py --hamilton/-h lub --non-hamilton/-n")
        return

    while True:
        data = input("nodes> ")
        try:
            n=int(data)
            if n<1: raise ValueError
            break
        except:
            print("Podaj liczbę naturalną")

    graph = []

    if sys.argv[1] in ["--hamilton", "-h"]:
        saturation = None

        while saturation not in [30, 70]:
            saturation = int(input("saturation (30/70)> "))
        saturation = int(saturation) / 100

        graph = create_hamiltonian_graph(n, saturation)
    else:
        graph = create_non_hamiltonian_graph(n, 0.5)

    while True:
        command = input("> ").strip().lower()
        if command == "print":
            print_graph(graph)
        elif command=="find euler":
            find_eulerian_cycle(graph)
        elif command=="find hamilton":
            find_hamiltonian_cycle(graph)
        elif command == "exit":
            print("Exiting program.")
            break
        elif command == "help":
            print('''Komendy:
print - wyświetla graf (lista sąsiedztwa)
find euler - sprawdza czy w grafie znajduje się cykl Eulera
find hamilton - sprawdza czy w grafie znajduje się cykl Hamiltona
exit - kończy program
help - wyświetla pomoc''')

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\nExiting...")
    except KeyboardInterrupt:
        print("\nExiting...")
