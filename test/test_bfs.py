# write tests for bfs
import pytest
from search import graph

#@pytest.fixture --> was causing me issues
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    G = graph.Graph('./data/tiny_network.adjlist')
    path = G.bfs('31806696', 'Neil Risch')
    # testing on a known path, to see if the shortest path given is the actual shortest path.
    assert path == ['31806696', 'Luke Gilbert', '31626775', 'Neil Risch']
    
    # asserting that each node in the path is a neighbor of the node to the left --> to make sure
    # that a real path is created (added nbr method to allow for this)
    for i in range(1, len(path)-1):
        assert path[i] in G.nbr(path[i-1])
        
    pass

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    G = graph.Graph('./data/citation_network.adjlist')
    
    # testing on a prior known path, to see if the shortest path given is the actual shortest path.
    path = G.bfs('30727954', 'Yin Shen')
    assert path == ['30727954', 'Michael McManus', '32728249', 'Yin Shen']
    # ensuring nodes are connected
    for i in range(1, len(path)-1):
        assert path[i] in G.nbr(path[i-1])
    
    # testing on a case where nodes not connected (and so should return None)
    path = G.bfs('34599200', 'Vasilis Ntranos')
    assert path == None
    
    # testing on if no end node specified - here, I am creating the path that records all the nodes traversed, and showing
    # that for each node in the path, all of it's neighbors are recorded in the traversal and were visited
    path = G.bfs('31712683', end = None)
   
    for i in range(1, len(path)-1): # to test all nodes are visited
        for n in G.nbr(path[i-1]):
            assert n in path
    pass
