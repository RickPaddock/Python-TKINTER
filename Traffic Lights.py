import tkinter as tk

#Different combinations of traffic lights
phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

#Set framework of circles. Changable parameters are position and colour
def draw_circle(pos,colour):
    canvas.create_oval(20,10+pos,140,130+pos,fill=colour,outline='black')

#Function changes lights when 'NEXT' button pressed. It calls the draw_circle function depending on tuple values
def change_lights():
    global loop_n
    #Draw circles in correct position and add colour depending on tuple. Loop_n itterates 4 times and starts again
    draw_circle(0,'red' if phases[loop_n][0] else 'grey')
    draw_circle(130,'yellow' if phases[loop_n][1] else 'grey')
    draw_circle(260,'green' if phases[loop_n][2] else 'grey')
    loop_n += 1
    if loop_n == len(phases):
        loop_n = 0

#Set loop variable to 0 so first itteration takes first tuple position
loop_n = 0
#Draw window
window = tk.Tk()
#Draw canvas size and background colour
canvas = tk.Canvas(window, width=150, height=400, bg='grey')
#Add two buttons. Next calls change_lights function so it draws three circles with relevant colours every time
button_next = tk.Button(window,text="Next",command = change_lights)
button_quit = tk.Button(window,text="Quit",command = window.destroy)
#Position canvas and buttons
canvas.grid(row=0)
button_next.grid(row=1)
button_quit.grid(row=2)
#Call function to start with first itteration of tuple (red light only)
change_lights()
window.mainloop()