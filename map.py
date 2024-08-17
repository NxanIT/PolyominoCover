import numpy as np

class map:

    nodes = []

    def __init__(self,shape:np.array,between_layer_mode = 0) -> None:
        """input:   shape - np.array, each entry corresponds to one layer, dtype = flatshape
                    between_layer_mode - int, 0 for TODO:
        """
        self.shape = shape

        between_layer_connections = []
        if(between_layer_mode==0):
            between_layer_connections = [(-1,-1),(-1,0),(0,-1),(0,0)]
        edges = []
        number_of_nodes = 0
        for layermap in shape:
            edges += layermap.get_flat_edges(startIndex = number_of_nodes)
            number_of_nodes += layermap.get_length()
        
        
        self.nodes = np.arange(0,number_of_nodes)
        layer_starting_index = 0
        for index in range(len(shape)-1):
            Lower = shape[index]
            Upper = shape[index+1]
            next_layer_starting_index = layer_starting_index +Lower.get_shape()[0]*Lower.get_shape()[1]
            for i,j in np.ndindex(Lower.get_shape()):
                if(Lower.is_available(i,j)):
                    for shift_index in between_layer_connections:
                        upper_i = i + shift_index[0]
                        upper_j = j+ shift_index[1]
                        if(upper_i>=Upper.get_a() or upper_j>=Upper.get_b() or upper_i<0 or upper_j<0):
                            continue
                        if(Upper.is_available(upper_i,upper_j)):
                            edges.append({layer_starting_index + Lower.get_shape()[0]*j + i,next_layer_starting_index+ Upper.get_shape()[0]*j + i})
            layer_starting_index = next_layer_starting_index
        self.edges = edges
        pass


    def get_edges(self):
        return self.edges
    def get_nodes(self):
        return self.nodes
    
    def __repr__(self):
        L = []
        for layer in self.shape:
            L.append(layer.__repr__())
        return L
    def __str__(self):
        S = ""
        for layer in self.shape:
            S += "\n" + (layer.__str__())
        return S
    def get_points(self):
        L = []
        startIndex = 0
        for layer in self.shape:
            a = layer.get_a()
            b = layer.get_b()
            stopIndex = startIndex + a*b
            la = np.arange(startIndex,stopIndex).reshape((a,b))
            L.append(la)
            startIndex = stopIndex
        return L