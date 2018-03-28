# Goals:
# Import dataset
# Train a Classifier
# Predict label for new flower
# Visualize the tree
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

iris = load_iris()
for i in range(len(iris.data)):
	print "Example %d, label: %s, features: %s" % (i, iris.target[i], iris.data[i])
test_idx = [0, 50, 100]
# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
for i in range(len(train_data)):
	print "Example2 %d, label: %s, features: %s" % (i, train_target[i], train_data[i])

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]	
for i in range(len(test_data)):
	print "Example2 %d, label: %s, features: %s" % (i, test_target[i], test_data[i])

#Step2: Train the Classifier using the Decision Tree classifier
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

#Step3: Predict lavel for new flower
print clf.predict(test_data)

#Step4: Visualize the Tree
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("iris.pdf")