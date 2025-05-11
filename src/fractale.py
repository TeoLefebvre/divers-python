import numpy as np
from matplotlib import pyplot as plt

def tortue(s,alpha):
    alpha *= np.pi / 180
    o = 0
    X,Y = [0], [0]
    for c in s:
        if c == "F":
            X.append(X[-1] + np.cos(o))
            Y.append(Y[-1] + np.sin(o))
        elif c == "+":
            o += alpha
        elif c == "-":
            o -= alpha
    plt.plot(X,Y)
    plt.show()

# tortue("F++F-F++F-F++F-F++F-F++F-F++F", 60)

def L_systeme(s0, alpha, regles, n):
    for i in range(n):
        s1 = ""
        for c in s0:
            add = False
            for l,r in regles:
                if c == l:
                    s1 += r
                    add = True
            if not add:
                s1 += c
        s0 = s1
    tortue(s0, alpha)

dragon = ["IDF", 45, [["D", "DF--G"], ["G", "DF++G"], ["I", "I+"]], 15]
hilbert = ["G", 90, [["G", "-DF+GFG+FD-"], ["D", "+GF-DFD-FG+"]], 7]
koch = ["F", 60, [["F", "F+F--F+F"]], 7]
# L_systeme(*koch)

def tortue2(s,alpha):
    alpha *= np.pi / 180
    o = 0
    X,Y = [0], [0]
    courbes = []
    S = []
    for c in s:
        if c == "F":
            X.append(X[-1] + np.cos(o))
            Y.append(Y[-1] + np.sin(o))
        elif c == "+":
            o += alpha
        elif c == "-":
            o -= alpha
        elif c == "[":
            S.append([X[-1], Y[-1], o])
        elif c == "]":
            x, y, o = S.pop()
            courbes.append([X,Y])
            X, Y = [x], [y]
    for X,Y in courbes:
        plt.plot(X,Y)
    plt.show()

def L_systeme2(s0, alpha, regles, n):
    for i in range(n):
        s1 = ""
        for c in s0:
            add = False
            for l,r in regles:
                if c == l:
                    s1 += r
                    add = True
            if not add:
                s1 += c
        s0 = s1
    tortue2(s0, alpha)

plantes = ["X", 25, [["F", "FF"], ["X", "F+[[X]-X]-F[-FX]+X"]], 6]
# L_systeme2(*plantes)

def IFS(X, functions, n):
    for i in range(n):
        Y = []
        [[Y.append(f(x)) for x in X] for f in functions]
        X = Y
    return X

def tracer(L, point = True):
    X, Y = [], []
    for x,y in L:
        X.append(x)
        Y.append(y)
    if point:
        plt.plot(X, Y, ".")
    else:
        plt.plot(X, Y)
    plt.show()

def d1(p):
    x,y = p
    return [(x-y)/2, (x+y)/2]

def d2(p):
    x,y = p
    return [1 - (x+y)/2, (x-y)/2]

def s1(p):
    x,y = p
    return [x/2, y/2]

def s2(p):
    x,y = p
    return [x/2, (y+1)/2]

def s3(p):
    x,y = p
    return [(x+1)/2, y/2]

dragon2 = [[[0., 0.]], [d1, d2], 15]
dragon3 = [[[0., 0.]], [lambda p : [(p[0] - p[1])/2, (p[0] + p[1])/2], lambda p : [1 - (p[0] + p[1])/2, (p[0] - p[1])/2]], 15]
sierpinski = [[[0., 0.]], [s1, s2, s3], 10]
tracer(IFS(*dragon3), True)
