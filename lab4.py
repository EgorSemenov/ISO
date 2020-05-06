import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.ribs = []

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node+1, "t", dist[node])
        print('Визуализация(рёбра, которые будут проведены:)')
        for i in self.ribs:
            print(i)


    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] != 'inf' and \
                        sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    self.ribs.append(str(u+1) + '-' + str(v+1))
        self.printSolution(dist)



def floydWarshall(graph):
    dist = graph
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)

def printSolution(dist):
    print("Following matrix shows the shortest distances\
between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == INF):
                print("%7s" % ("INF"), end='')
            else:
                print("%7d\t" % (dist[i][j]), end='')
            if j == V - 1:
                print("")

g = Graph(9)
###############
#задание 2 а)
###############
print('задание 2 а)')
g.graph = [['inf', 2, 'inf', 'inf', 3, 1, 'inf', 'inf', 'inf'],
           [2, 'inf', 3, 'inf', 1, 'inf', 'inf', 'inf', 'inf'],
           ['inf', 3, 'inf', 4, 2, 'inf', 'inf', 2, 'inf'],
           ['inf', 'inf', 4, 'inf', 'inf', 'inf', 'inf', 'inf', 2],
           ['inf', 1, 2, 'inf', 'inf', 1, 1, 3, 'inf'],
           [1, 'inf', 'inf', 'inf', 1, 'inf', 0, 'inf', 'inf'],
           ['inf', 'inf', 'inf', 'inf', 1, 'inf', 'inf', 2, 'inf'],
           ['inf', 'inf', 2, 4, 'inf', 'inf', 2, 'inf', 1],
           ['inf', 'inf', 'inf', 2, 'inf', 'inf', 'inf', 1, 'inf']
           ]

g.dijkstra(0)

V = 4
INF = 99999
#задание 4 а)
graph = [[0, -15, 15, INF, INF],
         [20, 0, 7, 1, INF],
         [8, INF, 0, -10, -3],
         [INF, 2, INF, 0, 6],
         [INF, INF, 14, 4, 0]]
print('задание 4 а)')
floydWarshall(graph)

