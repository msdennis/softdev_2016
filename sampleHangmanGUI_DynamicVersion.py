# Name: A Hangman GUI
# Description: This is a hangman game, old-school style
# Author: Selina Dennis, 2016

from Tkinter import *
import pygame
import random

class Hangman:

    # Initialize the entire frame
    # Place the initial GUI for Hangman.
    # Input: Tkinter frame
    # Output: None
    def __init__(self, master):
        self.master = master
        self.master.title("Let's Play Hangman!")
        self.master.minsize(620,800)
        self.numberTurns = 0
        self.correctLetters = []
        self.arrWordLabels = []
        self.fnCreateWidgets()
        self.fnStartGame()
        
    # Create the widgets that will appear on the frame
    # This sets up the blank hangman image,
    # the blank underscore letters for the random word chosen
    # the letters as buttons to press
    # and a blank space to put the letters already chosen
    # Input: self
    # Output: None
    def fnCreateWidgets(self):
        self.frWindow = Frame(bg="white")
        self.frWindow.grid(sticky=N+S+E+W)

        # Set the default size of the screen to a 13x13 grid, stretchy!
        for i in range(0, 13):
            self.frWindow.rowconfigure(i, weight=1)
            self.frWindow.columnconfigure(i, weight=1)

        self.lblHeading = Label(self.frWindow, text="Hangman!", font=("Tahoma", 16, "bold"), bg="white", anchor=N)
        self.lblHeading.grid(row=0, column=0, columnspan=13, sticky=N)

        # Create a frame for the letters in the words
        # this helps keep the UI in place no matter how
        # many letters there are in the word
        self.frLetters = Frame(self.frWindow, bg="white")
        self.frLetters.grid(row=12, column=0, columnspan=13, sticky=N)

        # set the default of the frame to take a weight so it's also stretchy
        # I cheated and checked the max length of the word from the word list
        for i in range(0,23):
            self.frLetters.columnconfigure(i, weight=1)
        # set the row weight for row 0 - only one row means no for-loop is needed
        self.frLetters.rowconfigure(0, weight=1)

        imgGameStart = PhotoImage(file="hangmanMedia\\hangman"+ str(self.numberTurns) +".gif")
        self.lblGameStart = Label(self.frWindow, image=imgGameStart, anchor=N)
        self.lblGameStart.photo = imgGameStart
        self.lblGameStart.grid(row=1, column=0, columnspan=13, rowspan=6, sticky=N)

        self.btnStartGame = Button(self.frWindow, text="Start Game", command = self.fnStartGame, font=("Tahoma", 12))
        self.btnStartGame.grid(row=14, column=0, sticky='EW', columnspan=13)

        # Set up the letters of the alphabet as buttons
        # Computers store the alphabet as ASCII code numbers
        # Where A = 65 and Z = 90
        # Display these in two rows, 13 letters per row
        # Once a button has been created, add it to a list of buttons so it can be tracked later on
        self.allLetterButtons = []
        rowLength = 13
        # display the first 13 letters
        for i in range(65, 65+rowLength):
            newButton = Button(self.frWindow, text=chr(i), command=lambda x=i: self.fnChooseLetter(x), width=4, font=("Tahoma", 12), anchor=N)
            newButton.grid(row=7, column=i-65)
            self.allLetterButtons.append(newButton)

        # display the last 13 letters
        rowLength = 65+rowLength
        for i in range(rowLength, rowLength+13):
            newButton = Button(self.frWindow, text=chr(i), command=lambda x=i: self.fnChooseLetter(x), width=4, font=("Tahoma", 12), anchor=N)
            newButton.grid(row=8, column=i-rowLength)
            self.allLetterButtons.append(newButton)

        # allow players to guess the word if they know it

        self.lblGuessAnswer = Label(self.frWindow, text = "Your Guess:", font=("Tahoma", 12, "bold"), bg="white", anchor=N)
        self.lblGuessAnswer.grid(row=13, column=0, columnspan=3, sticky=E+W)

        self.strUserGuess = StringVar()
        self.etGuessAnswer = Entry(self.frWindow, textvariable=self.strUserGuess, font=("Tahoma", 12), bg="white")
        self.etGuessAnswer.grid(row=13, column=3, columnspan=5, sticky=E+W)

        self.btnGuessAnswer = Button(self.frWindow, text="Submit Guess", command=self.fnSubmitGuess, font=("Tahoma", 12), bg="white")
        self.btnGuessAnswer.grid(row=13, column=9, columnspan=3, sticky=E+W)
        
        self.frWindow.update()

    # Allows a user to guess the word, regardless of how many letters they've guessed so far
    # Input: self
    # Output: None
    def fnSubmitGuess(self):
        # change whatever they've typed into all upper-case
        userGuess = self.strUserGuess.get().upper()
        if userGuess == self.gameWord:
            self.correctLetters = list(self.gameWord)
        arrUpdateInfo = self.fnUpdateLetterFrame()
        # check to see if they've won by guessing all of the letters
        boolBlanksLeft = arrUpdateInfo[1]
        if boolBlanksLeft is False:
            self.fnChangeImage("win")
        else:
            self.numberTurns = self.numberTurns+1
            # Make sure it doesn't load any images that don't exist
            if self.numberTurns > 11:
                self.numberTurns = 11
            self.fnChangeImage(self.numberTurns)            
            
    # Begins a new game, regardless of if the last game is over
    # Input: self
    # Output: None
    def fnStartGame(self):
        self.btnStartGame.config(text="Reset Game")
        self.btnGuessAnswer.config(state=ACTIVE)
        # Reset the number of turns left to 0
        self.numberTurns = 0
        # Reset the labels of the letter to empty, reset the correct letters chosen list
        for eachLetterLabel in self.arrWordLabels:
            eachLetterLabel.grid_forget()
        self.arrWordLabels = []
        self.correctLetters = []
        
        # Reset the hangman image
        self.fnChangeImage(self.numberTurns)
        # Reset all of the buttons to active status
        for eachButton in self.allLetterButtons:
            eachButton.config(state=ACTIVE)

        self.gameWord = self.fnGetNewWord().upper()
        print self.gameWord
        # update the user interface to show the new word
        self.fnUpdateLetterFrame()
    
    # Updates the letters frame to show underscores for unknown letters
    # and real letters for ones that have been guessed already
    # Input:
    #       self
    #       letter chosen (String) (Optional)
    # Output: list of two booleans: LetterFound (Boolean), BlanksLeft (Boolean)
    def fnUpdateLetterFrame(self, letterChosen=None):
        # loop through the word, keeping track of the index value of each letter
        foundLetter = False
        blanksLeft = False
        for i in range(0, len(self.gameWord)):
            if letterChosen == self.gameWord[i] or self.gameWord[i] in self.correctLetters:
                newLetter = Label(self.frLetters, text=self.gameWord[i], font=("Tahoma", 16), bg="white")
                newLetter.grid(row=0, column=i)
                self.arrWordLabels.append(newLetter)
                if letterChosen not in self.correctLetters and letterChosen == self.gameWord[i]:
                    # flag that we've found a letter (rather than just updating an old one)
                    foundLetter = True
                    self.correctLetters.append(letterChosen)
            else:
                # create a new label with an underscore if one doesn't exist,
                # otherwise leave it be
                newLetter = Label(self.frLetters, text="_", font=("Tahoma", 16), bg="white")
                newLetter.grid(row=0, column=i)
                self.arrWordLabels.append(newLetter)
                blanksLeft = True
        return [foundLetter, blanksLeft]

    # Opens the wordList.txt file to obtain a random word
    # from that file.
    # Input: self
    # Output: randomWord (String)
    def fnGetNewWord(self):
        fileWordList = open("hangmanMedia\\wordList.txt", "r")
        arrAllWords = fileWordList.readlines()
        fileWordList.close()
        randomWord = random.choice(arrAllWords)
        # take out any carriage return \n characters
        randomWord = randomWord.strip()
        return randomWord
        
    # Game code to handle when a letter has been chosen
    # to compare it against the selected word
    # Input: Letter Code as an ASCII number
    # Output: None
    def fnChooseLetter(self, intLetterCode):
        # disable the button once they've chosen the letter
        intLetterIndex = intLetterCode - ord("A")
        self.allLetterButtons[intLetterIndex].config(state=DISABLED)

        # check to see if the letter is good, get the first boolean from the update function
        arrUpdateInfo = self.fnUpdateLetterFrame(chr(intLetterCode))
        boolLetterFound = arrUpdateInfo[0]
        if boolLetterFound is False:
            # For now, just cycle through the images as if they lose every time
            self.numberTurns = self.numberTurns+1
            # Make sure it doesn't load any images that don't exist
            if self.numberTurns > 11:
                self.numberTurns = 11
            self.fnChangeImage(self.numberTurns)

        # check to see if they've won by guessing all of the letters
        boolBlanksLeft = arrUpdateInfo[1]
        if boolBlanksLeft is False:
            self.fnChangeImage("win")

    def fnChangeImage(self, imageNumber):
        # Load the 'winning' sound file
        sndFile = None
        if imageNumber == "win":
            sndFile = "hangmanMedia\\fanfare.wav"
        elif imageNumber == 11:
            sndFile = "hangmanMedia\\scream_no.wav"
            self.fnDisableAllLetters()
        if sndFile is not None:
            mxMixer = pygame.mixer
            mxMixer.init()
            mxTrackOne = mxMixer.Sound(sndFile)
            mxTrackOne.play()
        
        # Change the hangman image to whatever image is passed in as an argument
        imgGameStart = PhotoImage(file="hangmanMedia\\hangman"+str(imageNumber)+".gif")
        self.lblGameStart.config(image=imgGameStart)
        self.lblGameStart.photo = imgGameStart

    def fnDisableAllLetters(self):
        for eachLetter in self.allLetterButtons:
            eachLetter.config(state=DISABLED)
        self.btnGuessAnswer.config(state=DISABLED)
        self.btnStartGame.config(text="Play Again")

"""
Create the GUI and run the mainloop to check for events
"""
wdHangmanWindow = Tk()
appHangman = Hangman(wdHangmanWindow)
# set the default weight of the rows and columns so the screen will stretch
wdHangmanWindow.rowconfigure(0, weight=1)
wdHangmanWindow.columnconfigure(0, weight=1)
wdHangmanWindow.mainloop()

