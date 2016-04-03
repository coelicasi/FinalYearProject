import string
from word2number import w2n

#function to open specific text file
def readFiles():
    try:##chnage to a variable for different sample texts
        with open('C:\\Users\\Alexandra\\Documents\\College\\FinalYearProject\\FinalYearProject\\codedmessage_1.txt') as file_text:  # reading in a file
        #with open(user_text_input) as file_text:
            fileLines = file_text.read()  # read method
            return fileLines
    except IOError:
        print("File could not be read. It either does not exist or does not have read access")

#gets the characters of the text doc into a list
def charactertext(fileLines):
    remove_n = ''.join([x.rstrip("\n") for x in fileLines])
    lines = remove_n.translate(str.maketrans("", "", string.punctuation)).replace(" ", "").strip()
    characters = list(lines)
    return characters

#reverse the string of the text doc into a list
def reversetext(fileLines):
    reverse_text = []
    remove_n = ''.join([x.rstrip("\n") for x in fileLines])
    textlines = remove_n.replace("-", " ").translate(str.maketrans("", "", string.punctuation)).split(" ")
    for i in range(len(textlines)-1, -1, -1):#REVERSE REVERSE
        reverse_text.append(textlines[i])
    return reverse_text

#reverses the characters of the text doc into a list
def reversechar(characters):
    reverse_characters = []
    for i in range(len(characters)-1, -1, -1):
        reverse_characters.append(characters[i])
    return reverse_characters

#changes all written numbers to digits
def convertNumbers(fileLines):
    #because of word2number being in early stages of dev, support for python 2.x only, partially works for python 3.x
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split(" ")
    newline = []
    numwordlist = []

    for i in range(len(textlines)):
        try:
            numwords = w2n.word_to_num(textlines[i])
            numwordlist.append(numwords)
        except: pass

    return numwordlist

#takes in the written num list and searches for integers, adds all to a list
def numbers(fileLines, numwordlist):
    index = []
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split()

    for i in range(len(textlines)):
        try:
            index.append(int(textlines[i]))
        except:
            pass

    for i in range(len(numwordlist)):
        try:
            index.append(int(numwordlist[i]))
        except: pass

    return index

#finds the digits in a text doc and returns a list
def numerals(fileLines, reverse_text, characters , reverse_characters):
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split()
    paragraphs = fileLines.split(("\n"))
    sentences = fileLines.replace("?", ".").replace("!", ".").split(".")#? and ! count as change of sentence
    wordList = []
    charlist = []

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
            wordList.append(reverse_text[int(textlines[token])-1])
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

    for count, token in enumerate(characters, 1):
        try:
            i = count - int(token)  # find the nth word before the index
            charlist.append(characters[i - 1])
            n = count + int(token)  # find the nth word before the index
            charlist.append(characters[n - 1])
        except:
            pass

    # n character from the start and end
    for token in range(len(textlines)):
        try:
            charlist.append(characters[int(textlines[token]) - 1])  # START
            charlist.append(reverse_characters[int(textlines[token]) - 1])  # END
        except:
            pass
        # first char of the nth sentence
        try:
            charlist.append(sentences[int(textlines[token]) - 1].split()[0][0])
        except:
            pass
        # first char of the nth paragraph
        try:
            charlist.append(paragraphs[int(textlines[token]) - 1].split()[0][0])
        except:
            pass

    return wordList, charlist

