
# coding: utf-8

# In[68]:


import os
import csv


# In[69]:


budget_data_csv = os.path.join('..', 'Users', 'ginaf', 'budget_data.csv')


# In[70]:


budget_data = "C:/Users/ginaf/budget_data.csv" 


# In[71]:


print("Financial Analysis")
print("______________________")


# In[72]:


def getdata(budgetstuff):
    date = budgetstuff[0]
    money = int(budgetstuff[1])
    
    totalmo = date.count(date)
    totalcash = sum(money)
    aver = mean(money)
           
    print(f"Total Months: {totalmo}")
    print(f"Total: {(totalcash)}")
    print(f"Average Change: {(aver)}")


# In[74]:


with open(budget_data, "r") as csvreader:
    budget = csv.reader(csvreader, delimiter = ",")
    next(budget)
    
    print(getdata)

