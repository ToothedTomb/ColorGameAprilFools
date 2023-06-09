# import the modules 
import tkinter
from tkinter import*
from tkinter import CENTER, ttk, messagebox
from tkinter import Tk, Label, Button
import tkinter.messagebox
import random 
import os
from tkinter.ttk import *
import tkinter as tk
import sys
from tkinter.messagebox import showinfo




# list of possible colour. 

   
score = 1

#def reverseText(colours):
 #   str1 =""
  #  for i in colours:
   #     str1=i + str1
    #return str1 

colours = (['Red','Blue','Green','Pink','Black', 
        'Yellow','Orange','White','Purple','Brown','Grey'])
coloursReverseMode = colours.reverse()
# the game time left, initially 10 seconds. 

timeleft = 90

# function that will start the game. 
def startGame(event): 
    
    if timeleft == 90: 
        
        # start the countdown timer. 
        countdown() 
        
    # run the function to 
    # choose the next colour. 
    nextColour() 

# Function to choose and 
# display the next colour. 
def nextColour(): 

    # use the globally declared 'score' 
    # and 'play' variables above. 
    global score 
    global timeleft 

    # if a game is currently in play 
    if timeleft > 0: 

        # make the text entry box active. 
        e.focus_set() 

        # if the colour typed is equal 
        # to the colour of the text 
        if e.get().lower() == colours[1][::-1].lower(): 
            
            score += 1
        else:
            score -= 1

        # clear the text entry box. 
        e.delete(0, tkinter.END) 
        
        random.shuffle(colours) 
        
        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value 
        label.config(fg = str(colours[1]), text = str(colours[0][::-1])) 
        
        # update the points. 
        scoreLabel.config(text = "Points: "[::-1] + str(score)) 


# Countdown timer function 
def countdown(): 

    global timeleft 

    # if a game is in play 
    if timeleft > 0: 

        # decrement the timer. 
        timeleft -= 1
        
        # update the time left label 
        timeLabel.config(text = "Time left: "[::-1]
                            + str(timeleft)) 
                                
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown) 


# Driver Code 

# create a GUI window 
root = tk.Tk() 

# set the title 
root.title("Color Game April Fools Version!"[::-1])
my_menu= Menu(root)
root.config(menu=my_menu)
#This will be the popup to show keyboard shortcuts. 
def KeyboardShortcuts():
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.attributes("-topmost", True)
    root.title("Keyboard Shortcuts."[::-1])
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='ColorGameForLinux.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Keyboard shortcuts."[::-1])
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Press the 'Escape key' to exit the game."[::-1])
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit"[::-1],font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.destroy)
    B1.pack()
def whoMadeThisGame():
    root = tk.Toplevel()  
    root.attributes("-topmost", True)
    root.resizable(0,0)
    root.title("Who made this game?"[::-1])
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='ColorGameForLinux.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Who made this game?"[::-1])
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Jonathan Steadman has made this game."[::-1])
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.destroy)
    B1.pack()
def WhenWillThisGameEndSupport():
    root = tk.Toplevel()  
    root.attributes("-topmost", True)
    root.resizable(0,0)
    root.title("When did this game end support?"[::-1])
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='ColorGameForLinux.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="When did this game end support?"[::-1])
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Penguins are the best because "[::-1])
    label1 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="the Linux mascot is a penguin!"[::-1])
    label2 = ttk.Label(root,font=("Ubuntu",  16,"bold",),anchor='center', text="2nd of April 2023"[::-1])

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    label1.pack(side="top", fill="x", pady=3)
    label2.pack(side="top", fill="x", pady=3)


    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.destroy)
    B1.pack()

