# open csv file
import os
import csv

filename = (r'C:\Users\Scott\iCloudDrive\Documents\Tracy\Boot Camp\Python-challege\PyBank\Resources\budget_data.csv')

#Define Column names
Column1 = str(Date[0])
Column2 = int(Profits/Losses[1])


with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read the header row first
    csv_header = next(csvreader)

    #count the number of total months
    Total_months = Date.count('Date')

    print(Total_months)

    #read each row of data after the header
    #for row in csvreader:
            

