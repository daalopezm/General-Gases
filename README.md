<h1>General Gases</h1>

![Simulation image](https://github.com/daalopezm/Web-page-with-flask-and-bootstrap/blob/main/static/videos/programming/gas_explanation/Gas_sim.png?raw=true)

<p>Gases with arbitrary interactions
Here you can find a small simmulator of an ideal gas and a coulumb interaction, all with the same charge.</p>

![equation](https://latex.codecogs.com/svg.image?F(r)%20=%20%5Cfrac%7Bq%5E2%7D%7B4%5Cpi%5Cepsilon_0%7D%5Csum_%7Bi%3Cj%7D%20%5Cfrac%7B%5Chat%20r_i%7D%7B%7Cr_i-r_j%7C%5E%7B3/2%7D%7D%7B%5Ccolor%7BRed%7D%20%7D)

<p>There are two main modes until now. 
  <ol>
    <li>Ideal gas, which basically are balls that don't interact among each other. </li>
    <li>Coulomb interaction, the balls interact among each other according to the equation displayed before. </li>
  </ol>
</p>

<h2>How it works?</h2>
<p>Yo must insert in the field the number of particles that you wanna render. Then, click "enter"</p>

![alt text](https://infinite-thicket-70020.herokuapp.com/static/videos/programming/gas_explanation/field.png)

<p>In the dropdown menu, select the interaction and click in simulate. The fastest particle, more red it is and the
        darkest are slower than the red one.
    </p>

<h2>Skills developed</h2>
<p> In order to make the interface of the program, I used Tkinter, and Object Oriented Programming was used.
Some basic knowledge of physics were used, like electrostatics and integration. The velocities of each particle are obtained from the forces. This is passed to the move method in the canvas class of Tkinter. This project reinforce my knowledge in basic Python and the design of interfaces. </p>

<h2> Future developments</h2>
<p>I would like to evolve the programm in a useful tool in order to understand basic ideas of physics, like energy conservation, the partition function, and display how different interactions can affect the movement of the particles. Similar to this <a href="https://www.youtube.com/watch?v=Gwha8AxVD_s" target="_blank">video</a> that displays how particles interacting through a Lennard-Jones potential, lift a lid.</p>
