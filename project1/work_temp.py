# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 05:27:23 2019

@author: Petyo
"""

from string import punctuation, digits
import numpy as np
import random

def hinge_loss_single(feature_vector, label, theta, theta_0):
    """
    Finds the hinge loss on a single data point given specific classification
    parameters.

    Args:
        feature_vector - A numpy array describing the given data point.
        label - A real valued number, the correct classification of the data
            point.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.


    Returns: A real number representing the hinge loss associated with the
    given data point and parameters.
    """
    # Your code here
    z = label*(np.dot(theta,feature_vector) + theta_0 )
    if z >= 1:
        hinge_loss = 0
    else:
        hinge_loss = 1 - z
    
    try:
        return hinge_loss
    except:
        raise NotImplementedError

def hinge_loss_full(feature_matrix, labels, theta, theta_0):
    """
    Finds the total hinge loss on a set of data given specific classification
    parameters.

    Args:
        feature_matrix - A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.


    Returns: A real number representing the hinge loss associated with the
    given dataset and parameters. This number should be the average hinge
    loss across all of the points in the feature matrix.
    """
    # Your code here
    
    rows = np.shape(feature_matrix)[0]
    hinge_loss = 0.0
    
    for i in range(rows):
        feature_vector_single = feature_matrix[i,:]
        label_single = labels[i]
        
        hinge_loss += hinge_loss_single(feature_vector_single, label_single, theta, theta_0)/rows
    
    hinge_loss_hull = hinge_loss
    try:
        return hinge_loss_hull
    except:
        raise NotImplementedError


def perceptron_single_step_update(
        feature_vector,
        label,
        current_theta,
        current_theta_0):
    """
    Properly updates the classification parameter, theta and theta_0, on a
    single step of the perceptron algorithm.

    Args:
        feature_vector - A numpy array describing a single data point.
        label - The correct classification of the feature vector.
        current_theta - The current theta being used by the perceptron
            algorithm before this update.
        current_theta_0 - The current theta_0 being used by the perceptron
            algorithm before this update.

    Returns: A tuple where the first element is a numpy array with the value of
    theta after the current update has completed and the second element is a
    real valued number with the value of theta_0 after the current updated has
    completed.
    """
    # Your code here
    
    if label*(np.dot(current_theta,feature_vector) + current_theta_0) <= 0:
        new_theta = current_theta + label*feature_vector
        new_theta_0 = current_theta_0 + label   
    else:
        new_theta = current_theta
        new_theta_0 = current_theta_0  
        
    new_parameters = (new_theta,new_theta_0)
        
    try:
        return new_parameters
    except:
        raise NotImplementedError



def perceptron(feature_matrix, labels, T):
    """
    Runs the full perceptron algorithm on a given set of data. Runs T
    iterations through the data set, there is no need to worry about
    stopping early.

    NOTE: Please use the previously implemented functions when applicable.
    Do not copy paste code from previous parts.

    NOTE: Iterate the data matrix by the orders returned by get_order(feature_matrix.shape[0])

    Args:
        feature_matrix -  A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        T - An integer indicating how many times the perceptron algorithm
            should iterate through the feature matrix.

    Returns: A tuple where the first element is a numpy array with the value of
    theta, the linear classification parameter, after T iterations through the
    feature matrix and the second element is a real number with the value of
    theta_0, the offset classification parameter, after T iterations through
    the feature matrix.
    """
    # Your code here
    n = np.shape(feature_matrix)[1]
    theta = np.zeros(n)
    theta_0 = 0
    
    for t in range(T):
        for i in get_order(feature_matrix.shape[0]):
            # Your code here
            feature_vector = feature_matrix[i,:]
            label = labels[i]
            
            parameters = perceptron_single_step_update(feature_vector,
                    label,
                    theta,
                    theta_0)
            
            theta = parameters[0]
            theta_0 = parameters[1]

    new_parameters = (theta,theta_0)
   
    try:
        return new_parameters
    except:
        raise NotImplementedError

def average_perceptron(feature_matrix, labels, T):
    """
    Runs the average perceptron algorithm on a given set of data. Runs T
    iterations through the data set, there is no need to worry about
    stopping early.

    NOTE: Please use the previously implemented functions when applicable.
    Do not copy paste code from previous parts.

    NOTE: Iterate the data matrix by the orders returned by get_order(feature_matrix.shape[0])


    Args:
        feature_matrix -  A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        T - An integer indicating how many times the perceptron algorithm
            should iterate through the feature matrix.

    Returns: A tuple where the first element is a numpy array with the value of
    the average theta, the linear classification parameter, found after T
    iterations through the feature matrix and the second element is a real
    number with the value of the average theta_0, the offset classification
    parameter, found after T iterations through the feature matrix.

    Hint: It is difficult to keep a running average; however, it is simple to
    find a sum and divide.
    """
    # Your code here
    r = np.shape(feature_matrix)[0] #row number
    n = np.shape(feature_matrix)[1] #col number
    theta = np.zeros(n)
    theta_0 = 0
    
    theta_sum = np.zeros(n)
    theta_0_sum = 0
    
    for t in range(T):
        for i in get_order(feature_matrix.shape[0]):
            # Your code here
            feature_vector = feature_matrix[i,:]
            label = labels[i]
            
            parameters = perceptron_single_step_update(feature_vector,
                    label,
                    theta,
                    theta_0)
            
            theta = parameters[0]
            theta_0 = parameters[1]
            
            theta_sum += theta
            theta_0_sum += theta_0
    
    theta_avg = (1/(T*r)*theta_sum)
    theta_0_avg = (1/(T*r)*theta_0_sum)

    new_parameters = (theta_avg,theta_0_avg)
   
    try:
        return new_parameters
    except:
        raise NotImplementedError
        
def pegasos_single_step_update(
        feature_vector,
        label,
        L,
        eta,
        current_theta,
        current_theta_0):
    """
    Properly updates the classification parameter, theta and theta_0, on a
    single step of the Pegasos algorithm

    Args:
        feature_vector - A numpy array describing a single data point.
        label - The correct classification of the feature vector.
        L - The lamba value being used to update the parameters.
        eta - Learning rate to update parameters.
        current_theta - The current theta being used by the Pegasos
            algorithm before this update.
        current_theta_0 - The current theta_0 being used by the
            Pegasos algorithm before this update.

    Returns: A tuple where the first element is a numpy array with the value of
    theta after the current update has completed and the second element is a
    real valued number with the value of theta_0 after the current updated has
    completed.
    """
    # Your code here
    
    if label*(np.dot(current_theta , feature_vector)+current_theta_0) <= 1:
        new_theta = (1-eta*L)*current_theta + eta*label*feature_vector
        new_theta_0 = current_theta_0 + eta*label
    else:
        new_theta = (1-eta*L)*current_theta
        new_theta_0 = current_theta_0
    
    
    
    
    new_parameters = (new_theta,new_theta_0)
        
    try:
        return new_parameters
    except:
        raise NotImplementedError


def pegasos(feature_matrix, labels, T, L):
    """
    Runs the Pegasos algorithm on a given set of data. Runs T
    iterations through the data set, there is no need to worry about
    stopping early.

    For each update, set learning rate = 1/sqrt(t),
    where t is a counter for the number of updates performed so far (between 1
    and nT inclusive).

    NOTE: Please use the previously implemented functions when applicable.
    Do not copy paste code from previous parts.

    Args:
        feature_matrix - A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        T - An integer indicating how many times the algorithm
            should iterate through the feature matrix.
        L - The lamba value being used to update the Pegasos
            algorithm parameters.

    Returns: A tuple where the first element is a numpy array with the value of
    the theta, the linear classification parameter, found after T
    iterations through the feature matrix and the second element is a real
    number with the value of the theta_0, the offset classification
    parameter, found after T iterations through the feature matrix.
    """
    # Your code here
    n = np.shape(feature_matrix)[1]
    theta = np.zeros(n)
    theta_0 = 0
    
    step = 1
    
    for t in range(T):
       
        
        for i in get_order(feature_matrix.shape[0]):
            # Your code here
            feature_vector = feature_matrix[i,:]
            label = labels[i]
            
            eta = 1/np.sqrt(step)
            
            parameters = pegasos_single_step_update(
                    feature_vector,
                    label,
                    L,
                    eta,
                    theta,
                    theta_0)
            
            theta = parameters[0]
            theta_0 = parameters[1]
            step += 1

    new_parameters = (theta,theta_0)
   
    try:
        return new_parameters
    except:
        raise NotImplementedError








def classify(feature_matrix, theta, theta_0):
    """
    A classification function that uses theta and theta_0 to classify a set of
    data points.

    Args:
        feature_matrix - A numpy matrix describing the given data. Each row
            represents a single data point.
                theta - A numpy array describing the linear classifier.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.

    Returns: A numpy array of 1s and -1s where the kth element of the array is
    the predicted classification of the kth row of the feature matrix using the
    given theta and theta_0. If a prediction is GREATER THAN zero, it should
    be considered a positive classification.
    """
    # Your code here
    
    rows = np.shape(feature_matrix)[0]
    estimates = np.array([])
    
    for i in range(rows):
        x = feature_matrix[i,]
        
        y_est = np.dot(theta, x) + theta_0
        
        if y_est > 2**(-54):
            y_est = np.array([1])
        else:
            y_est = np.array([-1])
        
        estimates = np.append(estimates,y_est)
    
    try:
        return estimates
    except:
        raise NotImplementedError


def classifier_accuracy(
        classifier,
        train_feature_matrix,
        val_feature_matrix,
        train_labels,
        val_labels,
        **kwargs):
    """
    Trains a linear classifier and computes accuracy.
    The classifier is trained on the train data. The classifier's
    accuracy on the train and validation data is then returned.

    Args:
        classifier - A classifier function that takes arguments
            (feature matrix, labels, **kwargs) and returns (theta, theta_0)
        train_feature_matrix - A numpy matrix describing the training
            data. Each row represents a single data point.
        val_feature_matrix - A numpy matrix describing the training
            data. Each row represents a single data point.
        train_labels - A numpy array where the kth element of the array
            is the correct classification of the kth row of the training
            feature matrix.
        val_labels - A numpy array where the kth element of the array
            is the correct classification of the kth row of the validation
            feature matrix.
        **kwargs - Additional named arguments to pass to the classifier
            (e.g. T or L)

    Returns: A tuple in which the first element is the (scalar) accuracy of the
    trained classifier on the training data and the second element is the
    accuracy of the trained classifier on the validation data.
    """
    # Your code here
    
    theta, theta_0 = classifier(train_feature_matrix , train_labels , **kwargs)
    train_classy = classify(train_feature_matrix, theta, theta_0)
    accu_train = accuracy(train_classy, train_labels)
    
    val_classy = classify(val_feature_matrix, theta, theta_0)
    accu_val = accuracy(val_classy, val_labels)
    
    result_tuple = (accu_train , accu_val)
    
    try:
        return result_tuple
    except:
        raise NotImplementedError




















