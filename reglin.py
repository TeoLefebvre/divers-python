#!/usr/bin/env python
# coding: utf-8

# # Regression linéaire
# ## Import

# In[178]:


import numpy as np
from sklearn.datasets import make_regression
from matplotlib import pyplot as plt


# ## 1. Dataset

# In[179]:


# x, y = make_regression(n_samples=100, n_features=1, noise=10)

x = np.linspace(0, 100, 100)
y = x*0.1 + 1

y = y.reshape(len(y), 1)
x = x.reshape(len(x), 1)

y = y.reshape(y.shape[0], 1)

plt.scatter(x, y)
print(x.shape, y.shape)


# In[180]:


X = np.hstack((x, np.ones(x.shape)))
print(X.shape)

theta = np.random.randn(2,1)
print(theta.shape)


# ## 2. Model

# In[181]:


def model(X, theta):
    return X.dot(theta)

plt.scatter(x, y)
plt.plot(x, model(X, theta), c='r')
plt.show()


# ## 3. Cost function

# In[182]:


def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)


# ## 4. Gradients and Gradient Descent

# In[183]:


def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)


# In[184]:


def gradient_descent(X, y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    for i in range(0, n_iterations):
        theta = theta - learning_rate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history


# ## 5. Training phase

# In[185]:


learning_rate = 0.005
n_iterations = 1000
theta_final, cost_history = gradient_descent(X, y, theta, learning_rate, n_iterations)
predictions = model(X, theta_final)

plt.scatter(x, y)
plt.scatter(x, predictions, c='r')
plt.show()


# ## 6. Final evaluation

# In[186]:


plt.plot(range(1000), cost_history)
plt.show()


# In[187]:


def coeff_determination(y, prediction):
    u = ((y - predictions)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v


# In[188]:


print(coeff_determination(y, predictions))