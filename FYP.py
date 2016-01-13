from tkinter import *#
import nltk

root = Tk()#this stays as Tk
root.title("Text Decoder")#the title OBVIOUSLY
root.geometry("700x500")#window size

input = StringVar()

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

			Label(root, text = fileLines, justify = "left").pack(side = "left")
			Label(root, text = start_of_line, wraplength = 300, justify  = "left"). pack(side="right")
			Label(root, text = end_of_line, wraplength = 300, justify = "left").pack(side = "right")
		file_text.close()

class acrostics():
	
	def user_input():
		text = GUI.entry.get(1.0, END)
		print(text)
	def start_of_sentence():
		for i in range(len(words)):
				start_of_line.append(words[i].split()[:1])
	def end_of_line():
		for i in range(len(words)):
				end_of_line.append(words[i].split()[-1:])

class GUI:

	app = Frame(root)
	app.pack()

	instructions = Label(root, text = "Type in your text to be decoded or try a sample text").pack(side = "top")

	entry = Text(root, height = 5).pack()

	def retrieve_input():
		text = entry.get(1.0, END)
		Label(root, text = text).pack(side = "top")

	
	acrosticsb = Button(app, text = "Acrostics", command = acrostics.user_input).pack(side = "left", padx = 10, pady = 10)
	numeralsb = Button(app, text="Numerals").pack(side = "left", padx = 10, pady = 10)
	ratiosb = Button(app, text = "Ratios").pack(side = "left", padx = 10, pady = 10)
	sampletextb = Button(app, text = "Sample", command = sampleText.readSampleText).pack(side = "right", padx = 50, pady = 10)

	display = Button(app, text = "display", command = retrieve_input).pack()

	
	
	#user = entry.get(1.0, END)
	#print(user)
	root.mainloop()


GUI
