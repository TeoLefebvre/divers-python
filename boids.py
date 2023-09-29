import numpy as np
from numpy import pi
from matplotlib import pyplot as plt
from matplotlib import animation

def randomint(m, M):
    return np.random.randint(m,M+1)

def random(m, M):
    return m + np.random.rand() * (M - m)

def avancer(boid):
    x = boid[0] + np.cos(boid[2]) * speed
    y = boid[1] + np.sin(boid[2]) * speed

    theta = boid[2]

    if x < 0 or x > size:
        theta = pi - boid[2]
    if y < 0 or y > size:
        theta = 2*pi - boid[2]

    if theta != boid[2]:
        boid[2] = theta
        x = boid[0] + np.cos(boid[2]) * speed
        y = boid[1] + np.sin(boid[2]) * speed

    boid[0] = x
    boid[1] = y

    return boid

def tourner(boid, speed, sens):
    boid[2] += speed * sens
    return boid

def voisins(boid):
    voisins = [[], [], [], []]
    for b in boids:
        d = (boid[0] - b[0])**2 + (boid[1] - b[1])**2
        if d != 0:
            if d < tres_proche:
                voisins[0].append(b)
            elif d < proche:
                voisins[1].append(b)
            elif d < moyen:
                voisins[2].append(b)
            elif d < loin:
                voisins[3].append(b)
    return voisins

def arg(u):
    x,y = u
    if x == 0:
        if y == 0:
            return 0
        elif y > 0:
            return pi/2
        elif y < 0:
            return 3*pi/2
    else:
        theta = np.arctan(y/x)
        if x > 0 and y >= 0:
            return theta
        elif x > 0 and y < 0:
            return 2*pi + theta
        elif x < 0 and y >= 0:
            return pi + theta
        elif x < 0 and y < 0:
            return pi + theta
    

def regles(boid):
    V = voisins(boid)
    for b in V[0]:
        phi1 = arg(np.array([np.cos(boid[2]), np.sin(boid[2])]))
        phi2 = arg(b[:2] - boid[:2])
        phi = (phi2 - phi1) % (2*pi)
        if phi < pi:
            boid = tourner(boid, 2*rot_speed, -1)
        elif phi > pi:
            boid = tourner(boid, 2*rot_speed, 1)
    for b in V[1]:
        phi1 = arg(np.array([np.cos(boid[2]), np.sin(boid[2])]))
        phi2 = arg(b[:2] - boid[:2])
        phi = (phi2 - phi1) % (2*pi)
        if phi < pi:
            boid = tourner(boid, rot_speed, -1)
        elif phi > pi:
            boid = tourner(boid, rot_speed, 1)
    for b in V[2]:
        phi1 = arg(np.array([np.cos(boid[2]), np.sin(boid[2])]))
        phi2 = arg(np.array([np.cos(b[2]), np.sin(b[2])]))
        phi = (phi2 - phi1) % (2*pi)
        if phi < pi:
            boid = tourner(boid, rot_speed, 1)
        elif phi > pi:
            boid = tourner(boid, rot_speed, -1)
    for b in V[3]:
        phi1 = arg(np.array([np.cos(boid[2]), np.sin(boid[2])]))
        phi2 = arg(b[:2] - boid[:2])
        phi = (phi2 - phi1) % (2*pi)
        if phi < pi:
            boid = tourner(boid, rot_speed, 1)
        elif phi > pi:
            boid = tourner(boid, rot_speed, -1)
    return boid

FPS = 30
t = 10  # temps de l'animation en secondes

size = 4
speed = 1.5/FPS
rot_speed = 0.03
n = 30  # nb de boids
boids = np.array([np.array([random(0, size), random(0, size), random(0, 2*pi)]) for i in range(n)])
tres_proche, proche, moyen, loin = 0.2, 0.4, 0.8, 1.2
s = 0

fig, ax = plt.subplots()
plt.plot([0, size, size, 0, 0], [0, 0, size, size, 0], color="black")
plt.axis("off")
arrows = plt.quiver(boids[:,0], boids[:,1], np.cos(boids[:,2]), np.sin(boids[:,2]), color='orange', scale=30, pivot="middle", animated=True)

def animate(i):
    global boids, FPS, t, s
    regle = i > FPS * t/3 # la synchronisation des boids s'activent au bout d'un tiers de l'animation
    # regle = True # décommenter cette ligne et commenter celle au dessus pour que les boids restent tout le temps synchronisé
    for boid in boids:
        if regle:
            boid = regles(boid)
        r = random(-0.1, 0.1)
        boid[2] += r
        boid = avancer(boid)
    return plt.quiver(boids[:,0], boids[:,1], np.cos(boids[:,2]), np.sin(boids[:,2]), color='orange', scale=30, pivot="middle", animated=True),


ani = animation.FuncAnimation(fig, animate, frames=t*FPS, blit=True, interval=1000/FPS)
plt.show()
print(s)
