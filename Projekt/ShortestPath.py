from sys import maxsize


class BellmanFord(object):
    def __init__(self):  #  konstruktor
        """Constructor"""

    def ShortestPath(self, weight, source):
        size = len(weight)
        temp = -1;  # jak jest -1 tzn, ze nie ma predykatu, czyli wczesniejszego wierzcholka
        inifinity = maxsize

        predicate = [temp] * size
        minDistance = [inifinity] * size

        # minDistance[source] = 0, bo odleglosc do samego siebie = 0
        minDistance[source] = 0

        # relaksujemy krawedz V-1 razy aby znalezc wszystkie najkrotsze sciezki
        for i in range(1, size - 1):
            for v in range(size):
                for a in self.adjacency(weight, v):
                    if minDistance[a] > minDistance[v] + weight[v][a]:
                        minDistance[a] = minDistance[v] + weight[v][a]
                        predicate[a] = v

        # sprawdzamy czy sa ujemne cykle
        for v in range(size):
            for a in self.adjacency(weight, v):
                if minDistance[a] > minDistance[v] + weight[v][a]:
                    raise Exception("Error! Negative cycle present!")

        return [predicate, minDistance]

    #  zwraca liste sasiadow wierzcholka v
    def adjacency(self, Graph, v):
        result = []
        for a in range(len(Graph)):
            if Graph[v][a] is not None:
                result.append(a)

        return result;






