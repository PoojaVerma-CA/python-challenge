# Import the os module to create file paths and csv module for reading CSV files
import os
import csv

#Initialize variables and dictionaries
Increase = {}
Decrease = {}
SumChange = 0

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

#open and read csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #read csv header
    csv_header = next(csv_reader)
    #read first row and set rowcount to 1, and Total = profit/loss value from row 1
    prevrow = next(csv_reader)
    Rowcount = 1
    Total = int(prevrow[1])
    # now loop through the rest of the rows
    for currentrow in csv_reader:
        # If profit/loss for current row is greater than that for previous row....
        if currentrow[1] > prevrow[1]:
            # calculate Increase
            Inc = int(currentrow[1]) - int(prevrow[1])
            #Update Dictionary Increase with Month and calculted Increase
            Increase.update({currentrow[0]:Inc})
            #Add increase to SumChange
            SumChange = SumChange + Inc
        # if profit/loss for current row is less than that for previous row....
        elif currentrow[1] < prevrow[1]:
            # calculate decrease
            Dec = int(currentrow[1]) - int(prevrow[1])
            #Update Dictionary Decrease with Month and calculted decrease
            Decrease.update({currentrow[0]:Dec})
            #Add decrease to SumChange
            SumChange = SumChange + Dec

        # set previous row to current row and update row count
        prevrow = currentrow
        Rowcount = Rowcount + 1
        # add to Total profit/loss
        Total = Total + int(currentrow[1])
        # calculate Average change 
        AvgChange = SumChange/(Rowcount - 1)
        
# From Dictionary Increase calculate Max increase and key for max increase
MaxValue = max(Increase.values()) 
Maxkey = max(Increase, key=Increase.get)
# From dictionary Decrease calculate Min decrease and key for min decrease
MinValue = min(Decrease.values())   
Minkey = min(Decrease, key=Decrease.get)


# print the analysis
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {Rowcount}")
print(f"Total: {Total}")
print(f"Average  Change: {round(AvgChange,2)}")
print(f"Greatest Increase in Profits: {Maxkey} (${MaxValue})")
print(f"Greatest Decrease in Profits: {Minkey} (${MinValue})")




        
