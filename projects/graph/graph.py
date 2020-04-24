"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

"""
# Create a Graph Data Structure that uses the Adjacency List
# Adjacency List one of two comment ways to represent graphs in code.
# In an adjacency list, the graph stores a list of vertices.
# For each vertex, it stores a list of each connected vertex.
"""

"""
Notice that this adjacency list doesn’t use any lists. The vertices collection 
is a dictionary which lets us access each collection of edges in O(1) constant time. 
Because the edges are contained in a set we can check for the existence of edges in O(1) constant time.
"""

"""
class Graph:
    def __init__(self):
        self.vertices = {
                          "A": {"B"},
                          "B": {"C", "D"},
                          "C": {"E"},
                          "D": {"F", "G"},
                          "E": {"C"},
                          "F": {"C"},
                          "G": {"A", "F"}
                        }
"""


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # empty

        """
        
        {
            A: {},
            B: {},
            C: {},
            D: {}
        }

        """

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # an empty set()

    def add_edge(self, v1, v2):  # we want to add a Directed edge from v1 to v2
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # directed edge from v1 to v2 (A: {B},)
        else:
            raise IndexError("That vertex does not exist!")

    # I'm at A where can I go? we want to have the ability to traverse. Get all the vertices
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  # if the vertex id doesn't exist, it'll return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex on the stack
            current_vertex = plan_to_visit.pop()
            # if not visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        explore(graph) {
            visit(this_vert);
            explore(remaining_graph);
        }

        """
        # Initial Case
        if visited is None:
            visited = set()  # initialize empty set for visited
        # Base cased: how do we know we're done? When we have no more neighbors
        # Track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)
        # Call the function recursively - on neighbors
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
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

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # switch to stack (instead of queue)
        neighbors_to_visit = Stack()
        visited_vertices = set()
        neighbors_to_visit.push((starting_vertex, []))  # create a tuple
        while neighbors_to_visit.size() > 0:
            current_vertex_plus_path = neighbors_to_visit.pop()
            current_vertex = current_vertex_plus_path[0]
            if current_vertex not in visited_vertices:
                if current_vertex == destination_vertex:
                    updated_path = current_vertex_plus_path[1] + [
                        current_vertex]
                    return updated_path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # add neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    updated_path = current_vertex_plus_path[1] + [
                        current_vertex]
                    neighbors_to_visit.push((neighbor, updated_path))

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
