import os
import csv

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
    'Wyoming': 'WY',}

pyBoss_csv = os.path.join('employee_data.csv')
cleanData_csv = os.path.join('cleaned_employee_data.csv')

with open(cleanData_csv, 'w', newline='') as pyBossClean:
    csvwriter = csv.writer(pyBossClean, delimiter=',')
    headers = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    print(headers)
    csvwriter.writerow(headers)

    with open(pyBoss_csv, 'r') as pyBossData:
        csvreader = csv.reader(pyBossData, delimiter=",")

        next(csvreader, None)

        for row in csvreader:
            fullName = row[1]
            splitName = fullName.split()
            row.insert(1, splitName[0])
            row.insert(2, splitName[1])
            row.pop(3)
            
            oldDate = row[3]
            splitDate = oldDate.split("-")

            newDate = f"{splitDate[1]}/{splitDate[2]}/{splitDate[0]}"
            row.insert(3, newDate)
            row.pop(4)

            fullSSN = row[4]
            maskSSN = "***-**-" + fullSSN[-4:]
            row.insert(4, maskSSN)
            row.pop(5)

            fullState = row[5]
            state = us_state_abbrev[fullState]
            row.pop(5)

            row.append(state)
            print(row)
            csvwriter.writerow(row)

