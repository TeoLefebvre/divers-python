# Trace les lignes de champs pour un nombre fini de particules

import numpy as np
from matplotlib import pyplot as plt


def angle(x, y):
    theta = 0
    if x == 0:
        if y == 0:
            theta = 0
        elif y > 0:
            theta = np.pi / 2
        elif y < 0:
            theta = -np.pi / 2
    else:
        theta = np.arctan(y / x)

        if x < 0 and y >= 0:
            theta += np.pi
        elif x < 0 and y < 0:
            theta -= np.pi
    return theta


class Vecteur:
    def __init__(self, affixe):
        self.affixe = affixe
        self.x = affixe[0]
        self.y = affixe[1]

    def ajouter(self, vecteur):
        self.x += vecteur.x
        self.y += vecteur.y


class Particule:
    def __init__(self, q, coords):
        self.q = q
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]

    def champ(self, x, y):
        d = (self.x - x)**2 + (self.y - y)**2
        norme = self.q / d
        theta = angle(x - self.x, y - self.y)
        return Vecteur([np.cos(theta) * norme, np.sin(theta) * norme])


class Ldc:
    def __init__(self, origin, theta):
        self.origin = origin
        self.x = origin[0]
        self.y = origin[1]
        self.theta = theta

    def construire(self, P, pas, nb_pts):
        X = [self.x, self.x + np.cos(self.theta) * pas]
        Y = [self.y, self.y + np.sin(self.theta) * pas]

        for i in range(nb_pts):
            U = []
            for p in P:
                U.append(p.champ(X[-1], Y[-1]))
            E = Vecteur([0, 0])
            for u in U:
                E.ajouter(u)
            theta = angle(E.x, E.y)
            X.append(X[-1] + np.cos(theta) * pas)
            Y.append(Y[-1] + np.sin(theta) * pas)

        self.X, self.Y = X, Y


def main():
    nb_ldc = 30
    nb_pts = 50
    pas = 0.1
    L = []
    P = [Particule(1, [1, 2]), Particule(1, [3, 2]), Particule(-1, [2, 3])]
    P = [Particule(-1, (3, 1)), Particule(-2, (1, 3)), Particule(3, (1, 1.1)), Particule(1, (4, 4))]
    for p in P:
        if p.q > 0:
            for i in range(nb_ldc):
                theta = 2*np.pi * i / nb_ldc + 0.01
                L.append(Ldc(p.coords, theta))
            for l in L:
                l.construire(P, pas, nb_pts)
                plt.plot(l.X, l.Y, color='black')
    for p in P:
        if p.q > 0:
            plt.plot(p.x, p.y, 'p', color="r")
        else:
            plt.plot(p.x, p.y, 'p', color="b")

    plt.axis([-1,5,-1,5])
    plt.show()


main()
