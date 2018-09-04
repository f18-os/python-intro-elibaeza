import sys        # command line arguments
import re         # regular expression tools

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()
    
# define two arguments
inputFname = sys.argv[1]
outputFname = sys.argv[2]

# stats
words = []

# dictionary of words with count of occurrences
dictionary = dict()

# attempt to open input file
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        myWords = re.compile('[\W]+')
        # add lines in lowercase to the myList
        myList = myWords.split(line.lower() )

        for w in myList:
            words.append(str(w))

# add words and count to hashmap
for i in range(0, len(words) ):
    wString = str(words[i])
    
    if wString != '': #if statement to omit spaces
        if wString not in dictionary: # add the word to the dictionary if not in it
            dictionary[wString] = 1
        elif wString in dictionary: # if word is in dictionary then add 1 to count
            dictionary[wString] += 1

# write the hashmap to the output file
outputFile = open(outputFname, 'w')

for key,val in sorted(dictionary.items()):
    outputFile.write("%s %d\n" % (key, val))

outputFile.close() 
