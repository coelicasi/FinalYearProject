import string
##.replace('[', '').replace(']', '')
##characters : .translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
##changes tokens to textlines
start_of_line = []
end_of_line = []
start_characters = []
end_characters = []

def readFiles():
    try:
        with open('C:\\Users\\Alexandra\\Documents\\College\\FinalYearProject\\FinalYearProject\\pattern.txt') as file_text:  # reading in a file
            fileLines = file_text.read()  # read method
            return fileLines
    except IOError:
        print("File could not be read. It either does not exist or does not have read access")

def breaktext(fileLines):
    lines = fileLines.translate(str.maketrans("", "", string.punctuation))
    nospaces = lines.replace(" ", "")
    newlines = [x.strip("\n") for x in nospaces]
    return newlines

def removePunctuation(fileLines):
    hypenSplit = fileLines.replace('-', ' ')
    lines = hypenSplit.translate(str.maketrans("", "", string.punctuation))
    tokens = lines.split()
    return tokens

def reverseChar(fileLines):
    reversechar = fileLines[::-1]
    lines = reversechar.translate(str.maketrans("", "", string.punctuation))
    nospaces = lines.replace(" ", "")
    reversetokens = [x.strip("\n") for x in nospaces]
    return reversetokens

def leftAcrostics(fileLines):
    tokens = fileLines.split("\n")

    broken = list(fileLines.translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
    for i in range(len(tokens)):
        start_of_line.append(tokens[i].split()[:1])

    for i in range(len(tokens)):
        stri = str(tokens[i])
        char = list(stri.translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
        print(char[0])



def rightAcrostics(fileLines):
    tokens = fileLines.split("\n")
    end_of_line = []
    for i in range(len(tokens)):
        end_of_line.append(tokens[i].split()[-1:])

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

def main():
    leftAcrostics(readFiles())
    rightAcrostics(readFiles())
    print(start_of_line)
    print(start_characters)

main()