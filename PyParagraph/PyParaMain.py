import os
import re

paragraphFile = os.path.join("paragraph_1.txt")

with open(paragraphFile) as paragraphText:
    
    paragraph = paragraphText.read()
    
    wordList = paragraph.split()
    
    sentenceList = re.split("(?<=[.!?]) +", paragraph)
    
    wordsPerSentence = len(wordList) / len(sentenceList)
    
    totalCharacters = 0
    for i in range(len(wordList)):
        
        totalCharacters += len(wordList[i])
        
lettersPerWord = totalCharacters / len(wordList)

lettersPerWord = float('%.2f'%(lettersPerWord))

print(f"""Paragraph Analysis
------------------
Approximate Word Count: {len(wordList)}
Approximate Sentence Count: {len(sentenceList)}
Average Letter Count: {lettersPerWord}
Average Sentence Length: {wordsPerSentence}
""")