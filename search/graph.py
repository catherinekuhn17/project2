import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        Method for using breadth first search to find the shortest path from a start node to an end node.
        
        parametrs:
            self: network to traverse through
            start: starting node
            end: ending node

        returns:
            shortest path from start to end (if it exists)
        """
        queue = []  #to know which node to visit next
        visited = []  # will fill with visited nodes
        backtrace = {
        }  # creating a dict that we can backtrace from. format is {child : parent}

        queue.append(start_node)  # add start node to queue
        visited.append(start_node)  # mark start as visited

        while queue:
            current_node = queue.pop()  # keep track of current node
            path = current_node
            if current_node == end:  # break out of cycle if we reach the end
                break
            else:
                for nbr in self[current_node]:  # otherwise, loop through neighbors
                    if nbr not in visited:
                        queue.append(nbr)
                        visited.append(nbr)
                        backtrace[nbr] = current_node  # keep track of this neihgbors parent for pathfinding

        if end != None and end not in backtrace.keys():  # condition that there is and end node. but no path
            return None
        elif end != None:  # condition that there is and end node and a path
            path = [end]
        elif end == None:  # condition that there is no end node
            path = [path]

        while path[-1] != start_node:  # loop through until we reach the start node
            child_node = path[-1]
            parent_node = backtrace[child_node]  # find the current end of path node's parent
            path.append(parent_node)  # append to path

        return path[::-1]  # shortest path is the reverse of this            




