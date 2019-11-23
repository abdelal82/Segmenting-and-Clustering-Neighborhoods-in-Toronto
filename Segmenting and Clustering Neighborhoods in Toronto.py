#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data= pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")


# In[4]:


type(data)


# In[5]:


data[0]


# In[27]:


table=data[0]


# In[28]:


type(table)


# In[31]:


table.shape


# In[32]:


tabel.info()


# In[35]:


tabel.head()


# In[42]:


tabel[~(tabel['Borough']=='Not assigned')]


# In[51]:


tabel1=tabel[~(tabel['Borough']=='Not assigned')]


# In[52]:


tabel1


# In[55]:


tabel1.shape


# In[74]:


tabel1.iloc[4,0:2]


# In[80]:


tabel2 = tabel1.groupby(by=['Postcode','Borough']).agg(lambda x: ','.join(x))


# In[81]:


tabel2


# In[82]:


tabel2.reset_index(level=['Postcode','Borough'], inplace=True)


# In[83]:


tabel2


# In[99]:


tabel2.shape


# In[278]:


tabel2.head()


# In[98]:


geo=("http://cocl.us/Geospatial_data")


# In[175]:


cordinat= pd.read_csv("http://cocl.us/Geospatial_data")


# In[101]:


cordinat


# In[279]:


cordinate2 = cordinat.rename({'Postal Code':'Postcode'}, axis=1)


# In[227]:


cordinate2


# In[281]:


df = tabel2.merge(cordinate2,on='Postcode')


# In[282]:


df


# In[ ]:




