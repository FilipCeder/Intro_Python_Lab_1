# this function takes an input with a list of strings and gives the output of a list with strings
def tokenize(lines):
    words = []
    for line in lines: # itterates through all the sentences in the list
        start = 0
        end = 0
        while start < len(line): # itterates through every symbol in the sentence
            while start < len(line) and line[start].isspace() == True: # checks for spaces and skips if found
                    start += 1

            if start < len(line) and line[start].isalpha() == True: # checks for letters 
                end = start + 1
                while end < len(line) and line[end].isalpha() == True: # itterates through every symbol until it isnt a letter
                     end += 1

                #print(line[start:end], "is a letter word") 
                words.append(line[start:end].lower()) # ads the word to a list through use of range from start variable to end variable
                start = end # start the search after the found word

            elif start < len(line) and line[start].isdigit() == True: # checks for digits 
                end = start + 1
                while end < len(line) and line[end].isdigit() == True: # itterates through the sentence until it isnt a digit
                     end += 1

                #print(line[start:end], "is a digit word") 
                words.append(line[start:end].lower()) # puts the digit word into a list thorugh the range from start to end
                start = end # starts over after the digit word
            
            elif start < len(line):
                end = start + 1
                while end < len(line) and line[end].isdigit() == False and line[end].isspace() == False and line[end].isalpha() == False: # itterates through the sentence until it isnt a symbol
                     end +=1

                #print(line[start:end], "is a symbol")
                words.append(line[start:end].lower()) # puts the symbol "word" in a list through the range from start to end 
                start = end # starts over efter the symbol "word"
    return words # returns a list

# this function takes input of a list of words and stopWords and gives the output of a dictionary with words and the number of times it appears
def countWords(words, stopWords): 
    wordsDict = {}

    for word in words: # itterates through the list of words
         if word in stopWords: # nothing happends if stopWords is found
              pass
         else: 
              if word in wordsDict: # if already in the dictionary increase the count by one
                 wordsDict[word] = wordsDict[word] + 1  
              else: 
                   wordsDict[word] = 1 # if not in the dictionary add it with count 1 
    return wordsDict #return the dictionary

def printTopMost(frequencies, n):
     sortedDict = sorted(frequencies.items(), key = lambda x:x[1]) # looks at the value and not the keys and makes a sorted list 
     i = 0
     sortedList = []
     while i < n and n < len(sortedDict):
          sortedList.append(str(str(sortedDict[(-i-1)][0].ljust(20))+ str(sortedDict[(-i-1)][1]).rjust(5)))
          print(sortedDict[(-i-1)][0].ljust(20)+ str(sortedDict[(-i-1)][1]).rjust(5))
          i +=1
     
     returnString= '\n'.join(sortedList) + "\n"
     return returnString


 



