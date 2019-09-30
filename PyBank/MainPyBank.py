import os
import csv

pyBank_csv = os.path.join('budget_data.csv')

with open(pyBank_csv, 'r') as pyBankData:
    csvreader = csv.reader(pyBankData, delimiter=",")

    next(csvreader, None)

    totalProfit = 0
    totalMonths = 0
    greatIncrease = 0
    greatDecrease = 0

    previousRow = 0

    monthlyChanges = []

    for row in csvreader:

        totalMonths += 1

        totalProfit += int(row[1])

        if int(row[1]) > greatIncrease:
            greatIncrease = int(row[1])
        if int(row[1]) < greatDecrease:
            greatDecrease = int(row[1])

        thisRow = int(row[1])

        monthlyChange = thisRow - previousRow

        monthlyChanges.append(monthlyChange)
        
        previousRow = int(row[1])

    monthlyChanges.pop(0)

    avgMonthChange = sum(monthlyChanges) / len(monthlyChanges)

    avgMonthChange = float('%.2f'%(avgMonthChange))

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total Profit: ${totalProfit}")
    if avgMonthChange < 0:
        print(f"Average Monthly Change: -${abs(avgMonthChange)}")
    else:
        print(f"Average Monthly Change: ${avgMonthChange}")
    print(f"Greatest Monthly Profit: ${greatIncrease}")
    print(f"Greatest Monthly Loss: -${abs(greatDecrease)}")

bankDocument = open('financial_analysis.txt','w')
bankDocument.write(f"""Financial Analysis 
------------------
Total Months: {totalMonths}
Total Profit: ${totalProfit}
Average Monthly Change: ${avgMonthChange}
Greatest Monthly Profit: ${greatIncrease}
Greatest Monthly Loss: ${greatDecrease}""")
bankDocument.close()