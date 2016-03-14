import string
#read in file
def readFiles():
	try:
		with open('text.txt') as file_text:#reading in a file
			fileLines = file_text.read()#read method
			return fileLines
	except IOError:
		print("File could not be read. It either does not exist or does not have read access")

def printTextFile(fileLines):
	print(fileLines)

#punctuation
def removePunctuation(fileLines):
	hypenSplit = fileLines.replace('-', ' ')
	lines = hypenSplit.translate(str.maketrans("","", string.punctuation))
	tokens = lines.split()
	return tokens
##acrostics
def leftAcrostics(fileLines):
	tokens = fileLines.split("\n")
	start_of_line = []
	for i in range(len(tokens)):
		start_of_line.append(tokens[i].split()[:1])
	print(str(start_of_line).replace('[', '').replace(']',''))

def rightAcrostics(fileLines):
	tokens = fileLines.split("\n")
	end_of_line = []
	for i in range(len(tokens)):
		end_of_line.append(tokens[i].split()[-1:])
	print(str(end_of_line).replace('[', '').replace(']',''))

##all numerals
def numerals(fileLines):
	tokens = fileLines.split()
	#start with the nth word before the number shown in text
	for count, token in enumerate(tokens, 1):
		try:
			int(token)#check is the token is an integer
			i = count - int(token)#find the nth word before the index
			print(token + " places before " + token + ": " + tokens[i-1])
			n = count + int(token)#find the nth word before the index
			print(token + " places after " +token + ": " + tokens[n-1])
		except:
			pass

	tupleTokens = tuple(tokens)
	for count, token in enumerate(tupleTokens, 1):
		try:
			d.get(token)
			i = count - d.get(token)
			n = count + d.get(token)
			print(token + " places before " + token + ": " + tokens[i-1])
			print(token + " places after " + token + ": " + tokens[n-1])
		except:
			pass


