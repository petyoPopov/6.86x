import numpy as np

### Functions for you to fill in ###



def polynomial_kernel(X, Y, c, p):
    """
        Compute the polynomial kernel between two matrices X and Y::
            K(x, y) = (<x, y> + c)^p
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            c - a coefficient to trade off high-order and low-order terms (scalar)
            p - the degree of the polynomial kernel

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    n = np.shape(X)[0]
    m = np.shape(Y)[0]
    
    #kernel_matrix = np.zeros(n,m)
    kernel_matrix = np.power( ((X @ np.transpose(Y)) + c) , p)
    
    try:
        return kernel_matrix
    except:
        raise NotImplementedError



def rbf_kernel(X, Y, gamma):
    """
        Compute the Gaussian RBF kernel between two matrices X and Y::
            K(x, y) = exp(-gamma ||x-y||^2)
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            gamma - the gamma parameter of gaussian function (scalar)

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    def single_rbf_kernel(x , y , gamma):
        """
        takes one row x, one row of y and computes the kernel
        """
        norm_value = np.power(np.linalg.norm(x-y) , 2)
        return np.exp(-norm_value * (1 * np.power(gamma , 1)))
    
    n = np.shape(X)[0]
    m = np.shape(Y)[0]
    kernel_matrix = np.zeros([n,m])
    
    for i in range(n):
        for j in range(m):
            kernel_matrix[i][j] = single_rbf_kernel(X[i,:] , Y[j,:] , gamma)
    
    try:
        return kernel_matrix
    except:
        raise NotImplementedError
