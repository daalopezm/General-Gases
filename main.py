from ctypes.wintypes import RGB
from tkinter import *
import time
from Ball import *
import numpy as np
from collections import namedtuple

def run():

    window = Tk()

    WIDTH=600
    HEIGHT=400

    canvas = Canvas(window,width=WIDTH,height=HEIGHT)
    button_1 = Button(window, text="Ideal Gas")
    label_1 = Label(window,text="Ideal Gas")

    label_1.grid(row=1,column=1)
    button_1.grid(row=0,column=0)
    canvas.grid(row=0, column=1)
    

    number_of_particles=50
    max_x_velocity=20
    max_y_velocity=20

    radius = 5
    Color = namedtuple('Color', 'red green blue')


    initial_position_x=np.random.randint(10,WIDTH-1,number_of_particles)
    x_velocity=np.random.randint(-max_x_velocity,max_x_velocity,number_of_particles)
    initial_position_y=np.random.randint(10,HEIGHT-1,number_of_particles)
    y_velocity=np.random.randint(-max_y_velocity,max_y_velocity,number_of_particles)

    colors_depending_on_velocity=lambda x_vel, y_vel: Color(round((x_vel**2 + y_vel**2)**0.5*255/((max_y_velocity**2+max_x_velocity**2)**0.5)),139,116)

    particles=[Ball(canvas,initial_position_x[i],initial_position_y[i],
        x_velocity[i],y_velocity[i],radius,colors_depending_on_velocity(x_velocity[i],y_velocity[i])) for i in range(number_of_particles)]

    while True:
        for i in range(number_of_particles):
            particles[i].move()

        window.update()
        time.sleep(0.01)

    window.mainloop()

if __name__ == '__main__':
    run()
