import networkx as nx

class Graph:
    """
    Graph class. With this class, you can initialize a directed graph, and use a breadth first search method
    to find the shortest path between two nodes.
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and
        
        Parameters
        ----------
        filename : filename of directed network
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
    
    def nbr(self, node):
        """
        added for testing reasons
        Parameters
        ----------
        node : a node in the graph
        
        Returns
        -------
        the neighbors of that node
        """
        return self.graph[node]

    def bfs(self, start, end=None):
        """
        Method for using breadth first search to find the shortest path from a start node to an end node.
        
        Parameters
        ----------
        self : network to traverse through
        start : starting node
        end : ending node

        Returns
        -------
        shortest_path : shortest path from start node to end node (if it exists) or the end of network. If there is no connection 
            between the start and end node, None is returned.
        """
        queue = []  # to know which node to visit next in current layer
        visited = []  # will fill with visited nodes
        backtrace = {
        }  # creating a dict that we can backtrace from. format is {child : parent}

        queue.append(start)  # add start node to queue
        visited.append(start)  # mark start as visited

        while queue:
            current_node = queue.pop(0) # keep track of current node (pulled from queue)
            path = [current_node] # set current node as end of path
            if current_node == end:  
                break # break out of cycle if we reach the end
            else:
                for nbr in self.graph[current_node]:  # otherwise, loop through neighbors
                    if nbr not in visited: # ensure neighbor hasn't been visited
                        queue.append(nbr)
                        visited.append(nbr)
                        backtrace[nbr] = current_node  # keep track of this neihgbor's parent for pathfinding

        if end != None and end not in backtrace.keys():  # condition that there is an end node, but no path to it
            return None
        
        # otherwise, we will backtrace through the parent:child dictionary we created, starting with the
        # end node, or the end of the path (if no end node provided)

        while path[-1] != start:  # loop through until we reach the start node
            child_node = path[-1] # last in path
            parent_node = backtrace[child_node]  # find the current end of path node's parent
            path.append(parent_node)  # append to path
        
        shortest_path = path[::-1] # shortest path is the reverse of this 

        return shortest_path    
