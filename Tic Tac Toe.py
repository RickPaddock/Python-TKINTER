#TO DO: Fix all flake8 issues

#Simple TIC TAC TOE game using tkinter! 
#User is always 'O' and the computer randomly places 'X' so is pretty easy to beat

import tkinter as tk
from tkinter import messagebox
from random import randrange

#Set up list to capture positions played. True means position is availble. This will be replaced with X and O if played
available_positions = [True for x in range(9)]
#Button id is used so computer can capture and replace button text with X/O
button_id = []

winner = None

#Function to check for a winner. Hardcoded every possible 3 line row/column/diagonal
def winner_check():
    global winner
    if  available_positions[0]!=True and available_positions[0]==available_positions[1]==available_positions[2]:
        winner = available_positions[0]
    elif available_positions[0]!=True and available_positions[0]==available_positions[3]==available_positions[6]:
        winner = available_positions[0]
    elif available_positions[0]!=True and available_positions[0]==available_positions[4]==available_positions[8]:
        winner = available_positions[0]
    elif available_positions[1]!=True and available_positions[1]==available_positions[4]==available_positions[7]:
        winner = available_positions[1]
    elif available_positions[2]!=True and available_positions[2]==available_positions[5]==available_positions[8]:
        winner = available_positions[2]
    elif available_positions[2]!=True and available_positions[2]==available_positions[4]==available_positions[6]:
        winner = available_positions[2]
    elif available_positions[3]!=True and available_positions[3]==available_positions[4]==available_positions[5]:
        winner = available_positions[3]
    elif available_positions[6]!=True and available_positions[6]==available_positions[7]==available_positions[8]:
        winner = available_positions[6]
    #If winner has been updated from the checks above then show message & end game
    if winner != None:
        messagebox.showinfo("Winner",str(winner)+" is the winner!")   
        window.destroy()

#Function called if a button is pressed by the user
def placement_user(self):
    global turns_remaining, winner
    button_in_focus = self.widget
    #Collect value of button
    button_pressed = button_in_focus["text"]
    #If collected value is available then continue
    if button_pressed not in["O","X"]:
        #Set value to "O" in the available positions list, disable button, and add "O" to button in red
        available_positions[button_pressed] = "O"
        button_in_focus.config(disabledforeground='red',state=tk.DISABLED,text = "O")
        #Count turns remaining (how many True values in the list)
        turns_remaining = available_positions.count(True)
        #Check for winner
        winner_check()
        #If no winner and there are remaining turns available then let the computer have a go
        if turns_remaining > 0 and winner == None:
            window.after(1000,placement_comp)
        #If no more plays remaining and there is no winner then it is a draw
        if turns_remaining == 0 and winner == None:
            messagebox.showinfo("No Winner","It's a draw. Try again!") 
            window.destroy()

#Computer function is based on random number
def placement_comp():
    comps_pos = randrange(0,8)
    #If selected random number has already been played then recall function until it picks one available
    if available_positions[comps_pos] != True:
        placement_comp()
    #Disable button and set as "X" if position is available. It obtains button id from button ID list
    else:
        available_positions[comps_pos] = "X"
        bname_comp = button_id[comps_pos]
        bname_comp.configure(disabledforeground='red',state=tk.DISABLED,text = "X")
        winner_check()
    
    
#Open window
window = tk.Tk()
window.title("TicTacToe")

#Create 9 buttons and save ID of each in a list so can be used by the computer
for i in range(9):
    button = tk.Button(window,text=i,width=5, height=2,font=("Arial", 30, "bold"),fg="light grey",bg="light grey")
    button_id.append(button)
    #Assign user placement function to left click of mouse button for every created button
    button.bind("<Button-1>",placement_user)
    #Place buttons in 3 by 3 grid
    button.grid(row = i % 3, column = i // 3)
    
window.mainloop()