# Digit recognition (Part 1)

## Data
MNIST database contains binary images of handwritten digits commonly used to train image processing systems. 
The digits were collected from among Census Bureau employees and high school students. 
The database contains 60,000 training digits and 10,000 testing digits, all of which have been size-normalized and centered in a 
fixed-size image of 28 × 28 pixels.

## Used libraries
* scikit-learn
* numPy
* matplotlib

(scikit-learn can solve this problem in a few lines of code, but since this is a learning exercise, an algorithm  using numpy will be made)

## Files:

* linear_regression.py - implement linear regression
* svm.py - implement support vector machine
* softmax.py - multinomial regression
* features.py - principal component analysis (PCA) dimensionality reduction
* kernel.py - polynomial and Gaussian RBF kernels
* main.py - the code you write for this part of the project


# Digit recognition (Part 2)

The setup is the same as for Part 1, but Neural Networks algorithm shall be used.

## Files:

* part2-nn/neural_nets.py - for my first neural net from scratch
* part2-mnist/nnet_fc.py  - for PyTorch to classify MNIST digits
* part2-mnist/nnet_cnn.py - add convolutional layers to boost performance
* part2-twodigit/mlp.py   - for a new, more difficult version of the MNIST dataset
* part2-twodigit/cnn.py   - for a new, more difficult version of the MNIST dataset

