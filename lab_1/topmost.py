import wordfreq
import sys
import urllib.request
import ssl

def main(stopWordsFile,wordsFile,numberTopMost):
    stopWords = []

    #Reads the stopwords file and creates a list of all the stopwords
    inp_file = open(stopWordsFile)
    for i in inp_file: 
        i = i.replace('\n','')
        stopWords.append(i)
    inp_file.close()

    #Checks if the wordfile is a local file or a URL and runs the tokenize function on the wordfile
    if wordsFile[:7] == "http://" or wordsFile[:8] == "https://":
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(wordsFile,context=context)
        lines = response.read().decode("utf8").splitlines()
        words = wordfreq.tokenize(lines)
    else:
        inp_file = open(wordsFile)
        words = wordfreq.tokenize(inp_file)
        inp_file.close()
    

    wordsDict = wordfreq.countWords(words,stopWords) 

    wordfreq.printTopMost(wordsDict, int(numberTopMost)) 

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])