import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("ml_lab4.csv")
print(data)

x = data.iloc[:, [1,2]].values
print(f"\nThe X values are : {x}")

y = data.iloc[:, -1].values
print(f"\nThe Y Values are : {y}")

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.4)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
result1 = classification_report(y_test, y_pred)
print(f"Classification Report - {result1}")

result2 = accuracy_score(y_test, y_pred)
print(f"Accuracy Score - {result2}")

result = confusion_matrix(y_test, y_pred)
print(f"Confusion Score - {result}")