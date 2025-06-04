import numpy as np
from sympy import *

def christoffelSymbol(metric=["-1","0","0","0","0","1","0","0","0","0","1","0","0","0","0","1"], consts=["a", "b", "c"]):
    dim = sqrt(len(metric))
    matrix = Matrix(dim, dim, metric)
    invMatrix = matrix.inv()
    args = list(sympify(metric[0][0]).atoms(Symbol))
    
    for i in range(dim):
        for j in range(dim):
            newArgs = list(sympify(metric[dim*i+j]).atoms(Symbol))
            for x in newArgs:
                if x not in args:
                    args.append(x)
    
    print(matrix)
    print(args)
                
    
    

christoffelSymbol( [ "1","0","0","0", "r**2", "0", "0", "0", "(r**2)*(sin(t))**2" ] )



    


    
