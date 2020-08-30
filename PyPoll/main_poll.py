# Import the os module to create file paths and csv module for reading CSV files
import os
import csv

#Initialize dictionary to store candidates and corresponding votes
candidates = {}

#Initialize variables and dictionaries

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "election_data.csv")

#open and read csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #read csv header
    csv_header = next(csv_reader)
    # loop through rest of rows
    for row in csv_reader:
        # if candidate not in dictionary add to dictionary with vote count 1
        if row[2] not in candidates:
            candidates.update({row[2]:1})
        # if candidate in dictionary increment vote count by 1   
        else:
            candidates[row[2]] += 1


#count total votes
TotalVotes = sum(candidates.values())

#create list to print analysis 
lines = [] 
lines.append("Election Results")
lines.append("------------------------------")
lines.append(f"Total Votes: {TotalVotes}")
lines.append("------------------------------")

# calculate percentages from values stored in dictionary 
for candidate in candidates.keys():
    percentvote = candidates[candidate]/TotalVotes
    formatpervote = '{:.3%}'.format(percentvote)
    #add percentage to printlist
    lines.append(f"{candidate}: {formatpervote} ({candidates[candidate]})")

# Find winner
MaxValue = max(candidates.values()) 
Maxkey = max(candidates, key=candidates.get)

#Add Winner to print list
lines.append("------------------------------")
lines.append(f"Winner: {Maxkey}")
lines.append("------------------------------")

#print to terminal
print('\n'.join(lines)) 

# open the analysis text file and write analysis to file
AnalysisTxt = os.path.join("analysis", "Analysis.txt") 
with open(AnalysisTxt,"w") as f:
    f.write('\n'.join(lines))
f.close



 




        
