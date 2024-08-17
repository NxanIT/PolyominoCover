import numpy as np # linear algebra
import pandas as pd

import init
from map import map
from flatshape import flatshape
def main():
    a = flatshape(3,3)
    x = a.get_flat_edges()
    Map = map([flatshape(5,5),flatshape(4,4),flatshape(3,3),flatshape(2,2),flatshape(1,1)])
    #print("x",len(x))
    print(Map.get_edges())
    print(Map.get_points())

    pass


if __name__ == "__main__":
    main()