import os
import csv

budget = {}
Increase = {}
Decrease = {}
AvgChange = 0

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    #for row in csv_reader:
    prevrow = next(csv_reader)
    Rowcount = 1
    Total = int(prevrow[1])
        #budget.update({currentrow[0]:int(currentrow[1])})
    for currentrow in csv_reader:
        #currentrow = next(csv_reader)
        if currentrow[1] > prevrow[1]:
            Inc = int(currentrow[1]) - int(prevrow[1])
            Increase.update({currentrow[0]:Inc})
            AvgChange = AvgChange + Inc
        elif currentrow[1] < prevrow[1]:
            Dec = int(currentrow[1]) - int(prevrow[1])
            Decrease.update({currentrow[0]:Dec})
            AvgChange = AvgChange + Dec
        prevrow = currentrow
                   
        Rowcount = Rowcount + 1
        Total = Total + int(currentrow[1])

    Average = Total/Rowcount

MaxValue = max(Increase.values()) 
Maxkey = max(Increase, key=Increase.get)
MinValue = min(Decrease.values())   
Minkey = min(Decrease, key=Decrease.get)



#Maxkey = k for k, v in Increase.items() if v == MaxValue
#Minkey = k for k, v in Decrease.items() if v == MinValue


        



#print header
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {Rowcount}")
print(f"Total: {Total}")
print(f"Average  Change: {round(AvgChange/(Rowcount - 1),2)}")
print(f"Greatest Increase in Profits: {Maxkey} (${MaxValue})")
print(f"Greatest Decrease in Profits: {Minkey} (${MinValue})")




        
