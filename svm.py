'''
The linear discriminant function for a binary classification problem with three features is
the plane defined by the equation 3x1 + 2x2 + 4x3 = 18, where the features are x1, x2, and *3. The discriminant plane separates the positive hypotheses (3x1 + 2x2 + 4x3 ≥ 18) from
the negative hypotheses (3x1 + 2x2 + 4x3 < 18).

The training set consists of the following labeled examples:
x1 x2 x3 y
2, 2, 3, +
3, 3, 2, +
1, 2, 3, +
1, 4, 1, +
4, 4, 4, +
2, 2, 2, +
3, 3, 1, -
1, 1, 1, -
3, 3, 2, -
0, 4, 2, -
4, 0, 0, -
0, 0, 3, -

find, a) margin, b) 0-1 loss, c) hinge loss, d) squared loss (clamped to zero above 1)
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import zero_one_loss
from sklearn.metrics import hinge_loss
from sklearn.metrics import mean_squared_error
from sklearn import svm
from sklearn.metrics import confusion_matrix

# Training set
X = np.array([[2, 2, 3], [3, 3, 2], [1, 2, 3], [1, 4, 1], [4, 4, 4], [2, 2, 2], [3, 3, 1], [1, 1, 1], [3, 3, 2], [0, 4, 2], [4, 0, 0], [0, 0, 3]])
y = np.array([1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1])

# Create a linear SVM classifier
clf = svm.SVC(kernel='linear', C=1e10)
clf.fit(X, y)

# Get the separating hyperplane
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (clf.intercept_[0]) / w[1]

# Plot the parallels to the separating hyperplane that pass through the support vectors
b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

# Plot the line, the points, and the nearest vectors to the plane
plt.plot(xx, yy, 'k-')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')

plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)

plt.axis('tight')
plt.show()

# Margin
margin = 2 / np.sqrt(np.sum(clf.coef_ ** 2))
print("Margin: ", margin)

# 0-1 loss
y_pred = clf.predict(X)
print("0-1 loss: ", zero_one_loss(y, y_pred))

# Hinge loss
print("Hinge loss: ", hinge_loss(y, y_pred))

# Squared loss
print("Squared loss: ", mean_squared_error(y, y_pred))

exit(0)

