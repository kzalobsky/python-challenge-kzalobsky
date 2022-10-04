#formatting Budget Data Table
print("Financial Analysis")
print("-----------------------")

from datetime import date
from operator import index
import os
import csv
csvpath=os.path.join('..','Resources','budget_data.csv')
with open(csvpath,encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")

#Convert Budget_Data to list
with open('budget_data.csv', newline="") as f:
    reader= csv.reader(f)
    data = list(reader)
    #print(data)

#Count Months in Budget Data Files
reader = csv.reader(open("budget_data.csv"))
lines = len(list(reader))-1
print(f"Total Months: {lines}")

#Calculate Total Profits/Losses in Budget Data
sum = 0
for index, row in enumerate(data):
    if index != 0:
        current = (row[1])
        sum += int(current)


print(f"Total: {sum}")

#Find Average Change
index = 0
totalchange = 0
for index, row in enumerate(data):
    if(index > 1):
        prevRow = data[index-1]
        x1 = prevRow[1]
        x2 = row[1]
        change = int(x2) - int(x1)
        totalchange = totalchange + change

avg_change = totalchange/lines

print(f"Average Change: {avg_change}")

#Find Greatest Increase
index = 0
greatest_increase = 0
greatest_increase_index = 0
for index, row in enumerate(data):
    if index != 0:
        current_value = row[1]
        current_value_int = int(current_value)
        if current_value_int > greatest_increase:
            greatest_increase = current_value_int
            greatest_increase_index = index

greatest_increase_line_data = data[greatest_increase_index]
greatest_increase_value = greatest_increase_line_data[1]
greatest_increase_date = greatest_increase_line_data[0]
# print(greatest_increase_value, greatest_increase_date)
print(f"Greatest Increase In Profits: {greatest_increase_date, greatest_increase_value}")

#Find Greatest Decrease
index != 0
greatest_decrease = 0
greatest_decrease_index = 0
for index, row in enumerate(data):
    if index != 0:
        current_value_decrease = row[1]
        current_value_int_decrease = int(current_value_decrease)
        if current_value_int_decrease < greatest_decrease:
            greatest_decrease = current_value_int_decrease
            greatest_decrease_index = index

greatest_decrease_line_data = data[greatest_decrease_index]
greatest_decrease_value = greatest_decrease_line_data[1]
greatest_decrease_date = greatest_decrease_line_data[0]
# print(greatest_increase_value, greatest_increase_date)
print(f"Greatest Decrease In Profits: {greatest_decrease_date, (greatest_decrease_value)}")


# make the .txt file
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Months: " + str(lines))
f.write('\n')
f.write("Total: $" + str(sum))
f.write('\n')
f.write("Average Change: $" + str(avg_change)) 
f.write('\n')
f.write(f"Greatest Increase in Profits: " + str(greatest_increase_date) + "  ($" + str(greatest_increase_value) + ")")
f.write('\n')
f.write(f"Greatest Decrease in Profits: " + str(greatest_decrease_date) + "  ($" + str(greatest_decrease_value) + ")")
f.write('\n')