# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initializing the count variable to count up the votes 
total_votes = 0 
#Initializing the candidate options list 
candidate_options = []
#creating the dictionary of each candidates and votes
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # Go through all the rows in the file 
    for row in file_reader:
        #Increase the vote count everytime a new vote is found
        total_votes += 1
        #Printing candidate names from each row 
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #Add new candidates 
            candidate_options.append(candidate_name)
            #Tracking candidates votes 
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
        # Print the candidate list.
        #print(candidate_votes)
        #Iterating through the candidate list
        for candidate_name in candidate_votes:
            #Retrieving votes for each candidate 
            votes = candidate_votes[candidate_name]
            votes_percentage = float(votes)/float(total_votes)*100
            #Printinf candidates and their vote percentages 
            #print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
            #print(f"{candidate_name}: rececived {votes_percentage} of the votes.")
            if (votes > winning_count) and (votes_percentage > winning_percentage):
                #iff true then set winning_count = votes and winning_percent = # vote_percentage.
                winning_count = votes
                winning_percentage = votes_percentage
                #Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)

