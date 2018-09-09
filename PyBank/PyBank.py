
# coding: utf-8

# In[181]:


import os
import csv
from statistics import mean


# In[182]:


budget_data_csv = os.path.join('..', 'Users', 'ginaf', 'budget_data.csv')


# In[183]:


budget_data = "C:/Users/ginaf/budget_data.csv"


# In[184]:


with open (budget_data) as file:
    csvreader = csv.reader(file)

    next(csvreader)
    var = next(csvreader)
    ans = []

    for row in csvreader:
        #print(row)
        #print("this is var",var[1])
        #print("this is row",row[1])
        ans.append(int(row[1]) - int(var[1]))
        var = row

    #print(ans)


# In[185]:


avg=mean(ans)
#print(avg)


# In[186]:


with open(budget_data) as file:
    csvreader=csv.reader(file)
    next(csvreader)
    total = 0
    for row in csvreader:
        total += int(row[1])
    #print(total)
#stole this from stack overflow


# In[187]:


with open (budget_data) as file:
    csvreader = csv.reader(file)
    row_count = sum(1 for row in csvreader)


    #print(row_count)
#stole this from stack overflow too


# In[188]:


inc=max(ans)
#print(inc)
dec=min(ans)
#print(dec)


# In[189]:


print("Financial Analysis")
print("______________________")


# In[190]:


print("Total Months: ", (row_count-1))
#because the row_count includes the header, so I needed to subtract that out
print("Total: ", "$",total)
print("Average Change: ", "$",avg)
print("Greatest Increase: ", "($",inc,")")
print("Greatest Decrease: ", "($",dec,")")
