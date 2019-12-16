# Notes on Linear Classifiers and Generalizations

## Introduction on ML

Types of ML:
* supervised learning : learn from example. Provide data on desired output based on input
* unsuppervised learnign: no target given, just data. Algorythm learns by itself
* reinforsment learning: There is an objective nad the algorythm learns from own experience based on success/failure. 
This method is a combination of supervised and unsuppervised learning.

## Movie recommendation problem

Lets say that there is a dataset with all movies liked and disliked by ussers. Each movie can be represented by a 
feature vector of booleans defining its properties: (action, drama, studio, lead actors, etc)

x^(1) = [1 , 0 , 1 , 0 , 0 , 1 , ...]^T 

## Classifiers
Each classifier represents a possible hypothesis.
hypothesis space - set of possible classifiers

Types of learning:
* semi-supervised - supplement limited annotations
* active learning - learn to query the examples actually needed for learning
* transfer learning - applying the learned in A for B
* reinforcement learning - learn to act, not only predict. Goal is to optimize performance of actions.

## Linear classifier and precision

Goal is to find a vectore the normal to which is separating the space in sub-classes.
This line/surface is the decision boundary.

* Perception algorythm# Notes on Linear Classifiers and Generalizations

## Introduction on ML

Types of ML:
* supervised learning : learn from example. Provide data on desired output based on input
* unsupervised learning: no target given, just data. Algorithm learns by itself
* reinforcement learning: There is an objective and the algorithm learns from own experience based on success/failure. 
This method is a combination of supervised and unsupervised learning.

## Movie recommendation problem

Let’s say that there is a dataset with all movies liked and disliked by users. Each movie can be represented by a 
feature vector of Booleans defining its properties: (action, drama, studio, lead actors, etc)

x^(1) = [1 , 0 , 1 , 0 , 0 , 1 , ...]^T 

## Classifiers
Each classifier represents a possible hypothesis.
hypothesis space - set of possible classifiers

Types of learning:
* semi-supervised - supplement limited annotations
* active learning - learn to query the examples actually needed for learning
* transfer learning - applying the learned in A for B
* reinforcement learning - learn to act, not only predict. Goal is to optimize performance of actions.

## Linear classifier and precision

Goal is to find a vector the normal to which is separating the space in sub-classes.
This line/surface is the decision boundary.

* Perception algorithm
For each point it checks if it is on the "correct" side of the decision boundary. 
If it is not, it redefines the boundary, so it is normal to the vector going from the data point to old normal
(note to self, include equation/graph to make it easy to read)

Since the update of every point may change the result for all the rest, multiple iterations are necessary.

## Hinge loss , Margin boundaries and regularization

* margin boundary - the max normal distance between possible decision boundaries
* hinge loss - a function to maximize the margin boundary
* regularization - maximizing the decision boundary


For each point it checks if it is on the "correct" side of the decision bounday. 
If it is not, it redefines the boundary, so it is normal to the vector going from the data point to old normal
(note to self, iclude equation/graph to make it easy to read)

Since the update of every point may change the result for all the rest, ultiple iterations are necasery.

## Hinge loss , Margin boundaries and regularization

* margine boundary - the max normal bistance between possible decision boundaries
* hinge loss - a function to maximize the margine boundary
* regularization - maximizing the decision boundary

