import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def image(a):
    l, c = a.shape
    b = np.zeros((l, c, 3), dtype="float")
    for i in range(l):
        for j in range(c):
            if a[i, j]:
                b[i, j] = np.array([0, 0, 0])
            else:
                b[i, j] = np.array([1, 1, 1])
    return b


def grille(l, c):
    return np.zeros((l+2, c+2), dtype="bool")


def quadrillage(l, c):
    a = grille(l, c)
    for i in range(1, l+1):
        for j in range(1, c+1):
            a[i, j] = (i + j) % 2
    return a


def voisins(a, index):
    i, j = index
    D = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    s = 0
    for d in D:
        s += a[i+d[0], j+d[1]]
    return s


def regle(a):
    l, c = a.shape
    b = np.zeros((l, c), dtype="bool")
    for i in range(1, l-1):
        for j in range(1, c-1):
            v = voisins(a, (i, j))
            if a[i, j]:
                b[i, j] = (v == 2 or v == 3)
            else:
                b[i, j] = (v == 3)
    return b


def naissance(a, cellule):
    i, j = cellule
    a[i+1, j+1] = 1


def mort(a, cellule):
    i, j = cellule
    a[i+1, j+1] = 1


l, c = 20, 20
a = grille(l, c)
n = 10
dt = 100

# ligne droite
# for i in range(5):
#     naissance(a, (8, 10+i))

# planeur
naissance(a, (3, 2))
naissance(a, (3, 3))
naissance(a, (3, 4))
naissance(a, (2, 4))
naissance(a, (1, 3))


fig = plt.figure()
ax = plt.axes(xlim=(0, l), ylim=(0, c))
plt.axis("on")
im = ax.imshow(image(a))


def init():
    im.set_data(image(a))
    return im,


def animate(i):
    global a, im
    a = regle(a)
    im.set_data(image(a))
    return im,


anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=n, interval=dt, blit=True)
anim.save('animation.mp4', fps=2, extra_args=['-vcodec', 'libx264'])

plt.show()
