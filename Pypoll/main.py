#import csv
import os
import csv


#import cvs file part 2
csvpath = os.path.join ("election_data.csv")

#read csv___________
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next (csvreader)
print (f"CSV Header: {csvheader}")

#total of votes

with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next (csvreader)
    votes = 0
    for line in csvfile:
        if line.strip ():
            votes += 1
    print ("Total of votes:",votes)
 
 # the candidates

with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next (csvreader)
    candidates_names = []    
    for row in csvreader:
        data = (row [2])
        if data and data not in candidates_names:
            candidates_names.append(data)
             
    print(candidates_names)
    
# counting the votes
candidate_votes = {}  # Dictionary 

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

   
    
# for blank in cadidate name
    for row in csvreader:
        candidate_name = row[2].strip()  

        # If the candidate name is not empty
        if candidate_name:
            candidate_votes[candidate_name] = candidate_votes.get(candidate_name, 0) + 1
            total_votes = sum (candidate_votes.values ())

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    
    print(f"{candidate}:  {percentage:.2f}% {votes} votes")

# Finding the winner.
winner = max(candidate_votes, key=candidate_votes.get)
print("The winner is:", winner)

#for creating the .txt file.
output_file = os.path.join("Pypoll","analysis", "analysis.txt")
with open(output_file, "w",) as datafile:
    datafile.write ("Election results"+"\n"+ "_________________________"+ "\n")
    datafile.write ("\n"+ "Total votes: " + str(votes)+"\n")
    datafile.write ("_________________________"+ "\n")
    datafile.write ("\n")
    for candidate,votes in candidate_votes.items():
        percentage = (votes/total_votes)*100
        datafile.write (f"{candidate}:  {percentage:.2f}% {votes} votes\n")
    datafile.write ("____________________________ " + "\n")
    datafile.write ("\n")
    datafile.write ("Winner: " +str (winner))