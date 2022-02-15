from ctypes.wintypes import RGB
from tkinter import *
import time
from Ball import *
from Gas import *
import numpy as np
from collections import namedtuple

def run():

    window = Tk()

    WIDTH = 600
    HEIGHT = 400

    Volumen = namedtuple('Volumen','width, height')
    
    canvas = Canvas(window,width=WIDTH,height=HEIGHT)
    button_1 = Button(window, text="Ideal Gas")
    label_1 = Label(window,text="Ideal Gas")

    label_1.grid(row=1, column=1)
    button_1.grid(row=0, column=0)
    canvas.grid(row=0, column=1)
    

    number_of_particles=50
    gas = Gas(0,number_of_particles,Volumen(width= WIDTH,height=HEIGHT),window,canvas)
    particles = gas.create_gas()

    while True:        
        gas.move_gas(particles)  
        window.update()
        time.sleep(0.01)

    window.mainloop()

if __name__ == '__main__':
    run()