#iterates over thr text doc and finds words corresponding to numbers
def byWord(numwordlist, fileLines, reverse_text, characters , reverse_characters,):
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split()
    paragraphs = fileLines.split(("\n"))
    sentences = fileLines.replace("?", ".").replace("!", ".").split(".")
    byWord_wordlist = []

    for i in range(len(numwordlist)):
        try:
            byWord_wordlist.append(textlines[numwordlist[i] - 1])##words by start/end
            byWord_wordlist.append(reverse_text[numwordlist[i] - 1])
        except:
            pass

        try:
            byWord_wordlist.append(sentences[int(numwordlist[i]) - 1].split()[:1][0])
        except: pass

        try:
            byWord_wordlist.append(paragraphs[int(numwordlist[i]) - 1].split()[:1][0])
        except:
            pass

    byWord_charlist = []

    for i in range(len(numwordlist)):
        # characters from start/end
        try:
            byWord_charlist.append(characters[numwordlist[i] - 1])
            byWord_charlist.append(reverse_characters[numwordlist[i] - 1])
        except:
            pass

        # first char of the nth sentence
        try:
            byWord_charlist.append(sentences[int(numwordlist[i]) - 1].split()[0][0])
        except:
            pass
        # first char of the nth paragraph
        try:
            byWord_charlist.append(paragraphs[int(numwordlist[i]) - 1].split()[0][0])
        except:
            pass

    return byWord_wordlist, byWord_charlist

#find the left most word and characters, returns a list of each
def leftAcrostics(fileLines):
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split("\n")
    leftAcro_word = []
    leftAcro_char = []

    # broken = list(fileLines.translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
    for i in range(len(textlines)):
        leftAcro_word.append(textlines[i].split()[:1])#made into a list of lists

    for i in range(len(textlines)):
        stri = str(textlines[i])
        char = list(stri.translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
        leftAcro_char.append(char[0])

    return leftAcro_word, leftAcro_char

#finds the right most word and character, returns list of each
def rightAcrostics(fileLines):
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split("\n")
    rightAcro_word = []
    rightAcro_char = []

    for i in range(len(textlines)):
        rightAcro_word.append(textlines[i].split()[-1:])

    for i in range(len(textlines)):
        stri = str(textlines[i])
        char = list(stri.translate(str.maketrans("", "", string.punctuation)).replace(" ", ""))
        rightAcro_char.append(char[-1:])

    return rightAcro_word, rightAcro_char

#generates the Fibonacci sequence some n number of times
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

#generates a series of prime numbers up to c
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

#creates the list of Fibonacci numbers and returns it
def fibList(c):
    fList = []
    for i in range(c):
        fList.append(Fibonacci(i + 1))
    return fList

#searches for the words and characters corresponding to the sequence
def fibCheck(fList, fileLines, characters):
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split()
    fibArray = []
    fibchararry = []
    for i in range(len(fList)):
        fList[i] = fList[i] - 1
    try:#a safety net for when the text doc is not long enough to cover the sequence
        for i in range(len(fList)):
            fibArray.append(textlines[fList[i]])
    except IndexError:
        print("Array out of bounds!")

    try:
        for i in range(len(fList)):
            fibchararry.append(characters[fList[i]])
    except IndexError:
        print("Array out of bounds!")

    return fibArray, fibchararry

#searches for the words and characters corresponding to the sequence
def primeCheck(primeList, fileLines, characters):
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split()
    prichararray = []
    priList = []
    for i in range(len(primeList)):
        primeList[i] = primeList[i] - 1
    try:
        for i in range(len(primeList)):
            prichararray.append(characters[primeList[i]])
    except IndexError:
        print("Array out of bounds!")

    try:
        for i in range(len(primeList)):
            priList.append(textlines[primeList[i]])
    except IndexError:
        print("Array out of bounds!")

    return priList, prichararray

#finds if a number in the text doc correpsonds to a Fibonacci number, returns the Fibonacci word
#finds if a number in the text doc correpsonds to a prime number, returns the prime word
def crossdiscovery(fList,priList, fileLines, index):
    textlines = fileLines.translate(str.maketrans("", "", string.punctuation)).split()
    cross = list(set(fList).intersection(index))
    cross_prime = list(set(priList).intersection(index))
    crossed_list = []
    crossed_prime_list = []

    for i in range(len(cross)):
        crossed_list.append(textlines[cross[i] - 1])

    for i in range(len(cross_prime)):
        crossed_prime_list.append(textlines[cross_prime[i] - 1])


    return crossed_list, crossed_prime_list

def usersearch():
    user_input = input("Number of iterations for Fibonacci: ")
    return user_input
