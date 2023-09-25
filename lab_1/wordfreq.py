# this function takes the input of a list of sentencs and gives the output of a list of words
def tokenize(lines):
    words = []
    for line in lines: # iterates through all the sentences in the list
        start = 0
        end = 0
        while start < len(line): # iterates through every symbol in the sentence
            while start < len(line) and line[start].isspace(): # checks for spaces and skips if found
                    start += 1

            if start < len(line) and line[start].isalpha(): # checks for letters 
                end = start + 1
                while end < len(line) and line[end].isalpha(): # iterates through every symbol until one isnt a letter
                     end += 1

                words.append(line[start:end].lower()) # appends the word to a list through use of range from start variable to end variable
                start = end # start the search after the found word

            elif start < len(line) and line[start].isdigit(): # checks for digits 
                end = start + 1
                while end < len(line) and line[end].isdigit(): # iterates through the sentence until one isnt a digit
                     end += 1

                words.append(line[start:end].lower()) #appends the sequence of digits into a list through use of range from start variable to end variable
                start = end 
            
            elif start < len(line):
                
                words.append(line[start].lower()) #appends the symbol to the lost of words
                start +=1 # starts over efter the symbol 
    return words # returns a list

# this function takes input of a list of words and a list of stopWords and gives the output of a dictionary with words and their frequencies
def countWords(words, stopWords): 
    wordsDict = {}

    for word in words: # iterates through the list of words
         if word in stopWords: # nothing happens if stopWord is found
              pass
         else: 
              if word in wordsDict: # if already in the dictionary increase the count by one
                 wordsDict[word] = wordsDict[word] + 1  
              else: 
                   wordsDict[word] = 1 # if not in the dictionary add it with count 1 
    return wordsDict 




def printTopMost(frequencies, n):
     sortedDict = sorted(frequencies.items(), key = lambda x:x[1]) #sorts the dictionary of words by their frequency
     i = 0
     sortedList = []
     while i < n and n < len(sortedDict): #Adds the n most frequent words to the return variable and prints them
          
          sortedList.append(str(str(sortedDict[(-i-1)][0].ljust(20))+ str(sortedDict[(-i-1)][1]).rjust(5)))

          print(sortedDict[(-i-1)][0].ljust(20)+ str(sortedDict[(-i-1)][1]).rjust(5))
          i +=1
     
     returnString= '\n'.join(sortedList) + "\n"
     return returnString





