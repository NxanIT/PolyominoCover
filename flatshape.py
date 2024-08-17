import numpy as np
class flatshape:
    def __init__(self,a,b,filled = True) -> None:
        if(filled == True):
            filled = np.ones((a,b),dtype=int)
        self.flatarray = filled
        self.a = a
        self.b = b
        pass
    def get_neighbouring_edges_indizes(self):
        L = []
        shape = self.flatarray.shape
        for dir in range(2):
            for i,j in np.ndindex(tuple((shape)-1*np.array([dir==0,dir==1],dtype=int))):
                if(self.flatarray[i,j] == 1 and self.flatarray[i+1*(dir==0),j+1*(dir==1)]):
                    L.append([(i,j),(i+1*(dir==0),j+1*(dir==1))])
        return np.array(L)
    def get_flat_edges(self,startIndex = 0):
        L = self.get_neighbouring_edges_indizes()
        A = []
        for edge in L:
            point1 = edge[0]
            point2 = edge[1]
            A.append(set({startIndex+point1[0] + self.a*point1[1],startIndex+point2[0] + self.a*point2[1]}))
        return A
    def get_length(self):
        return self.a * self.b
    def get_shape(self):
        return (self.a,self.b)
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def is_available(self,i,j):
        return 1*self.flatarray[i,j]==1
    

    def __str__(self) -> str:
        return np.array2string(self.flatarray)
    def __repr__(self) -> str:
        return self.flatarray