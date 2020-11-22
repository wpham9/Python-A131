#Wendy Pham
import project6model
import python1_data
import tkinter as tk
from tkinter import Tk, BOTH, NORMAL, ACTIVE, DISABLED
from tkinter.ttk import Frame, Label

#data set
global bjh_movies
bjh_movies = (python1_data.string_films)

#All following functions correlate to corresponding command buttons
def barkingChoice():
    ''' Prints Barking Dogs Never Bite movie information.
        From model.py to shell.'''
    project6model.return_line(1)
    project6model.barkingChoice()
    
def hostChoice():
    ''' Prints The Host movie information.
        From model.py to shell '''
    project6model.return_line(2)
    project6model.hostChoice()
    
def momChoice():
    ''' Prints Memories of Murder movie information.
        From model.py to shell'''
    project6model.return_line(3)
    project6model.momChoice()
    
def motherChoice():
    ''' Prints Mother movie information.
        From model.py to shell.'''
    project6model.return_line(4)
    project6model.motherChoice()
    
def okjaChoice():
    ''' Prints Okja movie information.
        From model.py to shell.'''
    project6model.return_line(5)
    project6model.okjaChoice()
    
def parasiteChoice():
    ''' Prints Parasite movie information.
        From model.py to shell.'''
    project6model.return_line(6)
    project6model.parasiteChoice()
    
def snowChoice():
    ''' Prints Snowpiercer movie information.
        From model.py to shell.'''
    project6model.return_line(7)
    project6model.snowChoice()
    
def tokyoChoice():
    ''' Prints Tokyo! movie information.
        From model.py to shell.'''
    project6model.return_line(8)
    project6model.tokyoChoice()
    


#Main Function
if __name__ == "__main__":
    ''' Creates GUI window.'''
    window = tk.Tk()
    window.geometry("900x750")
    window.title("bjh movie go brrr")
    text = tk.Text(master=window, height=4, width=40)
    text.grid(sticky='n', column = 2, columnspan=2)
    text.insert(tk.END, "Films Directed by Director Bong Joon Ho\n" +
                "     Click movie poster to learn more.")
    moviePoster1 = tk.PhotoImage(file="barking.gif")
    moviePoster2 = tk.PhotoImage(file="host.gif")
    moviePoster3 = tk.PhotoImage(file="mom.gif")
    moviePoster4 = tk.PhotoImage(file="mother.gif")
    moviePoster5 = tk.PhotoImage(file="okja.gif")
    moviePoster6 = tk.PhotoImage(file="parasite.gif")
    moviePoster7 = tk.PhotoImage(file="snow.gif")
    moviePoster8 = tk.PhotoImage(file="tokyo.gif")
    
    button1 = tk.Button(master=window, image=moviePoster1, command=barkingChoice)
    button1.grid(row=1, column=1)
    button2 = tk.Button(master=window, image=moviePoster2, command=hostChoice)
    button2.grid(row=1, column=2)
    button3 = tk.Button(master=window, image=moviePoster3, command=momChoice)
    button3.grid(row=1, column=3)
    button4 = tk.Button(master=window, image=moviePoster4, command=motherChoice)
    button4.grid(row=1, column=4)
    button5 = tk.Button(master=window, image=moviePoster5, command=okjaChoice)
    button5.grid(row=2, column=1)
    button6 = tk.Button(master=window, image=moviePoster6, command=parasiteChoice)
    button6.grid(row=2, column=2)
    button7 = tk.Button(master=window, image=moviePoster7, command=snowChoice)
    button7.grid(row=2, column=3)
    button8 = tk.Button(master=window, image=moviePoster8, command=tokyoChoice)
    button8.grid(row=2, column=4)
    
    window.mainloop()
