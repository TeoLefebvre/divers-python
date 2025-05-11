# Trace une carte de champs

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
        if d == 0:
            norme = 0
        else:
            norme = self.q / d
        theta = angle(x - self.x, y - self.y)
        return Vecteur([np.cos(theta) * norme, np.sin(theta) * norme])


def main():
    P = [Particule(1, [1, 2]), Particule(1, [3, 2]), Particule(-1, [2, 3])]
    # P = [Particule(1, [2, 2])]
    x0, x1 = 0,4
    y0, y1 = 0,4
    plt.axis([x0, x1, y0, y1])
    nb_pts = 20 # sera au carré
    E = []
    
    for x in range(nb_pts):
        for y in range(nb_pts):
            u = (x1 - x0) * x / nb_pts + 0.5
            v = (y1 - y0) * y / nb_pts + 0.5
            e = Vecteur([0,0])
            for p in P:
                e.ajouter(p.champ(u,v))
            E.append([u,v,e])
            # plt.arrow(u, v, E.x, E.y, head_width=0.1, head_length=0.1, fc='black', ec='black')
            # plt.plot(u,v,'p',color="black")
    
    moy = 0
    for u,v,e in E:
        moy += e.x**2 + e.y**2
    moy /= len(E)
    
    vect_max = 5
    for u,v,e in E:
        norme = (e.x**2 + e.y**2)**0.2
        plt.arrow(u, v, vect_max * e.x / moy, vect_max * e.y / moy, head_width=0.03*norme, head_length=0.03*norme, fc='black', ec='black')
        # plt.plot(u,v,'p',color="black")

    for p in P:
        plt.plot(p.x, p.y, 'p', color='red')
    plt.show()

main()