def howtoplay():
    root = tk.Toplevel()
    root.attributes("-topmost", True) 
    root.resizable(0,0)
    root.title("How to play this game?"[::-1])
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='ColorGameForLinux.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="How to play this game?"[::-1])
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="You will need to type down the color of the text. Not what the text says what the color is."[::-1])
    label3 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center',text="You will need to be fast to get more points but needs to be written correctly and the right color."[::-1])
    labelw = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center',text="You will lose one point if you make a mistake."[::-1])
    label4 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center',text="Press the enter key to submit you answer."[::-1])
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    label3.pack(side="top", fill="x", pady=3)
    labelw.pack(side="top",fill="x",pady=4)
    label4.pack(side="top",fill="x", pady=5)


    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.destroy)
    B1.pack()
file_menu= Menu(my_menu,background="pink",activebackground="#23d18b")
my_menu.add_cascade(label="About:"[::-1],font=("Ubuntu",18),activebackground="#23d18b", menu=file_menu)
file_menu.add_command(label="How to play this game?"[::-1],font=("Ubuntu",18),activebackground="#23d18b",background="pink",command=howtoplay)
file_menu.add_command(label="Who made this game?"[::-1],font=("Ubuntu",18),activebackground="#23d18b",background="pink",command=whoMadeThisGame) 
file_menu.add_command(label="When did this game end support?"[::-1],font=("Ubuntu",18),activebackground="#23d18b",background="pink",command=WhenWillThisGameEndSupport)
file_menu.add_command(label="Keyboard shortcuts."[::-1],font=("Ubuntu",18),activebackground="#23d18b",background="pink",command=KeyboardShortcuts)


root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='ColorGameForLinux.png'))

# set the size 
root.geometry("820x589")
#Cant maximise the software!
root.resizable(0,0)
style = Style()
Help = tkinter.Label(root, text = "Color Game April Fools 2023!"[::-1], font = ('Ubuntu', 24,"bold","underline")) 
                
Help.pack() 
# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left "[::-1] +
            str(timeleft), font = ('Ubuntu', 28)) 
                
timeLabel.pack() 
# add a score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start:"[::-1], 
                                    font = ('Ubuntu', 28)) 
scoreLabel.pack() 



# add a label for displaying the colours 
label = tkinter.Label(root, font = ('Ubuntu', 170)) 
label.pack() 

# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root,font= ("Ubuntu", 28))
# run the 'startGame' function 
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack()


# set focus on the entry box 
e.focus_set()
# Reset the game:
def restart():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


#Function to ask the user when they press the escape key to exit the software or not.
def KeyPressEsc(event):
    root = tk.Toplevel()
    root.attributes("-topmost", True)  

    root.resizable(0,0)
    root.title("Confirm to exit the game:"[::-1])
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='ColorGameForLinux.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Confirm to exit the game:"[::-1])
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Are you sure you want to leave this game?"[::-1])

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Yes",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.quit)

    B2 = tk.Button(root, text="No",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.destroy)
    B1.pack(side=tkinter.LEFT, anchor=CENTER)
    B2.pack(side=tkinter.RIGHT, anchor=CENTER)
def on_closing():
    root = tk.Toplevel()
    root.attributes("-topmost", True)  

    root.resizable(0,0)
    root.title("Confirm to exit the game:"[::-1])
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='ColorGameForLinux.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Confirm to exit the game:"[::-1])
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Are you sure you want to leave this game?"[::-1])

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Yes",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.quit)

    B2 = tk.Button(root, text="No",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.destroy)
    B1.pack(side=tkinter.LEFT, anchor=CENTER)
    B2.pack(side=tkinter.RIGHT, anchor=CENTER)


root.bind('<Escape>', KeyPressEsc)



Tbutton = tkinter.Button(root,text = "Restart The Game"[::-1],font=("ubuntu",28),bg="pink",activebackground='#23d18b',border=16, command = restart)
Tbutton.place(relx=0.5, rely=0.9, anchor=CENTER)


#When the user press the escape key they will see a popup to exit this game.
#When the user press the escape key the they will be able to leave the software by seeing the popup.
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop() 