def tothehundreds(tokens):
	d = {'one': 1, 'two': 2, 'three': 3, 'four' : 4, 'five' : 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine' :9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen':15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
	dSpecial = {'twenty':20, 'thirty': 30, 'fourty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100}
	tokenLower = [under.lower() for under in tokens] 

	#for count, token in enumerate(tokenLower, 0):
		#print(count, token)

	for count, token in enumerate(tokenLower, 0):
		try:
			if(dSpecial.get(token)):
				i = count - 1
				k = count + 1
				if(d.get(tokenLower[i])):
					if(tokenLower[k]=='and'):
						j = k+1
						if(dSpecial.get(tokenLower[j])):#a double int after 100
							l = j + 1
							if(d.get(tokenLower[l])):#a single int after a double int
								total = d.get(tokenLower[l]) + dSpecial.get(tokenLower[j]) + (dSpecial.get(token) * d.get(tokenLower[i]))
								finalCount = l 
								after = finalCount + total
								prev = finalCount - total
								if(after > len(tokenLower)):
									print("Significant number ", total, " too large for text document.")
								else:
									print(total, " words after: ", tokenLower[after])
									print(total, " words before: ", tokenLower[prev])
								break
							else:#no single int after a double int
								total = dSpecial.get(tokenLower[j]) + (dSpecial.get(token) * d.get(tokenLower[i]))
								finalCount = l 
								after = finalCount + total
								prev = finalCount - total
								if(after > len(tokenLower)):
									print("Significant number ", total, " too large for text document.")
								else:
									print(total, " words after: ", tokenLower[after])
									print(total, " words before: ", tokenLower[prev])
								break
						elif(d.get(tokenLower[j])):#a single int after 100
							total = d.get(tokenLower[j]) + (dSpecial.get(token) * d.get(tokenLower[i]))
							finalCount = j
							after = finalCount + total
							prev = finalCount - total
							if(after > len(tokenLower)):
								print("Significant number ", total, " too large for text document.")
							else:
								print(total, " words after: ", tokenLower[after])
								print(total, " words before: ", tokenLower[prev])
							break

						else: #nothing after 100
							total = (dSpecial.get(token) * d.get(tokenLower[i]))
							finalCount = k
							after = finalCount + total
							prev = finalCount - total
							if(after > len(tokenLower)):
								print("Significant number ", total, " too large for text document.")
							else:
								print(total, " words after: ", tokenLower[after])
								print(total, " words before: ", tokenLower[prev])
							break
					else: #if there is no and concactinating numbers, i.e. thirty-six, four
						break
				elif(d.get(tokenLower[k])):#single int after double int
					total = dSpecial.get(token) + d.get(tokenLower[k])
					finalCount = k
					after = finalCount + total
					prev = finalCount - total
					if(after > len(tokenLower)):
						print("Significant number ", total, " too large for text document.")
					else:
						print(total, " words after: ", tokenLower[after])
						print(total, " words before: ", tokenLower[prev])
					break
				else: #no previous number, i.e. a hundred
					total = dSpecial.get(token)
					finalCount = count
					after = finalCount + total
					prev = finalCount - total
					if(after > len(tokenLower)):
						print("Significant number ", total, " too large for text document.")
					else:
						print(total, " words after: ", tokenLower[after])
						print(total, " words before: ", tokenLower[prev])
					break

			elif(d.get(token)):
				total = d.get(token)
				finalCount = count
				after = finalCount + total
				prev = finalCount - total
				if(after > len(tokenLower)):
					print("Significant number ", total, " too large for text document.")
				else:
					print(total, " words after: ", tokenLower[after])
					print(total, " words before: ", tokenLower[prev])
				break

		except: pass

#number sequences and series
def Fibonacci(n):
	if n == 0: 
		return 0
	elif n == 1:
		return 1
	else: 
		return Fibonacci(n-1) + Fibonacci(n - 2)

def prime(c):
	primeList = []
	for i in range(1, int(c)+1):
		count = 0
		for j in range(2, i):
			if i%j != 0:
				count += 1
		if count == i-2:
			primeList.append(i)
	return primeList

def toList(c):
	fList = []
	for i in range(c):
		fList.append(Fibonacci(i+1))
	return fList

def fileCheck(fList, fileLines):
	tokens = fileLines.split()
	for i in range(len(fList)):
		fList[i] = fList[i] - 1
	try:
		for i in range(len(fList)):
			print(tokens[fList[i]])
	except IndexError:
		print("Array out of bounds!")

def primeCheck(primeList, fileLines):
	tokens = fileLines.split()
	for i in range(len(primeList)):
		primeList[i] = primeList[i] - 1
	try:
		for i in range(len(primeList)):
			print(tokens[primeList[i]])
	except IndexError:
		print("Array out of bounds!")

def cli():
	c = '?'
	while c not in '012345':
		try:
			c  = input("\t Please enter a number corresponding to what you want to do:\n0. View sample Text\n1. Left Acrostics\n2. Right Acrostics\n3. Numerals\n4. Fibonacci\n5. Prime Numbers\n\tPress ctrl^Z to exit\n")
		except IndexError:
			pass

	return c

def switch(c):
	#print(isinstance(c, str))
	try: 
		if c == str(0):
			print("-------------------Sample Text File-------------------")
			printTextFile(readFiles())
		if c == str(1):
			print("-------------------Left Acrostics-------------------")
			leftAcrostics(readFiles())
		elif c == str(2):
			print("-------------------Right Acrostics------------------")
			rightAcrostics(readFiles())
		elif c == str(3):
			print("------------------- Integers------------------")
			numerals(readFiles())
			print("-------------------Written Numbers------------------")
			tothehundreds(removePunctuation(readFiles()))
		elif c == str(4):
			print("-------------------The Fibonacci Sequence------------------")
			cc = int(input("Enter the number of iterations you want to do: "))
			fileCheck(toList(cc), readFiles())
		elif c == str(5):
			print("-------------------Prime Numbers------------------")
			cc = int(input("Enter the limit of prime numbers you want: "))#
			primeCheck(prime(cc), readFiles())
	except IndexError:
		print("Available option not choosen")

def main():
	switch(cli())

main()
