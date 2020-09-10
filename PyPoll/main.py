#import modules
import os
import csv

#Find current working directory and create file path for csv file
cwkdir = os.getcwd()

csvpath = os.path.join(cwkdir,"Resources", "election_data.csv")

#Declare variables
votes = []
candidates = []
khan = []
correy = []
li = []
otooley = []
most_votes = 0

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
        
    #find total votes
    total_votes = (len(votes))
    
    #Find votes per candidate
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_total_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_total_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_total_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_total_votes = len(otooley)
            
    #Find the percentage of votes for each candidate
    khan_percentage= round(((khan_total_votes/total_votes)*100),3)
    correy_percentage = round(((correy_total_votes/total_votes)*100),3)
    li_percentage = round(((li_total_votes/total_votes)*100),3)
    otooley_percentage = round(((otooley_total_votes/total_votes)*100),3)
    
    
    
    #find winner
    if khan_total_votes > max(correy_total_votes,li_total_votes,otooley_total_votes):
        winner = "Khan"
    elif correy_total_votes > max(khan_total_votes, li_total_votes, otooley_total_votes):
        winner = "Correy"
    elif li_total_votes > max(khan_total_votes,correy_total_votes,otooley_total_votes):
        winner = "Li"
    else:
        winner = "O'Tooley"

    
#Print to Terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Kahn: {khan_percentage}% ({khan_total_votes})")
print(f"Correy: {correy_percentage}% ({correy_total_votes})")
print(f"Li: {li_percentage}% ({li_total_votes})")
print(f"O'Tooley: {otooley_percentage}% ({otooley_total_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
    
#export the analysis as a text file
export_file = os.path.join( cwkdir, "analysis", "voter_analysis.txt")

with open(export_file, "w") as output:
    
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("-------------------------\n")
    output.write(f"Kahn: {khan_percentage}% ({khan_total_votes})\n")
    output.write(f"Correy: {correy_percentage}% ({correy_total_votes})\n")
    output.write(f"Li: {li_percentage}% ({li_total_votes})\n")
    output.write(f"O'Tooley: {otooley_percentage}% ({otooley_total_votes})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write("-------------------------\n")
