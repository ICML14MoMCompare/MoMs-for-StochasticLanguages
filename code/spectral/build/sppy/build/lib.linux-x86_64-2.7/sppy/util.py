import numpy 
from sppy import csarray 

"""
Some utility function to create sparse arrays. 
"""


def diag(x): 
    """
    From a 1D numpy array x create a diagonal sparse array. 
    """
    result = csarray((x.shape[0], x.shape[0]), x.dtype)
    result[(numpy.arange(x.shape[0]), numpy.arange(x.shape[0]))] = x
    
    return result 
    
    
def eye(n, dtype=numpy.float):
    """
    Create the identity matrix of size n. 
    """
    
    result = diag(numpy.ones(n, dtype=dtype))
    return result 
    
def rand(shape, density, dtype=numpy.float): 
    """
    Generate a random sparse matrix with m rows and n cols with given density 
    and dtype. 
    """
    result = csarray(shape, dtype)
    size = result.size
    numEntries = int(size*density)
    
    inds = numpy.random.randint(0, size, numEntries)
    
    if result.ndim == 2: 
        rowInds, colInds = numpy.unravel_index(inds, shape)    
        result[rowInds, colInds] = numpy.random.rand(numEntries)
    elif result.ndim == 1: 
        result[inds] = numpy.random.rand(numEntries)
    
    return result 
    

def zeros(shape, dtype=numpy.float, storageType="col"): 
    """
    Create a zeros matrix of the given shape and dtype. 
    """
    result = csarray(shape, dtype, storageType)
    return result
    
def ones(shape, dtype=numpy.float, storageType="col"): 
    """
    Create a ones matrix of the given shape and dtype. Generally a bad idea 
    for large matrices. 
    """
    result = csarray(shape, dtype, storageType)
    result.ones()
    return result

#def solve(A, b): 
    """
    Solve a system of linear equations given by Ax = b.  
    """
    
    
