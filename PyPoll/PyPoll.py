
# coding: utf-8

# In[7]:


import os
import csv


# In[8]:


election_data_csv = os.path.join('..', 'Users', 'ginaf', 'election_data.csv')


# In[9]:


election_data = "C:/Users/ginaf/election_data.csv" 


# In[10]:


print("Election Results")
print("______________________")


# In[11]:


def getresults(votestuff):
    candidate = votestuff[2]
        
    totalvo = candidate.count(candidate)
    
    print(f"Total Votes: {totalvo}")
    #print the dictionary? of candidate name, percentage of vote, and vote count       
    print(f"")
    print("__________________")
    print(f"Winner: {()}")
    print("__________________")    


# In[12]:


with open(election_data, "r") as csvreader:
    election = csv.reader(csvreader, delimiter = ",")
    next(election)
    
    print(getresults)

