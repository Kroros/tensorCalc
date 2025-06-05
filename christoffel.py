import numpy as np
from sympy import *

def christoffelSymbol(metric=[["-1","0","0","0"],["0","1","0","0"],["0","0","1","0"],["0","0","0","1"]],vars=None, consts=["a", "b", "c"]):
    metric = np.reshape(metric, np.shape(metric)[0]*np.shape(metric)[1])
    dim = sqrt(len(metric))
    matrix = Matrix(dim, dim, metric)
    invMatrix = matrix.inv()
    if vars is None:
        symbs = list(sympify(metric[0][0]).atoms(Symbol))
        for i in range(dim):
            for j in range(dim):
                newArgs = list(sympify(metric[dim*i+j]).atoms(Symbol))
                for x in newArgs:
                    if x not in symbs:
                        symbs.append(x)
        symbs = tuple(symbs)
    else:
        symbs = symbols(vars)
    
    chrSymbl = np.full((dim, dim, dim), S(0), dtype=object)
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for l in range(dim):
                    chrSymbl[i][j][k] = Add(chrSymbl[i][j][k], (1/2) * invMatrix[i, l] * (diff(matrix[l, k], symbs[j]) + diff(matrix[j, l], symbs[k]) - diff(matrix[j, k], symbs[l])), evaluate=False)
                    
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                chrSymbl[i][j][k] = simplify(chrSymbl[i][j][k])
                
    return chrSymbl
    
print(christoffelSymbol( [ ["1","0","0"], ["0", "r**2", "0"], ["0", "0", "(r**2)*(sin(t))**2"] ], vars="r theta phi" ))




    


    
