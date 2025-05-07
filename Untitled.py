#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -q kaggle')

get_ipython().system('kaggle datasets download -d ankitbansal06/retail-orders -f orders.csv')


# In[3]:


get_ipython().system('kaggle datasets download -d ankitbansal06/retail-orders -f orders.csv --force')


# In[14]:


import chardet

with open("orders.csv", 'rb') as f:
    raw = f.read(100000)
    enc = chardet.detect(raw)['encoding']
    


# In[11]:


import chardet

# Detect encoding by reading the first 100,000 bytes
with open("orders.csv", 'rb') as f:
    raw_data = f.read(100000)
    result = chardet.detect(raw_data)

print(result)


# In[12]:


with open("orders.csv", 'rb') as f:
    print(f.read(200))  # Print first 200 bytes


# In[15]:


import os
os.listdir()

import zipfile

with zipfile.ZipFile("orders.csv.zip", 'r') as zip_ref:
    zip_ref.extractall()
import pandas as pd

df = pd.read_csv("orders.csv")
df.head()


# In[18]:


import os

# List all files in the current working directory
os.listdir()


# In[19]:


import os

os.rename("orders.csv", "orders.zip")


# In[20]:


import zipfile

with zipfile.ZipFile("orders.zip", 'r') as zip_ref:
    zip_ref.extractall()


# In[24]:


import pandas as pd

df = pd.read_csv("orders.csv", na_values=['Not Available', 'unknown'])
df.head(20)
df['Ship Mode'].unique() 


# In[35]:


df.columns = df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.columns


# In[36]:


df.head(10)


# In[43]:


#df['discount']=df['list_price']*df['discount_percent']*.01
#df.head(5)
#df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df.head()


# In[49]:


df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
df.dtypes


# In[57]:


#df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
df.head()


# In[59]:


get_ipython().system('pip install sqlalchemy pymysql')


# In[67]:


from urllib.parse import quote_plus
from sqlalchemy import create_engine

user = "root"
raw_password = "Qwerty@1112"
password = quote_plus(raw_password)  # Automatically encodes '@' as '%40'
host = "localhost"
port = 3306
database = "retail"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")


# In[68]:


df.to_sql('df_orders', con=engine, index=False, if_exists='append')


# In[66]:


with engine.connect() as conn:
    result = conn.execute("SELECT DATABASE();")
    print("Connected to:", result.fetchone()[0])

