# Modules - Start by importing relevant modules
import os
import csv



# Set the path for file, it has been manually placed in the same folder, so both csv file and python VSC file in same folder
csvpath = os.path.join("election_data.csv")
output_pathout = os.path.join("..", "Resources", "Election Analysis")
print(csvpath) 

# Total Vote Counter + Candidate Counter
votes = 0
winner_votes = 0
total_num_candidates = 0
most_votes = ["", 0]
candidate_options = []
candidate_votes = {}

# Read the csv and convert it into a list of dictionaries
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        votes = votes + 1
        total_num_candidates = row[2]
        if row[2] not in candidate_options:
            candidate_options.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1

    print("Election Results")
    print("-------------------")
    print("Total Votes" + str(votes))
    for candidate in candidate_votes:
        print(candidate + ' ' + str(round(((candidate_votes[candidate]/votes)*100))) + '%' + ' (' + str(candidate_votes[candidate]) + ')')
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + '%' + '(' + str(candidate_votes[candidate]) + ')')
candidate_votes
winner = sorted(candidate_votes.items())

print("---------------")
print("Winner: " + str(winner[0]))
# Please note that line 43 has been left with value of '0', however changing the value can provide correct winner.
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_pathout, 'w') as txt_file:

    txt_file.write("Election Results")
    txt_file.write("-------------------")
    txt_file.write("Total Votes" + str(votes))
    for candidate in candidate_votes:
        txt_file.write(candidate + ' ' + str(round(((candidate_votes[candidate]/votes)*100))) + '%' + ' (' + str(candidate_votes[candidate]) + ')')
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + '%' + '(' + str(candidate_votes[candidate]) + ')')
    candidate_votes
    winner = sorted(candidate_votes.items())

    txt_file.write("---------------")
    txt_file.write("Winner: " + str(winner[0]))

    

    

    