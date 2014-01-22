#=============================================
#        Generated classifier program
# To run: python classifier.py INPUT_FILE.csv
#=============================================

from learner import DecisionTree, copyTree
import csv
import sys

training = DecisionTree(0,{'None':'No','Full':DecisionTree(7,{'10-30':'Yes','30-60':'Yes','0-10':'No','>60':DecisionTree(2,{'Nope':'Yes','Yeah':DecisionTree(4,{'$$':'Maybe','$':'No','$$$':DecisionTree(5,{'Nope':'No','Yeah':'Maybe',}),}),}),}),'Some':DecisionTree(4,{'$$':'Yes','$':DecisionTree(2,{'Nope':'Yes','Yeah':'Maybe',}),'$$$':'Yes',}),})

input = sys.argv[1]
with open(input, 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		row = [item.strip() for item in row]
		currentTree = copyTree(training)
		while type(currentTree) is not str:
			currentTree = currentTree.subtrees[row[currentTree.value]]
		print currentTree
