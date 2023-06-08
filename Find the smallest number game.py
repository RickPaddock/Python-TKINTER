#Click the smallest number game
import tkinter as tk
from tkinter import messagebox
from random import randint

#Create random numbers to be put in a list
number_list = []
for i in range(25):
    n = randint(0,1000)
    while n in number_list:
        print("IT HAPPENED",n)
        n = randint(0,100)
        print("IT HAPPENED",n)
    number_list.append(n)

#Reset game parameters to default settings
counter = 0
wrong_clicks = 0
game_started = False
    
#Countdown timer. If game is live keep calling itself every second and update counter by one
def countdown():
    global counter, after_id, game_started
    if game_started:
        counter += 1
        clock_area["text"] = str(counter)
        after_id = clock_area.after(1000, countdown)   

#If first time set game to TRUE and start countdown. Check if number on button is the first one in the list. If no numbers remaining then game won
def button_click(self):
    global button_val, game_started, wrong_clicks
    button_in_focus = self.widget
    button_val = int(button_in_focus["text"])
    if not game_started:
        game_started = True
        clock_area.after(1000, countdown)  
    if button_in_focus.cget('state') == tk.NORMAL:
        if button_val == number_list[0]:
            del number_list[0]
            button_in_focus.config(state=tk.DISABLED)
            button_in_focus['bg'] = 'black'
        else:
            button_in_focus.flash()
            wrong_clicks += 1
    if len(number_list) == 0:
        game_started = False
        messagebox.showinfo("Congratulations You Won!","Time: "+clock_area["text"]+" Seconds\nWrong clicks: "+str(wrong_clicks))
    
#Open window
window = tk.Tk()
window.title("Click the smallest number")

#Assign random numbers from list and create grid 5 wide and 5 high. LEft button click is assigned the button_click function
for i in range(25):
    button = tk.Button(window,text=number_list[i], width=10, bg="antiquewhite2")
    button.grid(column=i // 5, row = i % 5)
    button.bind("<Button-1>", button_click)
    
#Sort list so smallest at the start
number_list.sort()

#Add clock label at bottom which shows counter value
clock_area = tk.Label(window,text=str(counter))
clock_area.grid(row=6,columnspan=5)

window = tk.mainloop()