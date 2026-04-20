import numpy as np

class hopfield_network:

    def __init__(self, num_of_node):

        self.number = num_of_node
        self.rng = np.random.default_rng()
        probability = self.random(size = None)
        self.nodes = self.rng.binomial(sel.number, probability)
        self.synapse = np.zeros(shape = (self.number, self.number))
        
    def update_synapse(self):
        """ This function supposed 
        """
        mask = np.eye((self.number, self.number), dtype = bool)
        self.synapse = np.outer(self.nodes, self.nodes)
        self.synapse[mask] = 0
        
        
        
    def update_nodes(self):
        """ This function supposed 
        """
        
        
        
        