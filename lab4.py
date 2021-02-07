﻿# CSC531/BIF633/INT382 -- Week#4 Lab -- Proximity measures (Distance & Similarity)
# by...Chakarida NUKOOLKIT
#
# Instruction:    
#
# 1) Try to edit the given code with other proximity parameters such as 'cityblock', 'cosine'
# 'euclidean', 'manhattan', 'hamming', 'jaccard', 'mahalanobis', 'chebyshev', 'canbera', 'matching', ...
# 2) Guess/manually calculate the result
# 3) Run your code and compare the result
#
#
#  Question: Before you execute a run  of a new proximity measure, guess what you will get before you run it by 
#            manually calculate the outcome.  If Python returns different answer than yours, ask yourself why !!!
#
#  Challenge#1:  Try to change the value of your data, manually calculate the output measure, then execute your coresponding 
#                code and compare results with your previous manual calculation
#
#  Challenge#2:   Can you make a scatter plot of the given data before computing variety of distances/similarity measures
#
############################################################################






from sklearn.metrics import pairwise_distances
import numpy as np


# our lab data is in the small array/matrix called x
x= np.array ([[1, 2], [0, 3], [5, 7]])


# print the whole array X
print('x= ')
print(x)
# print the 1st row array
print('1st row of x= ')
print(x[0, :])


# print the 2nd row array
print('2nd row of x= ')
print(x[1, :])


# print the 3rd row array
print('3rd row of x= ')
print(x[2, :])


#get EuclideanDistance of a pair of 2 rows of x
print('euclidean =')
e = pairwise_distances(x, x, 'euclidean')
print(e)


#get ManhattanDistance of a pair of 2 rows of x
print('manhattan =')
m = pairwise_distances(x, x, 'manhattan')
print(m)


#get HammingDistance of a pair of 2 rows of x
print('Hamming =')
h = pairwise_distances(x, x, 'hamming')
print(h)


#get JaccardSimilarity of a pair of 2 rows of x
print('Jaccard= ')
j = pairwise_distances(x, x, 'jaccard')
print(j)


#get CosineSimilarity of a pair of 2 rows of x
print('Cosine= ')
c = pairwise_distances(x, x, 'cosine')
print(c)