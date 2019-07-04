import numpy

INF = 99999
V = 0

f = open("input.txt", "r")

inputFile = f.readlines()

graph = []

for i in range(len(inputFile)):
    if i == 0:

        V = int(inputFile[i])
    else:
        row = [int(elem.strip()) if elem.strip() !=
               'INF' else INF for elem in str(inputFile[i]).split(',')]
        graph.append(row)


def floydWarshall(graph):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # Check if existis Negative Cycle
    for i in range(V):
        if (graph[i][i] < 0):
            print("Existis Negative Cycle on Vertice(s): " + str(i))


print("Vertices: " + str(V))
print(graph)

floydWarshall(graph)

print(graph)

f = open("output.txt", "w")
for elem in graph:
    f.write(str(elem)+"\n")

f.close()
