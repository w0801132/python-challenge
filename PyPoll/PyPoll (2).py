
# coding: utf-8

# In[23]:


import os
import csv


# In[24]:


election_data_csv = os.path.join('..', 'Users', 'ginaf', 'election_data.csv')


# In[25]:


election_data = "C:/Users/ginaf/election_data.csv" 


# In[26]:


with open (election_data) as file:
    csvreader = csv.reader(file)
    header= next(csvreader)
    candidates = []
    for row in csvreader:
        column = row[2]
        if column != candidates:
            candidates.append(column)
    #I worked this out with the tutor, so I hope it's right
    


# In[27]:


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
    #same with this one


# In[28]:


print("Election Results")
print("______________________")


# In[29]:


with open (election_data) as file:
    csvreader = csv.reader(file)
    row_count = sum(1 for row in csvreader)
    totalvo=(row_count -1)
        
    #print(row_count)


# In[30]:


print(f"Total Votes: ", totalvo)
#print the dictionary? of candidate name, percentage of vote, and vote count       
print(candidates, candidates_vote)
print("__________________")
print(f"Winner: Khan")
print("__________________")    

