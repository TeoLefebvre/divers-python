import numpy as np
from matplotlib import pyplot as plt


def distance(M1, M2):
    return ((M2[0] - M1[0])**2 + (M2[1] - M1[1])**2)**0.5


def champ(M, charges):
    E = [0, 0]
    for q, Mc in charges:
        d = distance(Mc, M)
        u = (M[0] - Mc[0], M[1] - Mc[1])
        n = q / d**3
        E[0] += n * u[0]
        E[1] += n * u[1]
    return E


def ok(M, charges, xmax, ymax, dmin):
    x, y = M
    if (x < 0 or x > xmax) and (y < 0 or y > ymax):
        print("out of graphic")
        return False
    for q, Mc in charges:
        if distance(Mc, M) < dmin:
            print("too close")
            return False
    return True


def ligne(MO, charges, xmax, ymax, dt, dmin):
    r = [MO[0], MO[1]]
    E = champ(r, charges)
    X = [MO[0]]
    Y = [MO[1]]
    c = 0
    while ok(r, charges, xmax, ymax, dmin) and c < 10000:
        E = champ(r, charges)
        r[0] += dt * E[0]
        r[1] += dt * E[1]
        X.append(r[0])
        Y.append(r[1])
        c += 1
    return X, Y


def voisinage(M, R, n):
    points = []
    for i in range(n):
        theta = 2 * np.pi * i / n
        points.append((M[0] + R * np.cos(theta), M[1] + R * np.sin(theta)))
    return points


def tracer(charges, n, xmax, ymax, dt, dmin):
    L = []
    R = 1.1 * dmin
    for q, Mc in charges:
        if q > 0:
            for M in voisinage(Mc, R, n):
                L.append(ligne(M, charges, xmax, ymax, dt, dmin))
    ax = plt.axis([0, xmax, 0, ymax])
    for l in L:
        plt.plot(l[0][0], l[1][0], 'p', color='orange')
        plt.plot(l[0], l[1], color='grey')
    for q, Mc in charges:
        if q > 0:
            # plt.plot(*Mc, 'p', color='r')
            plt.Circle(Mc, R)
        elif q < 0:
            plt.plot(*Mc, 'p', color='b')
    plt.show()


def main():
    charges = [(-1, (3, 1)), (-2, (1, 3)), (3, (1, 1.1)), (1, (4, 4))]
    tracer(charges, n=20, xmax=5, ymax=5, dt=0.01, dmin=0.3)

main()