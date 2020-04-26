class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("That vertex does not exist!")

# ancestors:
# [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    # Build our graph
    graph = Graph()  # make a graph

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)  # parent
        graph.add_vertex(child)  # child
        graph.add_edge(child, parent)

    # BFS
    queue = Queue()
    queue.enqueue([starting_node])

    path_length = 1
    earliest_ancestor = -1

    # while the queue is not Empty
    while queue.size() > 0:
        # dequeue the next path on the queue
        path = queue.dequeue()
        current_node = path[-1]  # last thing in the path

        if len(path) >= path_length and current_node < earliest_ancestor:
            path_length = len(path)
            earliest_ancestor = current_node

        if len(path) > path_length:
            path_length = len(path)  # updating the path length
            earliest_ancestor = current_node

        neighbors = graph.vertices[current_node]
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            queue.enqueue(path_copy)

    return earliest_ancestor


"""
UPER
Think we can use a BFS

 def bfs(self, starting_vertex, destination_vertex):
        # Breadth First Search - With Search you stop once you find what you're searcing for.
        # create a empty queue, and enqueue a PATH to the starting vertex
        neighbors_to_visit = Queue()  # what vertices are we planning to go to next
        # queue.enqueue ([starting_vertex])
        neighbors_to_visit.enqueue([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the queue is not empty
        while neighbors_to_visit.size() > 0:
            # dequeue the first PATH
            current_path = neighbors_to_visit.dequeue()
            # grab the last vertex in the path
            current_vertex = current_path[-1]
            # if it hasn't been visted
            if current_vertex not in visited_vertices:
                # check if its the target
                if current_vertex == destination_vertex:
                    # Return the path
                    return current_path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # make new versions of the current path, with each neighbor added to them
                for next_vertext in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(current_path)
                    # new_path = current_path[:] or you could do this
                    # add the neighbor
                    new_path.append(next_vertext)
                    # add the new path to the queue
                    neighbors_to_visit.enqueue(new_path)
        # What happens here in Python automatically? implied return None
        return None  # being explicit


"""
