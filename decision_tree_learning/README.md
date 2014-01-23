COMS W4701 Artificial Intelligence<br/>
Project #4: Decision Tree Learning

Assignment
----------
The purpose of this assignment was to implement the ID3 algorithm to generate a decision tree from given training data. The decision tree can then be used to classify further data.

Introduction
------------
The program is written in Python version 2.7.
To run, first run the learner program (learner.py) with training data input:

    python learner.py TRAINING_DATA.csv

The program will generate a classifier program (classifier.py), which should be run with test data input:

    python classifier.py TEST_DATA.csv

This will output the classifier for each row (example) according to the algorithm.

Tests
-----
To use the training and test data that are provided:

    python learner.py restaurant2_train.csv
    python classifier.py restaurant2_test.csv

The following is the output:

    Yes
    No
    Maybe

This means that the classifier, using the decision tree generated from the training data, determined the classification for the first row in the test data to be 'Yes', the second to be 'No', and the third to be 'Maybe'.

<b>NOTE:</b> The included classifier.py file is the result of running learner.py on the provided training data. You may delete classifier.py and re-run learner.py to verify. Running learner.py on another training data file will overwrite classifier.py.