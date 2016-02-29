import string
def readFiles():
	try:
		with open('text.txt') as file_text:#reading in a file
			fileLines = file_text.read()#read method
			return fileLines
	except IOError:
		print("File could not be read. It either does not exist or does not have read access")

def removePunctuation(fileLines):
	hypenSplit = fileLines.replace('-', ' ')
	lines = hypenSplit.translate(str.maketrans("","", string.punctuation))
	tokens = lines.split()
	return tokens

def leftAcrostics(fileLines):
	tokens = fileLines.split("\n")
	start_of_line = []
	for i in range(len(tokens)):
		start_of_line.append(tokens[i].split()[:1])
	print(start_of_line)

def rightAcrostics(fileLines):
	tokens = fileLines.split("\n")
	end_of_line = []
	for i in range(len(tokens)):
		end_of_line.append(tokens[i].split()[-1:])
	print(end_of_line)

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

def loopingNumerals(tokens):
	d = {'one': 1, 'two': 2, 'three': 3, 'four' : 4, 'five' : 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine' :9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen':15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
	dSpecial = {'twenty':20, 'thirty': 30, 'fourty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
	tokenLower = [under.lower() for under in tokens] 
	for count, token in enumerate(tokenLower, 0):
		try:
			if(d.get(token)):
				i = count - 1	
				if(dSpecial.get(tokenLower[i])):
					print(i, dSpecial.get(tokenLower[i]), d.get(token))
					n = (i + 1) + dSpecial.get(tokenLower[i]) + d.get(token)#should count from the second number as they are technically one
					if(n > len(tokenLower)):
						print(str(tokens[-1:]).strip('[]'))
						print("Ran out of words!")
					else:
						print(n)
						print(str(tokenLower[n]).strip('[]')
		except: pass

def main():
	loopingNumerals(removePunctuation(readFiles()))


main()


'''
print (i)
			if(dSpecial.get(tokens[i-1])):
				n = count + dSpecial.get(tokens[i-1]) + d.get(token)
				m = count + dSpecial.get(tokens[i-1]) + d.get(token)
				if(n > len(tokens)):
					print("End of file reached.")
				#else:
					#print(tokens[n-1])
					#print(tokens[m-1])
			else:
				print("This is " + d.get(token))
				n = count + d.get(token)#n starts from 0
				m = count - d.get(token)
				#print(tokens[n-1])
				#print(tokens[m-1])
'''