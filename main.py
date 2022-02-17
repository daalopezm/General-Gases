from ctypes.wintypes import RGB
from tkinter import *
import time
from Ball import *
from Gas import *
from collections import namedtuple
from functools import partial


def run():

    WIDTH = 600
    HEIGHT = 400
    window = Tk()
    Volumen = namedtuple('Volumen','width, height')    
    canvas = Canvas(window,width=WIDTH,height=HEIGHT, highlightthickness=4, highlightbackground="black")

    number_of_particles=7    
    
    button_1 = Button(window, text = "Coulomb potential gas", command = partial(
        simulate, window, gas = Gas('col',number_of_particles,Volumen(width= WIDTH,height=HEIGHT),window,canvas)))
    button_2 = Button(window, text = "Ideal Gas", command = partial(
        simulate, window, gas = Gas('ide',number_of_particles,Volumen(width= WIDTH,height=HEIGHT),window,canvas)))
    # button_3 = Button(window, text='Stop', command = stop_program)

    label_1 = Label(window,text = "Coulomb potential gas")

    label_1.grid(row=1, column=1)
    button_1.grid(row=0, column=0)
    button_2.grid(row=1, column=0)
    canvas.grid(row=0, column=1)
    window.mainloop()

def simulate(window, gas):
    particles = gas.create_gas()
    while True:        
        gas.move_gas(particles)  
        window.update()
        time.sleep(0.01)


if __name__ == '__main__':
    run()