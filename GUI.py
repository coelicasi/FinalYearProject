from tkinter import *

class Buttons:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack(side = LEFT)
		frame2 = Frame(master)
		frame2.pack(side = LEFT)
		
		
		self.button1 = Button(frame2, text = "Test", command= self.printMessage).grid()

		self.quit = Button(frame, text="Quit", command = frame.quit).grid()

	def printMessage(self):
		print("WHY")


root = Tk()
b = Buttons(root)
root.mainloop()



'''
one = Label(root, text = "One", bg = "red", fg="green").pack()
two = Label(root, text = "two", bg = "blue", fg="green").pack(fill = X)#fill across X
three = Label(root, text = "three", bg = "white", fg="green").pack(side = LEFT, fill = Y)

lebl = Label(root, text = "name").grid(row = 0, column = 0, sticky = E)
lebl2 = Label(root, text = "name2").grid(row = 1, column = 0, sticky = E)

e1 = Entry(root).grid(row = 0, column = 2)
e2 = Entry(root).grid(row = 1, column = 2)

wid = Checkbutton(root, text = "lolololol").grid(columnspan = 5)

filled = Label(root,text = "test", bg = 'red').grid(columnspan = 10, sticky = W+E+S+N, padx = 10, pady = 10)
'''