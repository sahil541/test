# -*- coding: utf-8 -*-
"""decision_tree(8).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16mlIum6fNy4nv_hxJxNcNapSy1LjQjUV
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = load_iris()
print('Classes to predict: ', data.target_names)

X = data.data
y = data.target
print('Number of examples in the data:', X.shape[0])

X[:4]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 47, test_size = 0.25)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion = 'entropy')
clf.fit(X_train, y_train)

y_pred =  clf.predict(X_test)
from sklearn.metrics import accuracy_score
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train)))
print('Accuracy Score on test data: ', accuracy_score(y_true=y_test, y_pred=y_pred))
clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
clf.fit(X_train, y_train)
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train)))
print('Accuracy Score on the test data: ', accuracy_score(y_true=y_test, y_pred=clf.predict(X_test)))