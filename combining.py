import string
from word2number import w2n
##probably bad coding practice, set returns, populate later?
wordList = []
charlist = []
indexes = []
numbers = []
start_of_line = []
end_of_line = []
start_characters = []
end_characters = []
fibArray = []
fibchararry = []
priList = []
prichararray = []

def readFiles():
    try:
        with open('C:\\Users\\Alexandra\\Documents\\College\\FinalYearProject\\FinalYearProject\\pattern.txt') as file_text:  # reading in a file
            fileLines = file_text.read()  # read method
            return fileLines
    except IOError:
        print("File could not be read. It either does not exist or does not have read access")



def breaktext(fileLines):
    line = fileLines.replace("-", " ")
    lines = fileLines.translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
    newlines = [x.strip("\n") for x in lines]
    return newlines

def reverseChar(fileLines):
    reversechar = fileLines[::-1]
    lines = reversechar.translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
    reversetokens = [x.strip("\n") for x in lines]
    return reversetokens

def numerals(fileLines, newlines, reversetokens):
    wordrev = ' '.join(fileLines.split()[::-1])
    wordreverse = list(wordrev.split())
    textlines = fileLines.split()
    paragraphs = fileLines.split(("\n"))
    sentences = fileLines.split(".")

    # n words before and after the number
    for count, token in enumerate(textlines, 1):
        try:
            i = count - int(token)   # find the nth word before the index
            wordList.append(textlines[i-1])
            n = count + int(token)  # find the nth word before the index
            wordList.append(textlines[n-1])
        except:
            pass
    #n word at from the start/end
    for token in range(len(textlines)):
        try:
            wordList.append(textlines[int(textlines[token]) - 1])
            wordList.append(wordreverse[int(textlines[token])])#spits out characters ??
        except: pass
    #n character from the start and end
    for token in range(len(textlines)):
        try:
            charlist.append(newlines[int(textlines[token])-1])#START
            charlist.append(reversetokens[int(textlines[token])-1])#END
        except: pass
    #first word of the nth sentence
    for token in range(len(textlines)):
        try:
            wordList.append(sentences[int(textlines[token])-1].split()[:1][0])
        except: pass

    #first word of the nth paragraph
    for token in range(len(textlines)):
        try:
            wordList.append(paragraphs[int(textlines[token])-1].split()[:1][0])
        except: pass



def convertNumbers(fileLines):
    textlines = fileLines.split()
    numwordlist = []

    for i in range(len(textlines)):
        try:
            numwords = w2n.word_to_num(textlines[i])
            numwordlist.append(numwords)
        except: pass

    return numwordlist


def byWord(numwordlist, fileLines, newlines, reversetokens):
    wordrev = ' '.join(fileLines.split()[::-1])
    wordreverse = list(wordrev.split())
    textlines = fileLines.split()
    paragraphs = fileLines.split(("\n"))
    sentences = fileLines.split(".")

    for i in range(len(numwordlist)):
        try:
            wordList.append(textlines[numwordlist[i] - 1])##words by start/end
            wordList.append(wordreverse[numwordlist[i] - 1])
        except:
            pass
        #characters from start/end
        try:
            charlist.append(newlines[numwordlist[i] - 1])
            charlist.append(reversetokens[numwordlist[i] - 1])
        except:
            pass

        try:
            wordList.append(sentences[int(numwordlist[i]) - 1].split()[:1][0])
        except: pass

        try:
            wordList.append(paragraphs[int(numwordlist[i]) - 1].split()[:1][0])
        except:
            pass

def leftAcrostics(fileLines):
    textlines = fileLines.split("\n")

    # broken = list(fileLines.translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
    for i in range(len(textlines)):
        start_of_line.append(textlines[i].split()[:1])

    for i in range(len(textlines)):
        stri = str(textlines[i])
        char = list(stri.translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
        start_characters.append(char[0])

def rightAcrostics(fileLines):
    textlines = fileLines.split("\n")
    for i in range(len(textlines)):
        end_of_line.append(textlines[i].split()[-1:])

    for i in range(len(textlines)):
        stri = str(textlines[i])
        char = list(stri.translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
        end_characters.append(char[-1:])

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

def fibCheck(fList, fileLines, newlines):
    textlines = fileLines.split()
    for i in range(len(fList)):
        fList[i] = fList[i] - 1
    try:
        for i in range(len(fList)):
            fibArray.append(textlines[fList[i]])
    except IndexError:
        print("Array out of bounds!")

    try:
        for i in range(len(fList)):
            fibchararry.append(newlines[fList[i]])
    except IndexError:
        print("Array out of bounds!")

def primeCheck(primeList, fileLines, newlines):
    textlines = fileLines.split()
    for i in range(len(primeList)):
        primeList[i] = primeList[i] - 1
    try:
        for i in range(len(primeList)):
            prichararray.append(newlines[primeList[i]])
    except IndexError:
        print("Array out of bounds!")

    try:
        for i in range(len(primeList)):
            priList.append(textlines[primeList[i]])
    except IndexError:
        print("Array out of bounds!")


def main():
    numerals(readFiles(), breaktext(readFiles()), reverseChar(readFiles()))
    convertNumbers(readFiles())
    byWord(convertNumbers(readFiles()), readFiles(), breaktext(readFiles()), reverseChar(readFiles()))


main()