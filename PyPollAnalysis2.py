# Setting up the Data
import os
import csv
totalVotes = 0 # total rows (not including the header is the total of votes)
csvpath=os.path.join('..','Resources','election_data.csv')
with open(csvpath,encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csv_reader)
    # print(f"CSV Header: csv_header)
    votesPerCandidate = {} #empty dict to catch votes
    # Read each row of data after the header
    for row in csv_reader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1  

       
        

#Formatting the Data
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votesPerCandidate, key=votesPerCandidate.get)

print(f"Winner: {winner}")

# make the .txt file
f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(totalVotes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in votesPerCandidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
