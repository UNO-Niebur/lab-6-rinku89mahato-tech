#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  lineNum = 0


  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()
    for w in wordList:
     w =w.lower()
     w = w.replace(",", "")
     w = w.replace(".", "")
     print(w)

     if w in words:
       if lineNum not in words[w]:
        words[w].append(lineNum)
     else:
       words[w] = [lineNum]

  for word in sorted (words):
    line_list = sorted(set(words[word]))
    print(f"{word}: {line_list}")
     
  
  #print ("fish" in words) #is a word already in the dictionary?
  #words["fish"] = [2]     #add a list to the dictionary
  #print ("fish" in words) #is the word there now?
  #words["fish"].append(5) #add to an existing list
  #print(words)


if __name__ == '__main__':
  main()
