from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


# graph = Graph([
#     ("a", "b", 90),  ("a", "c", 138),  ("a", "d", 348),
#     ("b", "c", 84),  ("b", "e", 66),
#     ("c", "d", 156), ("c", "f", 90),
#     ("d", "g", 48),
#     ("e", "i", 84),
#     ("f", "g", 132), ("f", "h", 60),
#     ("g", "h", 48), ("g", "j", 150),
#     ("h", "i", 132), ("h", "j", 126),
#     ("i", "j", 126)
#     ])

# graph = Graph([
#     ("0", "1", 40),  ("0", "2", 55),
#     ("1", "2", 50),  ("1", "3",85), ("1", "4", 120),
#     ("2", "3", 60),  ("2", "4", 95),
#     ("3", "4", 80),  ("3", "5", 90),
#     ("4", "5", 70)
#     ])

# graph = Graph([
#     ("a", "b", 30),  ("a", "d", 35),  ("a", "c", 75),
#     ("b", "d", 35),  ("b", "e", 50), ("b", "f", 65),
#     ("c", "d", 25), ("c", "e", 15), ("c", "g", 60),
#     ("d", "e", 30),
#     ("e", "f", 25),
#     ("f", "g", 20)
#     ])

graph = Graph([
    ("1", "2", 500),  ("1", "3", 1600),  ("1", "4", 4600),  ("1", "5", 5720),
    ("2", "3", 1150),  ("2", "4", 3900), ("2", "5", 4940),
    ("3", "4", 1350),  ("3", "5", 1910),
    ("4", "5", 450),
    ])

print(graph.dijkstra("1", "4"))
