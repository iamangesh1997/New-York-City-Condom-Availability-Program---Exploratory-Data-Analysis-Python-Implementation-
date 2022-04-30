#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[3]:


condom_data=pd.read_csv('nyc_condom_availablity.csv')


# In[4]:


condom_data.head()


# In[5]:


condom_data.tail()


# In[8]:


condom_data.shape


# In[9]:


condom_data.columns


# In[10]:


condom_data.info()


# In[11]:


condom_data.describe()


# In[12]:


condom_data.isnull().sum()


# In[17]:


condom_data=condom_data.drop(['BuildingNumber','Address 2','Phone','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Facility Type','Website'],axis=1)


# In[18]:


condom_data.head()


# In[19]:


condom_data.isnull().sum()


# In[20]:


condom_data.dropna(inplace=True)


# In[21]:


condom_data.shape


# In[22]:


condom_data['PartnerType'].unique()


# In[23]:


condom_data['PartnerType'].value_counts()


# In[26]:


plt.figure(figsize=(15,6))
sns.countplot('PartnerType',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[27]:


condom_data['PartnerTypeDetailed'].unique()


# In[29]:


condom_data['PartnerTypeDetailed'].value_counts()


# In[30]:


plt.figure(figsize=(15,6))
sns.countplot('PartnerTypeDetailed',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[32]:


condom_data['Condoms (Male)'].unique()


# In[33]:


condom_data['Condoms (Male)'].value_counts()


# In[34]:


plt.figure(figsize=(15,6))
sns.countplot('Condoms (Male)',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[38]:


colors=sns.color_palette('bright')
plt.pie(condom_data['Condoms (Male)'].value_counts(),colors=colors,autopct= '%0.0f%%',shadow='True',startangle=90)
plt.show()


# In[39]:


condom_data['FC2 (Female/Insertive Condoms)'].unique()


# In[40]:


condom_data['FC2 (Female/Insertive Condoms)'].value_counts()


# In[41]:


plt.figure(figsize=(15,6))
sns.countplot('FC2 (Female/Insertive Condoms)',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[42]:


colors=sns.color_palette('bright')
plt.pie(condom_data['FC2 (Female/Insertive Condoms)'].value_counts(),colors=colors,autopct= '%0.0f%%',shadow='True',startangle=90)
plt.show()


# In[43]:


condom_data['Community Board'].unique()


# In[44]:


condom_data['Community Board'].value_counts()


# In[45]:


plt.figure(figsize=(15,6))
sns.countplot('Community Board',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[46]:


condom_data['Council District'].unique()


# In[48]:


condom_data['Council District'].value_counts()


# In[49]:


plt.figure(figsize=(15,6))
sns.countplot('Council District',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[50]:


from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder


# In[53]:


condom_data['PartnerType'] = label_encoder.fit_transform(y=condom_data['PartnerType'])
condom_data['PartnerTypeDetailed'] = label_encoder.fit_transform(y=condom_data['PartnerTypeDetailed'])
condom_data['Condoms (Male)'] = label_encoder.fit_transform(y=condom_data['Condoms (Male)'])
condom_data['FC2 (Female/Insertive Condoms)'] = label_encoder.fit_transform(y=condom_data['FC2 (Female/Insertive Condoms)'])


# In[54]:


condom_data.head()


# In[55]:


plt.figure(figsize=(15,6))
sns.countplot(x='Condoms (Male)',hue='PartnerType',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[56]:


plt.figure(figsize=(15,6))
sns.countplot(x='FC2 (Female/Insertive Condoms)',hue='PartnerType',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[57]:


plt.figure(figsize=(15,6))
sns.countplot(x='PartnerTypeDetailed',hue='Condoms (Male)',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[58]:


plt.figure(figsize=(15,6))
sns.countplot(x='PartnerTypeDetailed',hue='FC2 (Female/Insertive Condoms)',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[59]:


plt.figure(figsize=(15,6))
sns.countplot(x='Community Board',hue='Condoms (Male)',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[60]:


plt.figure(figsize=(15,6))
sns.countplot(x='Community Board',hue='FC2 (Female/Insertive Condoms)',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[61]:


plt.figure(figsize=(15,6))
sns.countplot(x='Community Board',hue='Condoms (Male)',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[62]:


plt.figure(figsize=(15,6))
sns.countplot(x='Council District',hue='FC2 (Female/Insertive Condoms)',data=condom_data,palette='hls')
plt.xticks(rotation=90)
plt.show()


# In[ ]:




