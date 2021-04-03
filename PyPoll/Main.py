#open csv file
import os
import csv

filename = os.path.join('PyPoll\\Resources\\election_data.csv')

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    Voter_ID = []
    County = []
    Candidate = []

    header = next(csvreader)
    #print(header)

    for row in csvreader:
       Voter_ID.append(str(row[0]))
       County.append(str(row[1]))
       Candidate.append(str(row[2]))
    
#Find # of total voters
Total_votes = (f"{len(Voter_ID)}")
#print(f"{Total_votes}")

#Find candidates running
candidate_list = set(Candidate)
#print(f"{candidate_list}")

#Count the total # of votes per candidate
Khan_count = Candidate.count("Khan")
Correy_count = Candidate.count("Correy")
Li_count = Candidate.count("Li")
Otooley_count = Candidate.count("O'Tooley")

#print(f"{Khan_count}")
#print(f"{Correy_count}")
#print(f"{Li_count}")
#print(f"{Otooley_count}")

#find percent of the vote
percent_khan = (int(Khan_count)/int(Total_votes))*100
percent_correy = (int(Correy_count)/int(Total_votes))*100
percent_li = (int(Li_count)/int(Total_votes))*100
percent_otooley = (int(Otooley_count)/int(Total_votes))*100

#Make list with all counts from each candidate
Total_list = [Khan_count, Correy_count, Li_count, Otooley_count]
#print(Total_list)

#determine the highest vote count
highest_vote = (max(Total_list))

#for winner name....
if Khan_count == highest_vote:
    winner = "Khan"
elif Correy_count == highest_vote:
    winner = "Correy"
elif Li_count == highest_vote:
    winner = "Li"
elif Otooley_count == highest_vote:
    winner = "O'Tooley"

#Make table
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {Total_votes}")
print(f"-----------------------------")
print(f"Khan: {round(percent_khan, 3)}% ({Khan_count})")
print(f"Correy: {round(percent_correy, 3)}% ({Correy_count})")
print(f"LI: {round(percent_li, 3)}% ({Li_count})")
print(f"O'Tooley: {round(percent_otooley, 3)}% ({Otooley_count})")
print(f"-----------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------")

#write to txt file
results = open('Election_results.txt', "w")
results.write("Election Results\n")
results.write(f"-----------------------------\n")
results.write(f"Total Votes: {Total_votes}\n")
results.write(f"-----------------------------\n")
results.write(f"Khan: {round(percent_khan, 3)}% ({Khan_count})\n")
results.write(f"Correy: {round(percent_correy, 3)}% ({Correy_count})\n")
results.write(f"LI: {round(percent_li, 3)}% ({Li_count})\n")
results.write(f"O'Tooley: {round(percent_otooley, 3)}% ({Otooley_count})\n")
results.write(f"-----------------------------\n")
results.write(f"Winner: {winner}\n")
results.write(f"-----------------------------")


        