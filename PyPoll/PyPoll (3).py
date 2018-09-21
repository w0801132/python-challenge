
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd


# In[2]:


election_data_csv = os.path.join('..', 'Users', 'ginaf', 'election_data.csv')
file_to_output= os.path.join('C:/Users/ginaf/election_final.txt')


# In[8]:


election_data = "C:/Users/ginaf/election_data.csv" 


# In[9]:


# Total Vote Counter
totalvotes = 0

# Candidate Options and Vote Counters
candidates = []
candidatevotes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0


# In[10]:


# Read the csv and convert it into a list of dictionaries
with open (election_data) as file:
    csvreader = csv.reader(file)
    #read header
    header= next(csvreader)
    #candidates = []
    for row in csvreader:
        #What is "run the loader animation?"
        #print(". ", end=""),
        #add to the total vote count
        totalvotes= totalvotes + 1
        #extract candidate name from each row
        column = row[2]

        #looking for non-matching candidate names
        #if column != candidates:
        if column not in candidates:
            candidates.append(column)
            #I worked this out with the tutor, so I hope it's right
            candidatevotes[column]=0
            #then tracking each vote and adding it to the count
        candidatevotes[column]=candidatevotes[column] + 1
#         print("this is column",column)
#         print("this is candidates",candidates)
#         print("this is candidatevotes",candidatevotes)
#with open (election_data) as file:
    #csvreader = csv.reader(file)
    #header= next(csvreader)
    #candidates_vote = {}
    #for row in csvreader:
        #column = row[2]
        #if column != candidates:
            #candidates_vote[column]=0 
            #candidates.append(column)
    #candidates_vote[column]=candidates_vote[column]+1     
    #same with this one
file_to_output="C:/Users/ginaf/election.txt" 
# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:
    #I don't understand the above syntax
    # Print the final vote count (to terminal)
    election_final = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalvotes}\n"
        f"-------------------------\n")
    print(election_final, end="")

    # Save the final vote count to the text file
    txt_file.write(election_final)

    # Determine the winner by looping through the counts
    for column in candidatevotes:

        # Retrieve vote count and percentage
        votes = candidatevotes.get(column)
        vote_percentage = float(votes) / float(totalvotes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = column

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{column}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)


# In[11]:


#with open (election_data) as file:
    #csvreader = csv.reader(file)
    #header= next(csvreader)
    #candidates_vote = {}
    #for row in csvreader:
        #column = row[2]
        #if column != candidates:
            #candidates_vote[column]=0 
            #candidates.append(column)
    #candidates_vote[column]=candidates_vote[column]+1     
    #same with this one
#file_to_output= os.path.join('..', 'Users', 'ginaf', 'election_final.txt')    
# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:
    #I don't understand the above syntax
    # Print the final vote count (to terminal)
    election_final = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalvotes}\n"
        f"-------------------------\n")
    print(election_final, end="")

    # Save the final vote count to the text file
    txt_file.write(election_final)

    # Determine the winner by looping through the counts
    for column in candidatevotes:

        # Retrieve vote count and percentage
        votes = candidatevotes.get(column)
        vote_percentage = float(votes) / float(totalvotes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = column

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{column}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)


# In[ ]:


#print("Election Results")
#print("______________________")


# In[ ]:


#with open (election_data) as file:
    #csvreader = csv.reader(file)
    #row_count = sum(1 for row in csvreader)
    #totalvo=(row_count -1)
        
    #print(row_count)


# In[ ]:


#print(f"Total Votes: ", totalvo)
#print the dictionary? of candidate name, percentage of vote, and vote count       
#print(candidates, candidates_vote)
#print("__________________")
#print(f"Winner: Khan")
#print("__________________")    

