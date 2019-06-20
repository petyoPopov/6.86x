import numpy as np

def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    A=np.random.random([n,1])
    try:
        return A
    except:
        raise NotImplementedError

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    A=np.random.random([h,w])
    B=np.random.random([h,w])
    s=np.add(A,B)
    
    try:
        return A,B,s
    except:
        raise NotImplementedError

def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    s=np.add(A,B)
    s= np.linalg.norm(s)
    try:
        return s
    except:
        raise NotImplementedError


def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    out=np.sum(inputs*weights)
    out=np.tanh(out)
    out=out*np.ones((1,1))
    out=np.array(out)
    try:
        return out
    except:
        raise NotImplementedError
