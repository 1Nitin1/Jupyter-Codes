#!/usr/bin/env python
# coding: utf-8

# In[46]:


import requests as re
from bs4 import BeautifulSoup
import regex as p
from typing import List
import pandas as pd
url="https://codeforces.com/api/contest.standings?contestId=2234"
r=re.get(url)


# In[47]:


k=r.json()
problems=k['result']['problems']
list1=["Rank","ID","Score"]
for a in problems:
    list1.append(f"{a['index']} : {int(a['points'])}")


# In[48]:


rows=k['result']['rows']
def createList(x):
    l=[]
    l.append(int(x['rank']))
    l.append(x['party']['members'][0]['handle'])
    l.append(int(x['points']))
    y=x['problemResults']
    for a in y:
        z=int(a['points'])
        if z==0:
            z=int(a['rejectedAttemptCount'])
            if z==0:
                l.append(None)
            else:
                l.append(-z)
        else:
            l.append(z)
    return l
myList = []
for a in rows:
    myList.append(createList(a))


# In[49]:


c=list(zip(*myList))
i=0
data={}
for a in list1:
    data[a]=c[i]
    i+=1
df=pd.DataFrame(data)
print(df.head(20))


# In[50]:


df.to_excel("codeforces_scraped_xd_api.xlsx",index=False,engine="openpyxl")


# In[ ]:




