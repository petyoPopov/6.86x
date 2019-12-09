# Automati Review Analyzer
## Using Linear Classifiers and Generalizations

The goal of this project is to design a classifier to use for sentiment analysis of 
product reviews. The training set consists of reviews written by Amazon customers for 
various food products. The reviews, originally given on a 5 point scale, have been 
adjusted to a +1 or -1 scale, representing a positive or negative review, respectively.


In order to automatically analyze reviews the following tasks need to completed :

* Implement and compare three types of linear classifiers:
  * the perceptron algorithm
  * the average perceptron algorithm
  * the Pegasos algorithm

* Use these classifiers on the food review dataset, using some simple text features.
* Experiment with additional features and explore their impact on classifier performance.


The course organizers provide a structure of the code. My tasks was to develop the necessary functions, knowing 
what is the input and output of a function. Here is the file structure of the project: 

* project1.py contains various useful functions and function templates that you will use to implement your learning algorithms.
* main.py is a script skeleton where these functions are called and you can run your experiments.
* utils.py contains utility functions that __the staff has implemented for you__.
* test.py is a script which runs tests on a few of the methods you will implement. __It is entirely made by course staff.__
