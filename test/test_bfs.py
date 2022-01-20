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
   
    for i in range(1, len(path)-1): # to test all neighbors of nodes are visited
        for n in G.nbr(path[i-1]):
            assert n in path
    # also wanted to test the no end case on a known output (to not rely on the other method I created) 
    path = G.bfs('Rima Arnaout', end = None)
    assert path == ['Rima Arnaout', '34957251','34957230', '34948215','34945766','34919578','34912531','34883951','34863912', '34858707', '34857095', '34842542', '34828343', '34822377', '34821702', '34778259', '34768802','34765602','34754399','34754270','34745504','34742250','34728938','34722674','34681282','34680411','34680109','34650705','34646912','34645908','34611787','34600518','34600492','34599422','34585237','34577530','34557935','34548574','34533278','34522872','34522840','34513890','34512719','34489704','34465714','34458408','34445174','34442391','34428931','34426417','34422842','34422841', '34416899','34408248', '34397091', '34393777','34378773','34338756','34327238','34318510','34316068', '34307493','34295713','34279636','34274276','34228702','34214626','34209538','34207293','34203532','34201827','34199828','34179682', '34179218','34152269','34149617','34142884','34134641','34116660', '34104894', '34095129', '34080347', '34074030', '34073947', '34067554', '34063324', '34062899', '34050491', '34019817', '33994301', '33990806', '33986900', '33982075', '33952614','33950154', '33930310','33924375', '33918756', '33917701', '33897409', '33895824', '33478654', '32912474', '31325067', '31308376']
    pass
