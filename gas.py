from functools import reduce
import numpy as np
from Ball import *
from tkinter import *
from collections import namedtuple

energy = 0
K = 8.9*10**9
DELTA_T = 0.00001
RADIUS = 4
MAX_VELOCITY = 2

class Gas:
    def __init__(self, interaction, number_of_particles, volumen, window, canvas):
        self.interaction = interaction 
        self.number_of_particles = number_of_particles
        self.volumen = volumen
        self.window = window
        self.canvas = canvas
        self.energy = energy
        self.max_x_velocity = MAX_VELOCITY
        self.max_y_velocity = MAX_VELOCITY
    
    def create_gas(self):        
        
        initial_position_x = np.random.randint(10, self.volumen.width-1, self.number_of_particles)
        initial_velocity_x = np.random.randint(-self.max_x_velocity, self.max_x_velocity, self.number_of_particles)
        initial_position_y = np.random.randint(10, self.volumen.height-1, self.number_of_particles)
        initial_velocity_y = np.random.randint(-self.max_y_velocity, self.max_y_velocity, self.number_of_particles)

        particles=[Ball(self.canvas, initial_position_x[i], initial_position_y[i],
            initial_velocity_x[i], initial_velocity_y[i], RADIUS, MAX_VELOCITY) for i in range(self.number_of_particles)]

        return particles

    def coulomb_interaction(self, charge, mass, initial_position_x, initial_position_y, initial_velocity_x, initial_velocity_y):
        final_velocity_x = []
        final_velocity_y = []

        potential_matrix = np.zeros((self.number_of_particles,self.number_of_particles))

        potential_energy = 0
        kinetic_energy = mass*(sum(i*i for i in initial_velocity_x)+sum(i*i for i in initial_velocity_y))/2

        interaction_matrix_x = np.zeros((self.number_of_particles,self.number_of_particles))
        interaction_matrix_y = np.zeros((self.number_of_particles,self.number_of_particles))        
        
        for i in range(self.number_of_particles):
            for j in range(self.number_of_particles):
                if i < j:
                    ker = 1/((initial_position_x[i]-initial_position_x[j])**2+(initial_position_y[i]-initial_position_y[j])**2)
                    potential_matrix[i][j] = (K*charge)*ker**0.5
                    
                    interaction_matrix_x[i][j]=-(charge/mass)*potential_matrix[i][j]*ker*(initial_position_x[i]-initial_position_x[j])

                    interaction_matrix_x[j][i]=-interaction_matrix_x[i][j]

                    interaction_matrix_y[i][j]=-(charge/mass)*potential_matrix[i][j]*ker*(initial_position_y[i]-initial_position_y[j])

                    interaction_matrix_y[j][i]=-interaction_matrix_y[i][j]
                
                    potential_energy += potential_matrix[i][j]
                

            sum_colum_interaction_matrix_x=np.sum(interaction_matrix_x,axis=0)
            sum_colum_interaction_matrix_y=np.sum(interaction_matrix_y,axis=0)

        for i in range(self.number_of_particles):

            final_velocity_x.append(sum_colum_interaction_matrix_x[i]*DELTA_T + initial_velocity_x[i])
            final_velocity_y.append(sum_colum_interaction_matrix_y[i]*DELTA_T + initial_velocity_y[i])

        self.energy = potential_energy+kinetic_energy
        print(self.energy)

        return final_velocity_x, final_velocity_y

    def move_gas(self, particles):
        initial_x_position = [particles[i].x_position for i in range(self.number_of_particles)]
        initial_y_position = [particles[i].y_position for i in range(self.number_of_particles)]
        initial_x_velocity = [particles[i].x_velocity for i in range(self.number_of_particles)]
        initial_y_velocity = [particles[i].y_velocity for i in range(self.number_of_particles)]
        
        if self.interaction == "Coulomb potential gas":
            final_x_velocity, final_y_velocity = self.coulomb_interaction(
                    0.001, 0.0005, initial_x_position, initial_y_position, initial_x_velocity, initial_y_velocity)

            velocity = pow(pow(np.array(final_x_velocity),2)+pow(np.array(final_y_velocity),2),0.5)

            for i in range(self.number_of_particles):                                
                particles[i].move(final_x_velocity[i], final_y_velocity[i], max(velocity))            

        else:
            velocity = pow(pow(np.array(initial_x_velocity),2)+pow(np.array(initial_y_velocity),2),0.5)
            for i in range(self.number_of_particles):            
                particles[i].move(particles[i].x_velocity, particles[i].y_velocity, max(velocity)) 
