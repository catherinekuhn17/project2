# write tests for bfs
import pytest
from search import graph

@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    G = graph.Graph('./data/tiny_network.adjlist')
    path = G.bfs('32353859;Atul', '30944313;Hani')
  #  print('hi')
  #  for i in range(1,len(path)-1):
  #      assert path[i-1] in G[path[i]].nbr # want to see if 
    assert ['32353859;Atul', 'Sirota', '30944313;Hani'] == path
    assert 1==3
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
    assert 1==1
    pass
