from tkinter import *
import time
from tkinter import messagebox
from Ball import *
from gas import *
from collections import namedtuple
from functools import partial

number_of_particles=1

def change_number_of_particles(entry):
    global number_of_particles
    try:
        if entry.get().isnumeric() == True:             
            number_of_particles = int(entry.get())
        else:
            raise ValueError("No se puede ingresar letras")
            messagebox.showinfo("Error", "No se puede ingresar letras")
    except ValueError as ve:
        print(ve)
    
def stop_program(canvas):
    canvas.delete("all")

def run():

    WIDTH = 600
    HEIGHT = 400
    window = Tk()
    entry = Entry(window)

    Volumen = namedtuple('Volumen','width, height')    
    canvas = Canvas(window,width=WIDTH,height=HEIGHT, highlightthickness=4, highlightbackground="black")
    label = " "

    def simulate(window, interaction):
        stop_program(canvas)
        gas = Gas(interaction,number_of_particles,Volumen(width= WIDTH,height= HEIGHT),window,canvas)
        global label
        if interaction == 'col':
            label = "Coulomb interaction"
        elif interaction == 'ide':
            label = "Ideal gas"
        else:
            label = " "
        label_1 = Label(window, text = label)
        label_1.grid(row=1, column=1)
        print(number_of_particles)
        particles = gas.create_gas()
        while True:        
            gas.move_gas(particles)  
            window.update()
            time.sleep(0.01)

    
    button_1 = Button(window, text = "Coulomb potential gas", command = partial(simulate, window, 'col'))
    button_2 = Button(window, text = "Ideal Gas", command = partial(simulate, window, 'ide'))
    button_3 = Button(window, text='Stop', command = partial(stop_program,canvas))

    button_enter_number_particles = Button(window, text = "Enter", command=partial(change_number_of_particles,entry))

    button_1.grid(row=0, column=0)
    button_2.grid(row=1, column=0)
    button_3.grid(row=2, column=0)
    canvas.grid(row=0, column=1)
    entry.grid(row= 2, column=1)
    button_enter_number_particles.grid(row= 3, column=1)    

    window.mainloop()

if __name__ == '__main__':
    run()