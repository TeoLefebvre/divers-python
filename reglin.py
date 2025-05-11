## Imports

import numpy as np
from sklearn.datasets import make_regression
from matplotlib import pyplot as plt

## 1. Dataset

x, y = make_regression(n_samples=100, n_features=1, noise=10)
y = y.reshape(len(y), 1)
x = x.reshape(len(x), 1)
y = y.reshape(y.shape[0], 1)
print(x.shape, y.shape)

X = np.hstack((x, np.ones(x.shape)))
print(X.shape)

theta = np.random.randn(2,1)
print(theta.shape)

## 2. Model

def model(X, theta):
    return X.dot(theta)

plt.scatter(x, y, label='y')
plt.plot(x, model(X, theta), c='r', label='model')
plt.title('Model against real data before training')
plt.legend()
plt.grid()
plt.show()

## 3. Cost function

def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

## 4. Gradients and Gradient Descent

def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)

def gradient_descent(X, y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    for i in range(0, n_iterations):
        theta = theta - learning_rate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history

## 5. Training phase

learning_rate = 0.005
n_iterations = 1000
theta_final, cost_history = gradient_descent(X, y, theta, learning_rate, n_iterations)
predictions = model(X, theta_final)

plt.scatter(x, y, label='y')
plt.plot(x, predictions, c='r', label='model')
plt.legend()
plt.grid()
plt.title('Model against real data after training')
plt.show()

## 6. Final evaluation

plt.plot(range(n_iterations), cost_history)
plt.title('Cost history')
plt.show()

def coeff_determination(y, prediction):
    u = ((y - predictions)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

print(coeff_determination(y, predictions))