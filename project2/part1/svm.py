import numpy as np
from sklearn.svm import LinearSVC


### Functions for you to fill in ###

def one_vs_rest_svm(train_x, train_y, test_x):
    """
    Trains a linear SVM for binary classifciation

    Args:
        train_x - (n, d) NumPy array (n datapoints each with d features)
        train_y - (n, ) NumPy array containing the labels (0 or 1) for each training data point
        test_x - (m, d) NumPy array (m datapoints each with d features)
    Returns:
        pred_test_y - (m,) NumPy array containing the labels (0 or 1) for each test data point
    """
    lin_clf = LinearSVC(random_state=0 , C=0.1)
    lin_clf.fit(train_x,train_y)
    test_y_predict = lin_clf.predict(test_x)
        
    try:
        return test_y_predict
    except:
        raise NotImplementedError


def multi_class_svm(train_x, train_y, test_x):
    """
    Trains a linear SVM for multiclass classifciation using a one-vs-rest strategy

    Args:
        train_x - (n, d) NumPy array (n datapoints each with d features)
        train_y - (n, ) NumPy array containing the labels (int) for each training data point
        test_x - (m, d) NumPy array (m datapoints each with d features)
    Returns:
        pred_test_y - (m,) NumPy array containing the labels (int) for each test data point
    """
    lin_clf = LinearSVC(random_state=0 , C=0.1)
    lin_clf.fit(train_x,train_y)
    test_y_predict = lin_clf.predict(test_x)
        
    try:
        return test_y_predict
    except:
        raise NotImplementedError


def compute_test_error_svm(test_y, pred_test_y):
    term_1 = (theta @ np.transpose(X)) / temp_parameter
    #print("term_1\n",term_1)
    c = np.max(term_1 , 0)
    #print("c: \n", c)
    term_1 = np.exp(term_1 - c)
    scale_coef = np.sum(term_1,0)
    scale_coef = 1 / scale_coef
    #scale_coef = scale_coef[:, np.newaxis]
    n = np.shape(scale_coef)[0]
    scale_coef = scale_coef.reshape((n))
    
    H = scale_coef * term_1
    #print("scale", scale_coef)
    #print("scale shape", np.shape(scale_coef))
    #print("term_1", term_1)
    
    
    try:
        return H
    except:
        raise NotImplementedError
