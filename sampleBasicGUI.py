# A very basic representation of a GUI
# This is a sample of a very basic GUI screen. It displays a window with a button.
# Author: Selina Dennis, 2010-2016

from Tkinter import *

# A mostly pointless GUI Application created to show some of the basic
# widgets available in Tkinter. The name of your class should describe
# the whole program.
class BasicGUI:

    # Initialize the entire frame
    # this is required for the program to run
    def __init__(self, master):
        self.master = master
        self.master.title("This Application does very little.")
        # set the minimum size of the window - x,y values
        self.master.minsize(400,500)
        # it's always a good idea to separate your GUI display from the
        # initial function that gets called at the start, so you can choose
        # to display the window again at any time
        self.fnCreateWidgets()
        
    # Create the widgets that will appear on the frame
    def fnCreateWidgets(self):
        # make a frame to place your widgets
        self.frWindow = Frame()
        # use the grid layout on the frame to place widgets in it
        self.frWindow.grid()

        # have a button the user can choose to do things in the program
        self.btnDisplayMessage = Button(self.frWindow, text="Press Me", command = self.fnDisplayMessage, font=("Calibri", 12))

        # have the quit button appear on the first row row, first column
        # this means that the row = 0 and the column = 0
        # make sure that the quit button aligns to the left ('west')
        self.btnDisplayMessage.grid(row=0, column=0, sticky='W')

        self.frWindow.update()

    def fnDisplayMessage(self):
        self.btnDisplayMessage.config(text="You pressed me!")

"""
This is the code that runs all of the code above - you need
this to appear LAST in your program, or in a separate file
where you 'import' this file (by using its file name)
"""
wdBaseWindow = Tk()
appBasicGUI = BasicGUI(wdBaseWindow)
wdBaseWindow.mainloop()

