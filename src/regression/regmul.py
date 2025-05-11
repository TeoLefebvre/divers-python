## Regression multiple

## Imports

import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression

## Dataset

x, Y = make_regression(n_samples=100, n_features=2, noise=10)
Y = Y.reshape((len(Y), 1))
print(x.shape, Y.shape)

plt.scatter(x[:,0], Y)
plt.title('Data (first dim)')
plt.show()

plt.scatter(x[:,1], Y)
plt.title('Data(second dim)')
plt.show()

## Model

def model(X, theta):
    return X.dot(theta)

X = np.hstack((x, np.ones((len(x), 1))))
theta = np.random.randn(3,1)
print(X.shape, theta.shape)

plt.scatter(x[:,0],Y)
plt.scatter(x[:,0], model(X, theta), c='r')
plt.title('Model against data before training')
plt.show()

## Cost function

def cost_function(X, Y, theta):
    return np.sum((model(X, theta) - Y)**2) / (2*len(Y))

## Gradient descent

def grad(X, Y, theta):
    return X.T.dot(model(X, theta) - Y) / len(Y)

def gradient_descent(X, Y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    theta_f = np.copy(theta)
    for i in range(n_iterations):
        theta_f -= learning_rate * grad(X, Y, theta_f)
        cost_history[i] = cost_function(X, Y, theta_f)
    return theta_f, cost_history

## Machine learning

learning_rate = 0.005
n_iterations = 1000
theta_final, cost_history = gradient_descent(X, Y, theta, learning_rate, n_iterations)
prevision = model(X, theta_final)
print(theta_final)

plt.figure(3)
plt.scatter(x[:,0], Y)
plt.scatter(x[:,0], model(X, theta_final), c='r')
plt.title('Model against data after training')
plt.show()

## Verifications

def r_carre(y, prevision):
    u = ((y - prevision)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

print(r_carre(Y, prevision))

plt.plot(range(20, n_iterations), cost_history[20:])
plt.title('Cost history')
plt.show()

## 3D representation

fig = plt.figure(5)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[:,0].reshape((100,1)), x[:,1].reshape((100,1)), Y)
ax.scatter(x[:,0].reshape((100,1)), x[:,1].reshape((100,1)), model(X, theta_final))
plt.show()