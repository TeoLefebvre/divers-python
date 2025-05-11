# Imports
import numpy as np
import matplotlib.pyplot as plt

# Triangle ABC
A = np.array([2, 0])
B = np.array([-2, 2])
C = np.array([2, -2])

# Calculs des grandeurs
a = np.linalg.norm(B - C) # distance BC
b = np.linalg.norm(A - C) # distance AC
c = np.linalg.norm(A - B) # distance AB
p = a + b + c # périmètre
I = (a*A + b*B + c*C)/p # centre du cercle inscrit
r = np.sqrt((a+b-c)*(a-b+c)*(-a+b+c)/4/(a+b+c)) # rayon
s = r*p/2 # surface du triangle

# Droites et cercle pour tracer
AB = np.vstack((A, B))
BC = np.vstack((B, C))
AC = np.vstack((A, C))
theta = np.linspace(0,2*np.pi,100)
CI = np.array([I + r*np.array([np.cos(t), np.sin(t)]) for t in theta])

# Tracé de la figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.plot(*AB.T, color='r')
ax.plot(*AC.T, color='r')
ax.plot(*BC.T, color='r')
ax.scatter(*A, color='b')
ax.scatter(*B, color='b')
ax.scatter(*C, color='b')
ax.scatter(*I, color='b')
ax.plot(*CI.T)
plt.show()