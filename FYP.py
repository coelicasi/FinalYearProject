#reading in the first word of a line. Works A-OK
from tkinter import *
from tkinter import messagebox
import pydoc 

root = Tk()#this stays as Tk
root.title("My Window One")#the title OBVIOUSLY
root.geometry("700x500")#window size


class FileHandling:
	with open('text.txt') as file_text:#opens pre-existing text file
		my_list = [line.split(None, 1)[0] for line in file_text]#splits out the FIRST word.
		#print (my_list)#prints list
		with open("newFile.txt", 'w') as f:
			for item in my_list:
				f.write("%s " % item)#adds list items one by one into a line.
	file_text.close()#closes file


class EndofLine:
	with open('text.txt') as file_text:
		my_list = [line.rsplit(None, 1)[-1] for line in file_text]#splits the line ONCE ONLY and starts at the end of line
		#print (my_list)
		with open("newFileEND.txt", 'w') as f:
			for item in my_list:
				f.write("%s " % item)
	file_text.close()

class GUI:
	
	def newWindow():
		NewWin = Toplevel(root)
		NewWin.title("Results")
		NewWin.geometry("500x500")
		FileHandling
		myFile = open('newFile.txt')
		data = myFile.read()
		Results = Label(NewWin, text = data)
		Results.grid(row=1, column=1)

	app = Frame(root)
	app.grid()
	button1 = Button(app, text = "Acrostics LHS", command = newWindow)
	button1.pack(side="right", padx = 20, pady=20)
	button2 = Button(app, text="dummy")
	button2.pack(side="right", padx = 10, pady = 10)
	button3 = Button(app, text = "dummy2")
	button3.pack(side="right", padx = 20, pady=20)
	button4 = Button(app, text="dummy3")
	button4.pack(side="right", padx = 20, pady = 20)

	entry = Text(root).grid()



	

	root.mainloop()

GUI
#wat
