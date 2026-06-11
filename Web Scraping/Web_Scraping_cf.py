#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests as re
from bs4 import BeautifulSoup
import regex as p
from typing import List
import pandas as pd
url="https://codeforces.com/contest/2234/standings"
r=re.get(url)
print(r)
s=BeautifulSoup(r.text,'lxml')

# In[11]:


x=s.table.tr.find_all('th')
columns=[col.get_text(strip=True) for col in x]
y=len(s.body.find('div',class_="custom-links-pagination").find_all("nobr"))


# In[12]:


list1=[]
i=1
while i<=y:
    url1=f"{url}/page/{i}"
    r=re.get(url1)
    s=BeautifulSoup(r.text,"lxml")
    k=s.body.table.find_all('tr')
    j=1
    while j<len(k)-1:
        list1.append([p.sub("\d{2}:\d{2}","",col.get_text(strip=True)) for col in k[j].find_all('td')])
        j+=1
    print(f"Page {i} done")
    i+=1


# In[13]:


c=list(zip(*list1))


# In[15]:


data={}
i=0
for a in columns:
    if i==1:
        data[a]=list(c[1])
    else:
        data[a]=[int(x) if len(x)>0 else None for x in list(c[i])]
    i+=1
df=pd.DataFrame(data)


# In[17]:


df.to_excel("codeforces_scraped_xd.xlsx",index=False,engine="openpyxl")

