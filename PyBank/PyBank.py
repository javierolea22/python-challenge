# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#csvpath = OneDrive/Escritorio/LearnPython/Assignment1/accounting.csv
csvpath = "C:/Users/Jesus Redentor/Desktop/Unit 3  Assignment - Py Me Up, Charlie/python-challenge/PyBank/budget_data.csv"

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module
counter = 0
with open(csvpath, newline='') as csvfile:

   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

   print(csvfile)

   # Read the header row first (skip this step if there is now header)
   csv_header = next(csvreader,None)

   print(csv_header)
   first_row = next(csvreader,None)
   profit = 0
   number_of_months = 0
   prev_net = int(first_row [1])
   net_change = 0
   average_list = []
   month_list = []

   for i in csvreader:
       loss = i[1]
       profit = int(loss) + profit
       number_of_months = number_of_months + 1
       net_change = int(loss) - prev_net
       prev_net = int(loss)
       average_list.append(net_change)
       month_list.append(i[0])
       
    

print("Months: " + str(number_of_months))
print("The total is: $ " + str(profit))
print('The average is ' + str(sum(average_list)/len(average_list)))

max1 = max(average_list)
monthmax = [i for i, j in enumerate(average_list) if j == max1]
min1 = min(average_list)
monthmin = [i for i, j in enumerate(average_list) if j == min1]
print("Greatest Increase in Profits:", month_list[monthmax[0]], max(average_list))
print("Greatest Decrease in Profits:", month_list[monthmin[0]], min(average_list))



