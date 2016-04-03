from tkinter import *
import DecodeFunctions

textlines = DecodeFunctions.readFiles()
primeList = DecodeFunctions.prime(1000)
fiblist = DecodeFunctions.fibList(20)
characters = DecodeFunctions.charactertext(textlines)
reverse_text = DecodeFunctions.reversetext(textlines)
reverse_characters = DecodeFunctions.reversechar(characters)
numwordlist = DecodeFunctions.convertNumbers(textlines)
index = DecodeFunctions.numbers(textlines, numwordlist)

decrip = "DECODER: Enter number for iterations of Fibonacci."

class Buttons:
    def __init__(self, master):

        frame3 = Frame(master)
        frame3.pack(side=TOP)
        frame = Frame(master )
        frame.pack(side = LEFT)
        frame2 = Frame(master)
        frame2.pack(side = LEFT, expand = 3, fill = X)
        frame21 = Frame(frame2)
        frame21.pack(side = TOP)
        frame22 = Frame(frame2)
        frame22.pack(side = BOTTOM)

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
        choices.add_command(label = "Keys", command = self.fibKey)
        menuSequences.grid(padx=20, pady=20)
        menuSequences.config(relief=RAISED)

        numberButton = Button(frame, text = "Numeral", command = self.numeral).grid(padx = 20, pady = 20)

        self.decription = Label(frame3, text = decrip).grid(padx = 5, pady = 5)

        self.quit = Button(frame, text="Quit", command = frame.quit).grid(padx = 20, pady = 20)

        self.text = Label(frame21, text=textlines)
        self.text.pack(pady = 20, fill = Y, side = TOP)

        self.rr = Label(frame22, text = "..::Results::..").pack(side = TOP)

        self.temp = StringVar(None)
        self.temp2 = StringVar(None)
        self.result = Label(frame22, textvariable=self.temp).pack(side = TOP)
        self.result2 = Label(frame22, textvariable=self.temp2).pack(side = BOTTOM)


    def leftac(self):
        code1, code2 = DecodeFunctions.leftAcrostics(textlines)
        self.temp.set(' '.join(code1))
        self.temp2.set(''.join(code2))

    def rightac(self):
        code1, code2 = DecodeFunctions.rightAcrostics(textlines)
        self.temp.set(' '.join(code1))
        self.temp2.set(''.join(code2))

    def fib(self):
        code1, code2 = DecodeFunctions.fibCheck(fiblist, textlines, characters)
        self.temp.set(' '.join(code1))
        self.temp2.set(''.join(code2))

    def prime(self):
        code1, code2 = DecodeFunctions.primeCheck(primeList, textlines, characters)
        self.temp.set(' '.join(code1))
        self.temp2.set(''.join(code2))

    def numeral(self):
        code1, code2 = DecodeFunctions.numerals(textlines, reverse_text, characters, reverse_characters)
        code3, code4 = DecodeFunctions.byWord(numwordlist, textlines, reverse_text, characters, reverse_characters)
        code13 = code1 + code3
        code24 = code2 + code4
        self.temp.set(' '.join(code13))
        self.temp2.set(''.join(code24))

    def fibKey(self):
        code1, code2 = DecodeFunctions.crossdiscovery(fiblist, primeList, textlines,index)
        self.temp.set("Fibonacci: " + ' '.join(code1))
        self.temp2.set("Prime: " + ' '.join(code2))

root = Tk()
b = Buttons(root)
root.mainloop()
