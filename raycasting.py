import pygame
from math import cos, sin, atan, sqrt, floor, pi

GREY = (200,200,200)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
SKY = (134, 177, 255)

def sign(nb):
    if nb < 0:
        return -1
    else:
        return 1

pygame.init()
clock = pygame.time.Clock()
FPS = 30

pygame.display.set_caption('Ray Casting')
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

def rect(color, position):
    position[1] = screen_height - (position[1] + position[3])
    pygame.draw.rect(screen, color, position)

def circle(color, center, radius):
    center[1] = screen_height - center[1]
    pygame.draw.circle(screen, color, center, radius)

def line(color, startpoint, endpoint, width):
    startpoint[1] = screen_height - startpoint[1]
    endpoint[1] = screen_height - endpoint[1]
    pygame.draw.line(screen, color, startpoint, endpoint, width)

def draw_background():
    rect(WHITE, [0, 0, screen_width, screen_height/2])
    rect(SKY, [0, screen_height/2, screen_width, screen_height])

def define_grid():
    f = open("map.txt", "r")
    grid = []
    line = []
    c = f.read(1)
    while c:
        if (c == '\n'):
            grid.insert(0, line)
            line = []
        else:
            line.append(int(c))
        c = f.read(1)
    return grid

grid = define_grid()
grid_width = len(grid[0])
grid_height = len(grid)
square = 10

def case(color, x, y):
    rect(color, [x*square, y*square, square, square])

def draw_minimap():
    for y in range(grid_height):
        for x in range(grid_width):
            if grid[y][x]:
                case(GREY, x, y)
            else:
                case(WHITE, x, y)

class Player:
    def __init__(self):
        self.x = 2
        self.y = 2
        self.speed = 0.1
        self.orientation = 0.1
        self.rotate_speed = 0.1
        self.size = 5

p = Player()

def draw_player():
    rect(RED, [p.x*square, p.y*square, p.size, p.size])

def draw():
    draw_background()
    draw_walls()
    draw_minimap()
    draw_player()
    draw_compass()

def turn(sens):
    orientation = p.orientation + p.rotate_speed * sens
    if orientation % (pi/2) == 0:
        orientation += 0.01
    p.orientation = orientation

# def direction(angle_joueur, ratio):
#     angle = atan(ratio)+angle_joueur
#     return (cos(angle), sin(angle))

def direction (angle_joueur, ratio):
    x = cos(angle_joueur)/2 + cos(angle_joueur-pi/2)*ratio
    y = sin(angle_joueur)/2 + sin(angle_joueur-pi/2)*ratio
    return (x, y)

def deltaDist(dirX, dirY):
    deltadistX = sqrt(1+(dirY/dirX)**2)
    deltadistY = sqrt(1+(dirX/dirY)**2)
    return (deltadistX, deltadistY)

def sideDist(deltadistX, deltadistY, dirX, dirY):
    if dirX > 0:
        sideDistX = deltadistX * (1 - (p.x - floor(p.x)))
    else:
        sideDistX = deltadistX * (p.x - floor(p.x))
    if dirY > 0:
        sideDistY = deltadistY * (1 - (p.y - floor(p.y)))
    else:
        sideDistY = deltadistY * (p.y - floor(p.y))
    return (sideDistX, sideDistY)

def draw_walls():
    for i in range(screen_width):
        ratio = (i-screen_width/2)/(screen_width/2)
        dirx, diry = direction(p.orientation, ratio)
        mapx, mapy = floor(p.x), floor(p.y)
        deltadistx, deltadisty = deltaDist(dirx, diry)
        sidedistx, sidedisty = sideDist(deltadistx, deltadisty, dirx, diry)
        stepx, stepy = sign(dirx), sign(diry)
        hit = 0
        side = 0
        perpwall = 0
        while not hit:
            if sidedistx < sidedisty:
                sidedistx += deltadistx
                mapx += stepx
                side = 0
            else:
                sidedisty += deltadisty
                mapy += stepy
                side = 1
            hit = grid[mapy][mapx]
        
        if side:
            perpwall = (mapy - p.y + (1 - stepy)/2) / diry
        else:
            perpwall = (mapx - p.x + (1 - stepx)/2) / dirx
        
        wall_color = BLACK if side else GREY
        line(wall_color, [i, screen_height/2 - (screen_height/2)/perpwall], [i, screen_height/2 + (screen_height/2)/perpwall], 1)

def move(sens):
    tmpx = p.x + p.speed * cos(p.orientation) * sens
    tmpy = p.y + p.speed * sin(p.orientation) * sens
    # itmpx = int(tmpx)
    # itmpy = int(tmpy)
    # if grid[itmpy][itmpx]+grid[itmpy+1][itmpx]+grid[itmpy][itmpx+1]+grid[itmpy+1][itmpx+1] == 0:
    #     p.x = tmpx
    #     p.y = tmpy

    if grid[int(p.y)][int(tmpx)] == 0:
        p.x = tmpx

    if grid[int(tmpy)][int(p.x)] == 0:
        p.y = tmpy

class Compass:
    def __init__(self):
        self.x = screen_width - 75
        self.y = 75
        self.radius1 = 50
        self.radius2 = self.radius1 * 1.1
        self.radius3 = self.radius1 * 1.2
        self.width = 5

cmps = Compass()

def draw_compass():
    circle(BLACK, [cmps.x, cmps.y], cmps.radius3)
    circle(WHITE, [cmps.x, cmps.y], cmps.radius2)
    line(RED, [cmps.x, cmps.y], [cmps.x + cos(p.orientation)*cmps.radius1, cmps.y + sin(p.orientation)*cmps.radius1], cmps.width)

while running:
    pygame.display.flip()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_z]:
        move(1)
    if pressed[pygame.K_s]:
        move(-1)
    if pressed[pygame.K_q]:
        turn(1)
    if pressed[pygame.K_d]:
        turn(-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")

    draw()
    clock.tick(FPS)