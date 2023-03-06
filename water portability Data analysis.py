#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[5]:


data = pd.read_csv(r'C:\Users\Admin\Desktop\csv files\water_potability.csv')
data.head(5)


# In[6]:


data.describe()


# In[7]:


data.info()


# In[8]:


d = pd.DataFrame(data["Potability"].value_counts())
fig = px.pie(d, values = "Potability", names = ["Not Potable", "Potable"], hole = 0.35, opacity = 0.8,
            labels = {"label" :"Potability","Potability":"Number of Samples"})
fig.update_layout(title = dict(text = "Pie Chart of Potability Feature"))
fig.update_traces(textposition = "outside", textinfo = "percent+label")
fig.show()


# In[9]:


data.corr()


# In[10]:


sns.clustermap(data.corr(), cmap = "vlag", dendrogram_ratio = (0.1, 0.2), annot=True, linewidths = .8, figsize = (9,10))
plt.show()


# In[18]:


non_potable = data.query("Potability == 0")
potable = data.query("Potability == 1")

plt.figure(figsize = (15,15))
for ax, col in enumerate(data.columns[:9]):
    plt.subplot(3,3, ax + 1)
    plt.title(col)
    sns.kdeplot(x = non_potable[col], label = "Non Potable")
    sns.kdeplot(x = potable[col], label = "Potable")
    plt.legend()
plt.tight_layout()


# In[21]:


data.isnull().sum()


# In[22]:


data["ph"].fillna(value = data["ph"].mean(), inplace = True)
data["Sulfate"].fillna(value = data["Sulfate"].mean(), inplace = True)
data["Trihalomethanes"].fillna(value = data["Trihalomethanes"].mean(), inplace = True)


# In[23]:


data.isnull().sum()


# In[24]:





# In[ ]:





# In[ ]:




