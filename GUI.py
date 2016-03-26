from tkinter import *
import DecodeFunctions

textlines = DecodeFunctions.readFiles()
primeList = DecodeFunctions.prime(20)
fiblist = DecodeFunctions.fibList(10)
tokens = DecodeFunctions.removePunctuation(textlines)
decrip = "DECODER: Enter number for iterations on Fibonacci and Prime numbers. Otherwise, select an option to fins out more about the revealed text."

class Buttons:
    def __init__(self, master):

        frame3 = Frame(master)
        frame3.pack(side=TOP)
        frame = Frame(master)
        frame.pack(side = LEFT)
        frame2 = Frame(master)
        frame2.pack(side = LEFT)

        menuAcrostics = Menubutton(frame, text = "Acrostics")
        choices = Menu(menuAcrostics)
        menuAcrostics.config(menu = choices)
        choices.add_command(label="Left", command=self.leftac)
        choices.add_command(label="Right", command=self.rightac)
        menuAcrostics.grid(padx=20, pady=20)
        menuAcrostics.config(relief=RAISED)

        menuSequences = Menubutton(frame, text = "Sequences")
        choices = Menu(menuSequences)
        menuSequences.config(menu = choices)
        choices.add_command(label="Fibonacci", command=self.fib)
        choices.add_command(label="Primes", command=self.prime)
        menuSequences.grid(padx=20, pady=20)
        menuSequences.config(relief=RAISED)

        numberButton = Button(frame, text = "Numeral", command = self.numeral).grid(padx = 20, pady = 20)

        decription = Label(frame3, text = decrip).grid(padx = 5, pady = 5)
        userinput = StringVar(None)
        self.input = Entry(frame3, textvariable=userinput)
        self.input.grid(sticky = E)
        self.input.config(relief = SUNKEN)

        self.quit = Button(frame, text="Quit", command = frame.quit).grid(padx = 20, pady = 20)

        self.text = Label(frame2, text=textlines).grid(sticky=N+S+E+W)
        self.temp = StringVar(None)
        self.temp2 = StringVar(None)
        self.result = Label(frame2, textvariable=self.temp).grid(sticky=N+S+E+W, padx = 15, pady = 10)
        self.result2 = Label(frame2, textvariable=self.temp2).grid(sticky=N+S+E+W)


    def leftac(self):
        text=DecodeFunctions.leftAcrostics(textlines)
        self.temp.set(text)

    def rightac(self):
        text=DecodeFunctions.rightAcrostics(textlines)
        self.temp.set(text)

    def fib(self):
        text2 = DecodeFunctions.fibCheck(fiblist, textlines)
        self.temp.set(text2)

    def prime(self):
        text2 = DecodeFunctions.primeCheck(primeList, textlines)
        self.temp.set(text2)

    def numeral(self):
        text3 = DecodeFunctions.numerals(textlines)
        self.temp.set(text3)

        text4 = DecodeFunctions.tothehundreds(tokens)
        self.temp2.set(text4)





root = Tk()
b = Buttons(root)
root.mainloop()
