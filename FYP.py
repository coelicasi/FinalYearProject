from tkinter import *
from tkinter import messagebox
import nltk
import string

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
	numberDictionary = {'one': 1, 'two': 2, 'three': 3, 'four' : 4, 'five' : 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine' :9, 'ten': 10}
	romanDictionary = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10}
	def readSampleText():
		#start with the nth word before the number shown in text
		with open('text.txt') as file_text:
			lines = file_text.read()
			tokens = lines.split()
			for count, token in enumerate(tokens, 1):
				try:
					int(token)#check is the token is an integer
					i = count - int(token)#find the nth word before the index
					print(tokens[i-1])#print i-1 as i starts with 0
				except:
					pass#ignore everything else
		#then print the nth word AFTER the number shown in text
		with open('text.txt') as file_text:
			lines = file_text.read()
			tokens = lines.split()
			for count, token in enumerate(tokens, 1):
				try:
					int(token)#check is the token is an integer
					i = count + int(token)#find the nth word before the index
					print(tokens[i-1])#print i-1 as i starts with 0
				except:
					pass#ignore everything else

	def readRomanNumerals():
		with open('romans.txt') as file_text:
			lines = file_text.read()
			lines = lines.translate(str.maketrans("","", string.punctuation))
			tokens = lines.split()
			for count,token in enumerate(tokens, 1):
				try:
					i = count - romanDictionary.get(token)
					print(tokens[i-1])
				except:
					pass


				
			

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

		self.sampletextb = Button(frame, text = "Sample Numerals", command = Numerals.readRomanNumerals)
		self.sampletextb.pack(side = 'left', padx = 10, pady = 10)


		

root = Tk()
app = App(root)
root.geometry("700x400")
root.mainloop()
