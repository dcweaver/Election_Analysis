#  The Data we need to retrieve 
# 1. The number of votes cast
# 2. a complete list of cadidates who received votes 
#3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize vote counter
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

#open election results and read file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:

        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            #add the candidate name to candidate list
            candidate_options.append(candidate_name)
            #begin tallying votes
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1   

# print ("The total votes cast was", + total_votes)
print(candidate_votes)
    # Print the file object.
     #print(election_data)

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Counties in the election\n-----------------------\nArapahoe\nDenver\nJefferson")

