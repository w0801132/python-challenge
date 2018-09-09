
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


election_data_csv = os.path.join('..', 'Users', 'ginaf', 'election_data.csv')


# In[3]:


election_data = "C:/Users/ginaf/election_data.csv"


# In[5]:


with open (election_data) as file:
    csvreader = csv.reader(file)
    header= next(csvreader)
    candidates = []
    for row in csvreader:
        column = row[2]
        if column != candidates:
            candidates.append(column)
    #print(candidates)



# In[ ]:


with open (election_data) as file:
    csvreader = csv.reader(file)
    header= next(csvreader)
    candidates_vote = {}
    for row in csvreader:
        column = row[2]
        if column != candidates:
            candidates_vote[column]=0
            candidates.append(column)
    candidates_vote[column]=candidates_vote[column]+1


# In[7]:


print("Election Results")
print("______________________")


# In[8]:


def getresults(votestuff):
    candidate = votestuff[2]

    totalvo = candidate.count(candidate)

    print(f"Total Votes: {totalvo}")
    #print the dictionary? of candidate name, percentage of vote, and vote count
    print(f"")
    print("__________________")
    print(f"Winner: {()}")
    print("__________________")


# In[9]:


with open (election_data) as file:
    csvreader = csv.reader(file)
    row_count = sum(1 for row in csvreader)


    print(row_count)
