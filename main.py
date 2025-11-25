import random
import math


# The objective function to be minimized (minimum at x=0)
def target_function(x):
    return x**2



class Particle:
    def __init__(self, bounds):
        # start position: random between bounds
        self.position = random.uniform(bounds[0], bounds[1])

        # start velocity: random near 0
        self.velocity = random.uniform(-1,1)

        self.pbest_position = self.position
        self.pbest_value = target_function(self.position)



def pso_optimize():
    # TODO
    pass