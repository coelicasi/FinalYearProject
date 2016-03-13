def readFiles():
	try:
		with open('text.txt') as file_text:#reading in a file
			fileLines = file_text.read()#read method
			return fileLines
	except IOError:
		print("File could not be read. It either does not exist or does not have read access")

def prime(c):
	for i in range(1, int(c) + 1):
		count = 0
		for j in range(2, i):
			if i%j != 0:
				count += 1
		if count == i-2:
			return i

def toList(primeNumber):
	

def cli():
	c = int(input("Enter the number of iterations you want to do: "))
	return c
	

def main():
	toList(prime(cli()))

main()

'''
def fileCheck(fList, fileLines):
	tokens = fileLines.split()
	for i in range(len(fList)):
		fList[i] = fList[i] - 1
	print(fList)
	try:
		for i in range(len(fList)):
			print(tokens[fList[i]])
	except IndexError:
		print("Array out of bounds!")
'''