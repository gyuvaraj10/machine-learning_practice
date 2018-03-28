# The technique to write the classifier automatically is called supervised learning
# Supervised Learning: Create a classifer by finding patterns in examples
# Start with Scikit
# Supervised Learning
# Step1: Collect Training Data
# Step2: Train Classifier
# Step3: Make Predictions

import sklearn
from sklearn import tree
#Step1: Collect Training data
#features are the input to the classifer
features=[[140, 1], [130, 1],[150, 0],[170, 0]] #1 for smooth, 0 for bumpy
#labels are the output we want
labels=[0,0,1,1] # 0 for apple, 1 for oranle
#Step2: use these example to train the classifier
#The type of classifier we start with is called Decision Tree
#Classifier is a box of rules
#To train the classifier we need a learning algoritham. 
#Learning alogorithm is a procedure that creates classifiers and
#it does by creating the patterns from the training data
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels) # fit = find patterns in the data
print clf.predict([[110, 0]])



