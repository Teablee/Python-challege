# open csv file
import os
import csv

filename = (r'C:\Users\Scott\iCloudDrive\Documents\Tracy\Boot Camp\Python-challege\PyBank\Resources\budget_data.csv')

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    Date = []
    Profit_Losses = []
    change = []
    i = 0
    #j = 0
    k = 0
    for row in csvreader:
        if i==0:
            print(row)
            Column1 = row[0]
            Column2 = row[1]
            i = i + 1
            continue
        print(row)
        Date.append(row[0])
        Profit_Losses.append(int(row[1]))
        #j = j + 1

    for k in range(len(Profit_Losses)-1):
        change.append(Profit_Losses[k+1]-Profit_Losses[k])

#print sum of (Profit_Losses)
print(sum(Profit_Losses))
Average = sum(change)/len(change)
print(len(Profit_Losses))
print(Average)
print(max(change))
print(min(change))

# total number of months
total_months = len(Date)
print(total_months)

            

