#WordCount.py
#Name: Rinku Mahato
#Date: 02/28/2026
#Assignment: Word Count

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0 
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    characters = len(line)
    letterCount = letterCount + characters
    print(words)
    for w in words:
      wordCount = wordCount + 1
    #print(line)
  print("Lines:", lineCount)
  print ("words:", wordCount)
  print("characters:", letterCount)

if __name__ == '__main__':
  main()
