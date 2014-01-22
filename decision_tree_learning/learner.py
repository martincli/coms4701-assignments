import math
import csv
import sys

#==================================
# Decision tree learning algorithm
# (textbook pg. 658, 2nd edition)
#==================================

def decisionTreeLearning(examples, attributes, default):
	if not examples:
		return default
	elif allSameClassification(examples):
		return examples[0].classification
	elif not attributes:
		return majorityValue(examples)
	else:
		best = chooseAttr(attributes, examples)
		tree = DecisionTree(best, {})
		m = majorityValue(examples)
		values = []
		for e in examples:
			currentVal = e.attributes[best]
			if currentVal not in values:
				values.append(currentVal)
		exs = {}
		for v in values:
			exs[v] = []
			for e in examples:
				if e.attributes[best] == v:
					exs[v].append(e)
			restOfAttrs = list(attributes)
			restOfAttrs.remove(best)
			subtree = decisionTreeLearning(exs[v], restOfAttrs, m)
			tree.subtrees[v] = subtree
		return tree

#================================
# Helper functions for algorithm
#================================

# Returns True if all given examples are the same classification, otherwise returns False
def allSameClassification(examples):
	first = examples[0].classification
	for e in examples[1:]:
		if e.classification != first:
			return False
	return True

# Returns the majority classification for given examples
def majorityValue(examples):
	counts = {}
	for e in examples:
		if e.classification in counts:
			counts[e.classification] += 1
		else:
			counts[e.classification] = 0
	return sorted(counts, key=counts.get, reverse=True)[0]

# Determine best attribute by information gain
def chooseAttr(attributes, examples):
	gainValues = {}
	entropy = 0
	classifications = {}
	for e in examples:
		if e.classification not in classifications.keys():
			classifications[e.classification] = 1
		else:
			classifications[e.classification] += 1
	for c in classifications.itervalues():
		entropyPart = -(float(c) / float(len(examples))) * math.log(float(c) / float(len(examples)), 2)
		entropy += entropyPart
	for a in attributes:
		gainValues[a] = entropy - remainder(a, examples)
	return sorted(gainValues, key=gainValues.get, reverse=True)[0]

# Remainder value, used for chooseAttr function
def remainder(attribute, examples):
	valuesDict = {}
	remainder = 0
	for e in examples:
		value = e.attributes[attribute]
		if value not in valuesDict.keys():
			valuesDict[value] = {}
		if e.classification not in valuesDict[value].keys():
			valuesDict[value][e.classification] = 1
		else:
			valuesDict[value][e.classification] += 1
	for v in valuesDict.keys():
		numClassifications = 0
		for val in valuesDict[v].itervalues():
			numClassifications += val
		for val in valuesDict[v].itervalues():
			remainderPart = (float(numClassifications) / float(len(examples))) * (-(float(val) / float(numClassifications) * math.log(float(val) / float(numClassifications), 2)))
			remainder += remainderPart
	return remainder

#==========
# Classes
#==========

# Class to parse examples
# attributes is a dictionary containing attribute-value pairs
# classification is taken from the last element of an example
class Example:
	def __init__(self, attributes={}, classification=None):
		self.attributes = attributes
		self.classification = classification

# Class for decision trees
# value is either an attribute (index by integers) or string value
# subtrees is a dictionary containing a node's children, where the keys are edge values (i.e. "none", "some", and "full" for the "patrons" attribute)
class DecisionTree:
	def __init__(self, value, subtrees):
		self.value = value
		self.subtrees = subtrees

#=========================
# Decision tree functions
#=========================

# Prints a decision tree (for testing purposes)
def printTree(tree):
	if type(tree) is str:
		print tree
	else:
		print tree.value
	print tree.subtrees
	print "======="
	for subtree in tree.subtrees.values():
		if type(subtree) is not str:
			printTree(subtree)

# Returns a copy of a decision tree
def copyTree(tree):
	currentNode = DecisionTree(tree.value, {})
	for edge, subtree in tree.subtrees.iteritems():
		currentNode.subtrees[edge] = subtree
		if type(subtree) is not str:
			copyTree(subtree)
	return tree

# Writes a decision tree to a single string (for classifier program)
def writeTree(tree):
	if type(tree) is str:
		return '\'' + tree + '\''
	edgeValues = []
	for edge, subtree in tree.subtrees.iteritems():
		edgeValues.append(edge)
	subtreeDict = '{'
	for edge in edgeValues:
		subtreeDict = subtreeDict + '\'' + edge + '\':' + writeTree(tree.subtrees[edge]) + ','
	subtreeDict = subtreeDict + '}'
	return 'DecisionTree(' + str(tree.value) + ',' + subtreeDict + ')'

#=============================================
# CSV parsing + generating classifier program
#=============================================

if __name__ == '__main__':
	examples = []

	# Parse CSV file and generate decision tree
	input = sys.argv[1]
	with open(input, 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			row = [item.strip() for item in row]
			attrs = {}
			i=0
			for value in row[:-1]:
				attrs[i] = value
				i += 1
			examples.append(Example(attrs, row[-1]))
	tree = decisionTreeLearning(examples, attrs.keys(), None)

	# Generate classifier program
	f = open('classifier.py', 'w')
	f.write('#=============================================\n')
	f.write('#        Generated classifier program\n')
	f.write('# To run: python classifier.py INPUT_FILE.csv\n')
	f.write('#=============================================\n\n')
	f.write('from learner import DecisionTree, copyTree\n')
	f.write('import csv\n')
	f.write('import sys\n\n')
	f.write('training = ' + writeTree(tree) + '\n\n')
	f.write('input = sys.argv[1]\n')
	f.write('with open(input, \'r\') as file:\n')
	f.write('	reader = csv.reader(file)\n')
	f.write('	for row in reader:\n')
	f.write('		row = [item.strip() for item in row]\n')
	f.write('		currentTree = copyTree(training)\n')
	f.write('		while type(currentTree) is not str:\n')
	f.write('			currentTree = currentTree.subtrees[row[currentTree.value]]\n')
	f.write('		print currentTree\n')