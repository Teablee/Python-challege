# open csv file
import os
import csv

filename = os.path.join('PyBank\\Resources\\budget_data.csv')

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Make place holder for separating values
    Date = []
    Profit_Losses = []
    change = []
    i = 0
    k = 0
 #Make loop through all rows   
    for row in csvreader:
        if i==0:
            #print(row)
            Column1 = row[0]
            Column2 = row[1]
            i = i + 1
            continue
       #separate values to corresponding lists
        Date.append(row[0])
        Profit_Losses.append(int(row[1]))

    for k in range(len(Profit_Losses)-1):
        change.append(Profit_Losses[k+1]-Profit_Losses[k])

# total number of months
total_months = len(Date)

#Find sum of (Profit_Losses)
Sum_Profit_losses = (sum(Profit_Losses))

#Average change of profit losses
Average = sum(change)/len(change)

#Find max and min of change
Max_change = (max(change))
Min_change = (min(change))

#Find correlating month with max and min change
Max_change_date = (Date[change.index(Max_change)+1])
Min_change_date = (Date[change.index(Min_change)+1])

#Make Table
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${Sum_Profit_losses}")
print(f"Average Change: ${round(Average, 2)}")
print(f"Greatest Increase in Profits: {Max_change_date} (${Max_change})")
print(f"Greatest Decrease in Profits: {Min_change_date} (${Min_change})")

#Write to txt file
output_file = open("Output_summary.txt", "w")
output_file.write("Financial Analysis\n")
output_file.write("---------------------------------\n")
output_file.write(f"Total Months: {total_months}\n")
output_file.write(f"Total: ${Sum_Profit_losses}\n")
output_file.write(f"Average Change: ${round(Average, 2)}\n")
output_file.write(f"Greatest Increase in Profits: {Max_change_date} (${Max_change})\n")
output_file.write(f"Greatest Decrease in Profits: {Min_change_date} (${Min_change})\n")
output_file.close()


            

