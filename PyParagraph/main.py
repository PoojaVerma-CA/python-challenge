# Import the os module to create file paths 
import os

 #-----------Function Definition for paragraph analysis---------------
 #------Parameters - Input file path to read and output file path to write analysis
def paragraph(InputFilePath,OutputFilePath):
    with open(InputFilePath,"r") as p:
        for lines in p:
            # build a word list
            words = lines.split(" ")
            # build a sentence list
            sentences = lines.split(".")
    
    # calculate word count and sentence count
    totwordcount =  len(words)
    totsentencecount = len(sentences)

    # count letters in each word
    LetterSum = 0
    for word in words:
        LetterSum = len(word) + LetterSum
    AvgLetterCount = LetterSum/len(words)

    # count words in each sentence
    wordsinS = 0
    for sentence in sentences:
        wordsperS = sentence.split(" ")
        wordsinS = wordsinS + len(wordsperS)
    
    # calculate sentence length
    AvgSentenceL = wordsinS/len(sentences)

    #prepare list for printing 
    lines = []
    lines.append("Paragraph Analysis")
    lines.append("----------------------------")
    lines.append(f"Approximate Word Count: {totwordcount}")
    lines.append(f"Approximate Sentence Count: {totsentencecount}")
    lines.append(f"Average Letter Count: {AvgLetterCount}")
    lines.append(f"Average Sentence Length: {AvgSentenceL}")
    #print to terminal
    print('\n'.join(lines)) 
    
    # open the analysis text file and write analysis to file
    with open(OutputFilePath,"w") as f:
        f.write('\n'.join(lines))
    f.close

#--------------------END Function------------------------------------

# Define file paths for Raw Data 
Paragraph1 = os.path.join("Resources", "paragraph_1.txt") 
Paragraph2 = os.path.join("Resources", "paragraph_2.txt") 
# Define file path for Analysis files
OutputFile1 = os.path.join("analysis", "Analysis for Paragraph_1.txt") 
OutputFile2 = os.path.join("analysis", "Analysis for Paragraph_2.txt") 

# Call function for both paragraphs
paragraph(Paragraph1,OutputFile1)
paragraph(Paragraph2,OutputFile2)