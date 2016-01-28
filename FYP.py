from tkinter import *
from tkinter import messagebox
import nltk

class sampleText: 
	def readSampleText():
		start_of_line = []
		end_of_line = []
		with open('text.txt') as file_text:
			fileLines = file_text.read()
			words = fileLines.split(".")#splits the file by full stop
			for i in range(len(words)):
				start_of_line.append(words[i].split()[:1])
				#my_list.append(words[i])
			for i in range(len(words)):
				end_of_line.append(words[i].split()[-1:])

			Label(root, text = "Original Text: ", justify = "left").pack(side = "left")
			Label(root, text = fileLines, justify = "left").pack(side = "left")

			Label(root, text = "Start of line: ").pack()
			Label(root, text = start_of_line, wraplength = 200, justify  = "left"). pack()

			Label(root, text = "End of line: ").pack()
			Label(root, text = end_of_line, wraplength = 200, justify = "left").pack()
		file_text.close()
"""
class acrostics():
		print(text)
	def start_of_sentence():
		for i in range(len(words)):
				start_of_line.append(words[i].split()[:1])
	def end_of_line():
		for i in range(len(words)):
				end_of_line.append(words[i].split()[-1:])
"""

class Numerals:
	
	def readSampleText():
		nums = []
		with open('text.txt') as file_text:
			lines = file_text.read()
			tokens = lines.split()
			for token in tokens:
				if token.isdigit():
					for i in reversed(xrange(token)):
						nums.append(token)
		print(i)			
			

class App:
	def changeLabel(self):
			text = "You input: " + self.user.get()
			self.labelText.set(text)
			self.user.delete(0, END)

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.labelText = StringVar()
		self.labelText.set("Click OK when ready")
		label1 = Label(frame, textvariable = self.labelText)
		label1.pack()
		userInput = StringVar(None)
		self.user = Entry(frame, textvariable = userInput)
		self.user.pack(side = 'top', padx = 20, pady = 30)


		self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
		self.button.pack(side='bottom')

		self.hi_there = Button(frame, text="OK", command=self.changeLabel)
		self.hi_there.pack(side= 'bottom', padx = 10)

		self.acrosticsb = Button(frame, text = "Acrostics")
		self.acrosticsb.pack(side = 'left', padx = 10, pady = 10)

		self.numeralsb = Button(frame, text="Numerals")
		self.numeralsb.pack(side = 'left', padx = 10, pady = 10)

		self.ratiosb = Button(frame, text = "Ratios")
		self.ratiosb.pack(side = 'left', padx = 10, pady = 10)

		self.sampletextb = Button(frame, text = "Sample Acrostics", command = sampleText.readSampleText)
		self.sampletextb.pack(side = 'left', padx = 10, pady = 10)

		self.sampletextb = Button(frame, text = "Sample Numerals", command = Numerals.readSampleText)
		self.sampletextb.pack(side = 'left', padx = 10, pady = 10)


		

root = Tk()
app = App(root)
root.geometry("700x400")
root.mainloop()
