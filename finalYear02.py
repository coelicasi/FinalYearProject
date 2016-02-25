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
	d = {'one': 1, 'two': 2, 'three': 3, 'four' : 4, 'five' : 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine' :9, 'ten': 10}
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

## works from the big number first(i.e. 20, 30), reverse it to add to the main def and work from the small number first then check n-1 position
##decide whether ti cycle or call end of file ?? If i > total words, display error message, or nothing of value
def loopingNumerals(tokens):
	d = {'one': 1, 'two': 2, 'three': 3, 'four' : 4, 'five' : 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine' :9, 'ten': 10}
	dSpecial = {'twenty':20, 'thirty': 30, 'fourty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
	for count, token in enumerate(tokens, 1):
		try:
			if(dSpecial.get(token)):
				i = count+1
				if(d.get(tokens[i-1])):
					n = count + dSpecial.get(token) + d.get(tokens[i-1])
					print (tokens[n-1])
				else:
					k = count + dSpecial.get(token)
					print (tokens[k-1])
		except: pass
	
'''
	for count, token in enumerate(tokens, 1):
		try:
			if(dSpecial.get(token)):
				if(tokens[token] + 1 == d.get(token)):
			
		except:
			pass
'''

def main():
	loopingNumerals(removePunctuation(readFiles()))

main()