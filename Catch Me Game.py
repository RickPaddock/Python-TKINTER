# Catch Me Game!
import tkinter as tk
import random

# Function to create new random button co-ordinates
def mouseover(self):
    x_pos = random.randint(0, 440)
    y_pos = random.randint(0, 440)
    button_catch.place(x=x_pos, y=y_pos)

# Open Window
window = tk.Tk()
# Create Frame
frame_game = tk.LabelFrame(window, text="Catch Me Game!", width=500, height=500, bg="White")
# Create button and bind it to the MOUSEOVER function. When cursor 'enters' button, it triggers the function
button_catch = tk.Button(frame_game, text="Catch Me!")
button_catch.bind("<Enter>", mouseover)
button_catch.place(x=10, y=10)
# Pack window around the frame
frame_game.pack()
window.mainloop()
