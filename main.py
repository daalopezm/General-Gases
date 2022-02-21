from tkinter import *
from tkinter import messagebox
from Ball import *
from gas import *
from collections import namedtuple
from functools import partial
import time
import tkinter

number_of_particles=0

def run():

    WIDTH = 600
    HEIGHT = 400
    window = Tk()
    window.title("Gas simulator")
    window.iconbitmap('./icons/icons8-gas-storage-32.ico')

    Volumen = namedtuple('Volumen','width, height')    
    canvas = Canvas(window,width=WIDTH,height=HEIGHT, highlightthickness=4, highlightbackground="black")
    label = " "

    def change_number_of_particles(entry):
        global number_of_particles
        try:
            if entry.get().isnumeric() == True:             
                number_of_particles = int(entry.get())
            else:
                messagebox.showerror("Error", "No se puede ingresar letras")
                raise ValueError("No se puede ingresar letras")
                
        except ValueError as ve:
            print(ve)
        
    def stop_program():
        canvas.delete("all")

    def simulate():
        try:
            if number_of_particles != 0:
        
                interaction = clicked.get()
                stop_program()
                gas = Gas(interaction, number_of_particles, Volumen(width= WIDTH,height= HEIGHT), window, canvas)

                global label
                if interaction == "Coulomb potential gas":
                    label = "Coulomb potential gas"
                elif interaction == "Ideal gas":
                    label = "Ideal gas"
                else:
                    label = " "
                label_1 = Label(window, text = label)
                label_1.grid(row=4, column=1)
                
                print(number_of_particles)
                particles = gas.create_gas()

                while True:        
                    gas.move_gas(particles)  
                    label_energy = Label(window, text = f"Energy = {round(gas.energy,2)}")
                    label_energy.grid(row=5, column=0)
                    window.update()
                    time.sleep(0.01)
            
            else:
                mensaje =  "Ingresar un número de \n partículas mayor a 0"
                messagebox.showerror("Error", mensaje)
                raise ValueError(mensaje)

        except ValueError as ve:
            print(ve)

    options_of_interactions = ["Coulomb potential gas","Ideal Gas"]
    clicked = tkinter.StringVar(window)
    clicked.set("Select an interaction")
    drop = OptionMenu(window, clicked, *options_of_interactions)
    drop.config(width=20)
      
    button_1 = Button(window, text = "Simulate", command = simulate)
    button_2 = Button(window, text = 'Stop', command = stop_program)
    entry = Entry(window)
    button_enter_number_particles = Button(window, text = "Enter", command = partial(change_number_of_particles,entry))
    canvas.configure(bg='white')
    
    drop.grid(row = 0, column = 0)
    button_1.grid(row = 1, column = 0)
    button_2.grid(row = 2, column = 0)   
    entry.grid(row = 3, column = 0)
    button_enter_number_particles.grid(row = 4, column = 0)    
    canvas.grid(row = 0, column = 1, rowspan = 4)
    
    window.mainloop()

if __name__ == '__main__':
    run()