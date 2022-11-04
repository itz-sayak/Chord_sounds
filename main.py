'''
tkinter gui implementation program
guitar tuner - standard tuning and drop d
'''
from tkinter import *
import winsound


'''
1 (E)	329.63 Hz	E4
2 (B)	246.94 Hz	B3
3 (G)	196.00 Hz	G3
4 (D)	146.83 Hz	D3
5 (A)	110.00 Hz	A2
6 (E)	82.41 Hz	E2
'''

notes = {"E2": 82.41, "A2": 110.00, "D3": 146.83, "G3": 196.00, "B3": 246.94, "E4": 329.63}

class GuitarTuner:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.Label = Label(frame, text = "Standard Guitar Tuner",font=('arial',16,'bold'))
        self.Label.grid(row = 0,column = 1,pady = 10)

        self.EButton = Button(frame, text = "e" ,command = lambda: self.playNote(notes["E4"]), width = 50,height = 2,font=('arial',16,'bold'))
        self.EButton.grid(row = 2,column = 1,pady = 10)
        
        self.AButton = Button(frame, text = "B", command = lambda: self.playNote(notes["B3"]), width = 50,height = 2,font=('arial',16,'bold'))
        self.AButton.grid(row = 3,column = 1,pady = 10)

        self.DButton = Button(frame, text = "G", command = lambda: self.playNote(notes["G3"]), width = 50,height = 2,font=('arial',16,'bold'))
        self.DButton.grid(row = 4,column = 1,pady = 10)

        self.GButton = Button(frame, text = "D", command = lambda: self.playNote(notes["D3"]), width = 50,height = 2,font=('arial',16,'bold'))
        self.GButton.grid(row = 5,column = 1,pady = 10)

        self.BButton = Button(frame, text = "A", command = lambda: self.playNote(notes["A2"]), width = 50,height = 2,font=('arial',16,'bold'))
        self.BButton.grid(row = 6,column = 1,pady = 10)

        self.eButton = Button(frame, text = "E", command = lambda: self.playNote(notes["E2"]), width = 50,height = 2,font=('arial',16,'bold'))
        self.eButton.grid(row = 7,column = 1,pady = 10)

        self.quitButton = Button(frame, text = "Quit", command = frame.quit, width = 50,height = 2,font=('arial',16,'bold'))
        self.quitButton.grid(row = 9,column = 1,pady = 20)

    def playNote(self, note):
        winsound.Beep(int(float(note)),1000)
        

root = Tk()
b = GuitarTuner(root)
root.mainloop()
