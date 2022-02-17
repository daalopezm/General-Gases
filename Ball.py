class Ball:
    def __init__(self,canvas,x_position,y_position,x_velocity,y_velocity,radius,color):
        self.canvas=canvas
        self.figure=canvas.create_oval(x_position-radius,y_position-radius,x_position+radius,y_position+radius,
        fill='#{:02X}{:02X}{:02X}'.format(color.red,color.green,color.blue))
        self.radius = radius
        self.x_position = self.canvas.coords(self.figure)[0]+radius
        self.y_position = self.canvas.coords(self.figure)[1]+radius
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def move(self,latest_x_velocity, latest_y_velocity):
        coordinates = self.canvas.coords(self.figure)
        print(coordinates)        
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            latest_x_velocity=-latest_x_velocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            latest_y_velocity=-latest_y_velocity
        self.canvas.move(self.figure,latest_x_velocity,latest_y_velocity)

        self.x_position = self.canvas.coords(self.figure)[0]+self.radius
        self.y_position = self.canvas.coords(self.figure)[1]+self.radius
        self.x_velocity = latest_x_velocity
        self.y_velocity = latest_y_velocity

