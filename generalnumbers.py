import string
from word2number import w2n

wordList = []
charlist = []
indexes = []
numbers = []


def readFiles():
    try:
        with open('C:\\Users\\Alexandra\\Documents\\College\\FinalYearProject\\FinalYearProject\\text.txt') as file_text:  # reading in a file
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



def main():
    numerals(readFiles(), breaktext(readFiles()), reverseChar(readFiles()))
    convertNumbers(readFiles())
    byWord(convertNumbers(readFiles()), readFiles(), breaktext(readFiles()), reverseChar(readFiles()))


main()