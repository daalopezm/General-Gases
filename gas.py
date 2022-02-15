import numpy as np
from Ball import *
from ctypes.wintypes import RGB
from tkinter import *
from collections import namedtuple

class Gas:
    def __init__(self, interaction, number_of_particles, volumen, window, canvas):
        self.interaction = interaction 
        self.number_of_particles = number_of_particles
        self.volumen = volumen
        self.window = window
        self.canvas = canvas
    
    def create_gas(self):
        max_x_velocity=20
        max_y_velocity=20

        radius = 5
        Color = namedtuple('Color', 'red green blue')

        initial_position_x = np.random.randint(10, self.volumen.width-1, self.number_of_particles)
        x_velocity = np.random.randint(-max_x_velocity, max_x_velocity, self.number_of_particles)
        initial_position_y = np.random.randint(10, self.volumen.height-1, self.number_of_particles)
        y_velocity = np.random.randint(-max_y_velocity,max_y_velocity, self.number_of_particles)

        colors_depending_on_velocity = lambda x_vel, y_vel: Color(round((x_vel**2 + y_vel**2)**0.5*255/((max_y_velocity**2+max_x_velocity**2)**0.5)),139,116)

        particles=[Ball(self.canvas, initial_position_x[i], initial_position_y[i],
            x_velocity[i], y_velocity[i], radius, colors_depending_on_velocity(x_velocity[i],y_velocity[i])) for i in range(self.number_of_particles)]

        return particles

    def move_gas(self, particles):
        for i in range(self.number_of_particles):
            particles[i].move()