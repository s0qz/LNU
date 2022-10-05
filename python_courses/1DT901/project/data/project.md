# Project Task

The project is about understanding hashing and binary search trees. We will use  the two large text files you used in Assignment 3 as input data. We strongly recommend that you look at Lecture 10 before you start to work on the project exercises.

The problem can be divided in three parts:

1. Count unique words using Python's set and dictionary
2. Implement two data structures suitable for working with words as data: a) A hash based set, and b) a binary search tree (BST) based map (dictionary). 
3. Use your two data structures to repeat Part 1 (counting unique words)

## Part 1 - Count unique words 1 

In Exercises 8 and 9 in Assignment 3 you saved all words from the two text files, one containing the script to Life of Brian and one for news items, in two separate files. (Do it now if you haven't done this exercise already) Your task here is to 

1. use Python's set class to count the number of unique words in each file 
2. use Python's dictionary class to produce a Top 10 list of the ten most frequently used words having a length larger than 4 in each file. 

In Part 3 you will repeat the same computations using your own hash and BST based implementations.

## Part 2 - Implementing data structures 

Lecture 10 outlines the basic ideas of two techniques suitable for implementing maps (dictionaries) and sets: **Binary search trees (BST)** and **Hashing**. Your task is to implement a _set_ (suitable for words) based on hashing and a _map_ based on binary search trees. 

Additional limitations:

* The BST based map is a linked implementation where each node has four fields (key, value, left-child, right-child). 
* The hash-based set is built using a Python list to store the buckets where each bucket is another Python list. The initial bucket list size is 8 and rehashing (double the bucket list size) takes place when the number of elements equals the number of buckets. 
* Furthermore, code skeletons outlining which methods we expect for each data structure are available [here](project_skeleton.zip). They also contains an example program showing how the various methods can be used.

**Notice:** You are not allowed to make any changes of the method signatures in the given skeletons. Also, the demo programs should work as outlined in the provided example programs once your implementations are complete. Your task is simply to complete the given code fragments in the skeletons. However, feel free to add additional methods. 

## Part 3 - Count unique words 2 

In this exercise you should basically repeat Part 1 using your own data structures rather than Python's. Using your hash based set and BST based map you should:

1. Count how many unique words that are used in the two given texts files using your **HashSet** implementation.
2. Present a list of the top-10 most frequently used words having a length larger than 4 using your **BstMap** implementation. 
3. What is the max bucket size for hash table after having added all words in the large text files (Life of Brian and News items respectively)?
4. What is the max depth of the BST when adding all words (as both key and value) from the large text files (Life of Brian and News items respectively)?

Notice: You are not allowed to use Python's set and dictionary classes to solve these problems. The results for the first two parts should be the same as in Part 1.

**Finally**, remember that writing the report takes a few days! Instructions for the report (a report  template) will be presented in a separate document.
