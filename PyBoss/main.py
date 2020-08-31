# Import the os module to create file paths and csv module for reading CSV files
import os
import csv
import datetime

#Initialize variables and dictionaries
lines = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Path for read and write files
Emp_csv = os.path.join("Resources", "employee_data.csv")
Output_path = os.path.join("Analysis", "Output_emp_data.csv")

#open write file
with open(Output_path, 'w', newline='') as output_file:
    # Initialize csv.writer
    csvwriter = csv.writer(output_file, delimiter=',')
    # Write the header row
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    #open and read csv file
    with open(Emp_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        #read csv header
        csv_header = next(csv_reader)
        #loop through rest of the rows, re-format as needed and add values to list lines
        for row in csv_reader:
            lines.append(row[0])
            #split first name and last name
            lines.append(row[1].split(" ")[0])
            lines.append(row[1].split(" ")[1])
             #need to reformat date
            d = datetime.datetime.strptime(row[2], '%m/%d/%Y')
            lines.append(d.strftime('%m/%d/%Y'))
            #format SSN
            lines.append(f'***-**-{row[3].split("-")[2]}')
            #use state abbreviation dictionary to format state to abbreviation
            lines.append(us_state_abbrev[row[4]])
            #write to list to file
            csvwriter.writerow(lines)
            #clear the list fot next row
            lines.clear()
#close file
output_file.close