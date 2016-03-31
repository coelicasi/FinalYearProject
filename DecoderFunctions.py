import string


# read in file
def readFiles():
    try:
        with open('C:\\Users\\Alexandra\\Documents\\College\\FinalYearProject\\FinalYearProject\\text.txt') as file_text:  # reading in a file
            fileLines = file_text.read()  # read method
            return fileLines
    except IOError:
        print("File could not be read. It either does not exist or does not have read access")


def printTextFile(fileLines):
    print(fileLines)


# punctuation
def removePunctuation(fileLines):
    hypenSplit = fileLines.replace('-', ' ')
    lines = hypenSplit.translate(str.maketrans("", "", string.punctuation))
    tokens = lines.split()
    return tokens


##acrostics
def leftAcrostics(fileLines):
    tokens = fileLines.split("\n")
    start_of_line = []
    for i in range(len(tokens)):
        start_of_line.append(tokens[i].split()[:1])
    return(str(start_of_line).replace('[', '').replace(']', ''))


def rightAcrostics(fileLines):
    tokens = fileLines.split("\n")
    end_of_line = []
    for i in range(len(tokens)):
        end_of_line.append(tokens[i].split()[-1:])
    return(str(end_of_line).replace('[', '').replace(']', ''))


##all numerals
def numerals(fileLines):
    numList = []
    tokens = fileLines.split()
    # start with the nth word before the number shown in text
    for count, token in enumerate(tokens, 1):
        try:
            int(token)  # check is the token is an integer
            i = count - int(token)  # find the nth word before the index
            numList.append(tokens[i])
            n = count + int(token)  # find the nth word before the index
            numList.append(tokens[n])
        except:
            pass
    return(numList)

def tothehundreds(tokens, newlines):
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
         'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
         'eighteen': 18, 'nineteen': 19}
    dSpecial = {'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80,
                'ninety': 90, 'hundred': 100}
    num = 0
    tokenLower = [under.lower() for under in tokens]

    print("Final number: ")

    for token in range(len(tokenLower)):
        if d.get(tokenLower[token]):
            if dSpecial.get(tokenLower[token+1]):
                if tokenLower[token + 2] == "and":
                    if d.get(tokenLower[token+3]):
                        num = d.get(tokenLower[token+3]) + (d.get(tokenLower[token]) * dSpecial.get(tokenLower[token+1]))
                        return num
                    elif dSpecial.get(tokenLower[token+3]):
                        if d.get(tokenLower[token+4]):
                            num = d.get(tokenLower[token+4]) + dSpecial.get(tokenLower[token+3]) + (d.get(tokenLower[token]) * dSpecial.get(tokenLower[token+1]))
                            return num
                        else:
                            num = dSpecial.get(tokenLower[token+3]) + (d.get(tokenLower[token]) * dSpecial.get(tokenLower[token+1]))
                            return num
                    else:
                        num = d.get(tokenLower[token]) * dSpecial.get(tokenLower[token+1])
                        return num
                else:
                    num = d.get(tokenLower[token]) * dSpecial.get(tokenLower[token+1])
                    return num
            elif dSpecial.get(tokenLower[token-1]):
                num = dSpecial.get(tokenLower[token-1]) + d.get(tokenLower[token])
                return num
            else:
                num = d.get(tokenLower[token])
                return num
        else: pass

def printNum(num):
    print(num)

# number sequences and series
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def prime(c):
    primeList = []
    for i in range(1, int(c) + 1):
        count = 0
        for j in range(2, i):
            if i % j != 0:
                count += 1
        if count == i - 2:
            primeList.append(i)
    return primeList


def fibList(c):
    fList = []
    for i in range(c):
        fList.append(Fibonacci(i + 1))
    return fList


def fibCheck(fList, fileLines):
    fibArray = []
    tokens = fileLines.split()
    for i in range(len(fList)):
        fList[i] = fList[i] - 1
    try:
        for i in range(len(fList)):
            fibArray.append(tokens[fList[i]])
    except IndexError:
        print("Array out of bounds!")

    return(fibArray)


def primeCheck(primeList, fileLines):
    priList = []
    tokens = fileLines.split()
    for i in range(len(primeList)):
        primeList[i] = primeList[i] - 1
    try:
        for i in range(len(primeList)):
            priList.append(tokens[primeList[i]])
    except IndexError:
        print("Array out of bounds!")

    return(priList)