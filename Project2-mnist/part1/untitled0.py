# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 13:07:08 2019

@author: Petyo
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("..")

def closed_form(X, Y, lambda_factor):
    """
    Computes the closed form solution of linear regression with L2 regularization

    Args:
        X - (n, d + 1) NumPy array (n datapoints each with d features plus the bias feature in the first dimension)
        Y - (n, ) NumPy array containing the labels (a number from 0-9) for each
            data point
        lambda_factor - the regularization constant (scalar)
    Returns:
        theta - (d + 1, ) NumPy array containing the weights of linear regression. Note that theta[0]
        represents the y-axis intercept of the model and therefore X[0] = 1
    """
    # YOUR CODE HERE
    X_transpose = np.transpose(X)
    term_1 = np.invert(np.multiply(X_transpose,X)+lambda_factor*np.identity(np.shape(X)[1]))
    theta = np.multiply( term_1 , np.transpose(X))
    theta = np.multiply(theta , Y)
    
    
    try:
        return theta
    except:
        raise NotImplementedError
