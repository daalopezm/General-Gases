from collections import namedtuple

class Ball:
    def __init__(self,canvas,x_position,y_position,x_velocity,y_velocity,radius,max_velocity):
        
        self.radius = radius
        self.x_position = x_position
        self.y_position = y_position        
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.max_velocity = max_velocity  

        self.canvas = canvas       
        
        self.figure = self.canvas.create_oval(self.x_position-self.radius,self.y_position-self.radius,
                self.x_position+self.radius,self.y_position+self.radius, 
                fill='black', outline="")
        self.x_position = self.canvas.coords(self.figure)[0]+self.radius
        self.y_position = self.canvas.coords(self.figure)[1]+self.radius         

    def move(self,latest_x_velocity, latest_y_velocity, max_velocity):

        coordinates = self.canvas.coords(self.figure)
        
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            latest_x_velocity=-latest_x_velocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            latest_y_velocity=-latest_y_velocity
        self.canvas.move(self.figure,latest_x_velocity,latest_y_velocity)

        self.x_position = self.canvas.coords(self.figure)[0]+self.radius
        self.y_position = self.canvas.coords(self.figure)[1]+self.radius
        self.x_velocity = latest_x_velocity
        self.y_velocity = latest_y_velocity

        Color = namedtuple('Color', 'red green blue')
        
        colors_depending_on_velocity = lambda x_vel, y_vel: Color(round((x_vel**2 + y_vel**2)**0.5*255/((
            2**0.5*max_velocity))), round((x_vel**2 + y_vel**2)**0.5*84/((2**0.5*max_velocity))), 
            95-round((x_vel**2 + y_vel**2)**0.5*94/((2**0.5*max_velocity))))
        
        self.color = colors_depending_on_velocity(self.x_velocity, self.y_velocity)

        self.canvas.itemconfigure(self.figure, 
                    fill='#{:02X}{:02X}{:02X}'.format(self.color.red, self.color.green, self.color.blue))
          