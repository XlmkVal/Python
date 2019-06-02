import random

def random_walk(n):
    """ Creates a better random walk """
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0,1),(1,0),(0, -1),(-1,0)])
        y += dy
        x += dx
    return x, y

for i in range(25):
    walk = random_walk(10)
    print((walk))