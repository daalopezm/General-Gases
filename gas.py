import numpy as np
from Ball import *
from ctypes.wintypes import RGB
from tkinter import *
from collections import namedtuple
from functools import reduce

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
        initial_velocity_x = np.random.randint(-max_x_velocity, max_x_velocity, self.number_of_particles)
        initial_position_y = np.random.randint(10, self.volumen.height-1, self.number_of_particles)
        initial_velocity_y = np.random.randint(-max_y_velocity, max_y_velocity, self.number_of_particles)

        colors_depending_on_velocity = lambda x_vel, y_vel: Color(round((x_vel**2 + y_vel**2)**0.5*255/((
            max_y_velocity**2 + max_x_velocity**2)**0.5)), 139, 116)

        particles=[Ball(self.canvas, initial_position_x[i], initial_position_y[i],
            initial_velocity_x[i], initial_velocity_y[i], radius, 
            colors_depending_on_velocity(initial_velocity_x[i], initial_velocity_y[i])) for i in range(self.number_of_particles)]

        return particles

    def move_gas(self, particles):
        for i in range(self.number_of_particles):
            particles[i].move()

    
    def coulomb_interaction(self, charge, mass, initial_position_x, initial_position_y, initial_velocity_x, initial_velocity_y):
        final_velocity_x = []
        final_velocity_y = []
        interaction_matrix_x=np.zeros((self.number_of_particles,self.number_of_particles))
        interaction_matrix_y=np.zeros((self.number_of_particles,self.number_of_particles))
        k = 0.1
        delta_t = 0.01
        for i in range(len(initial_position_x)):
            for j in range(len(initial_position_x)):
                if i < j:
                    interaction_matrix_x[i][j]=(k*charge/mass)*charge/(
                        (initial_position_x[i]-initial_position_x[j])**2+(initial_position_y[i]-initial_position_y[j])**2)**1.5*(
                            initial_position_x[i]-initial_position_x[j])

                    interaction_matrix_x[j][i]=-interaction_matrix_x[i][j]

                    interaction_matrix_y[i][j]=(k*charge/mass)*charge/(
                        (initial_position_x[i]-initial_position_x[j])**2+(initial_position_y[i]-initial_position_y[j])**2)**1.5*(
                            initial_position_y[i]-initial_position_y[j])

                    interaction_matrix_y[j][i]=-interaction_matrix_y[i][j]

        for i in range(len(initial_position_x)):
            final_velocity_x[i] = np.sum(interaction_matrix_x,axis=i)*delta_t + initial_velocity_x[i]
            final_velocity_y[i] = np.sum(interaction_matrix_y,axis=i)*delta_t + initial_velocity_y[i]

        return final_velocity_x, final_velocity_x
