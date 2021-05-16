#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
netflix_raw_df=pd.read_csv('netflix_titles.csv')


# In[32]:


project_name = "Netflix_Show_Data_Analysis"


# In[33]:


# Data Preparation and Cleaning


# In[34]:


# Here, I have tried to clean the datset and fill the missing values with appropriate.


# In[35]:


netflix_raw_df.head()


# In[36]:


shape=netflix_raw_df.shape
print('The shape of the dataframe is {}'.format(shape))


# In[37]:


netflix_raw_df.info('all')


# In[38]:


netflix_raw_df.describe()


# In[39]:


netflix_raw_df.director.fillna('None',inplace=True)
netflix_raw_df.cast.fillna('None',inplace=True)
netflix_raw_df.country.fillna('None',inplace=True)
netflix_raw_df.dropna(subset=['date_added','rating'],inplace=True)


# In[40]:


# Exploratory Analysis and Visualisation


# In[41]:


# I have tried to devise various relationships between the columns using bar charts, stacked bar charts and other types of graph

# Let's begin by importingmatplotlib.pyplot and seaborn.


# In[42]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[43]:


#TODO - Number of Netflix movie titles which are either Movie or TV Show


# In[44]:


netflix_raw_df.type.value_counts().plot(kind='bar');
plt.title('Number of Netflix titles that are either Movie or TV Shows');
plt.ylabel('Frequency');


# In[45]:


#TODO - Most tiltes come under which rating


# In[46]:


plt.figure(figsize=(12,8))
sns.countplot(x='rating',data=netflix_raw_df);


# In[47]:


#TODO - Most Movie/ TV Show titles are given which rating


# In[48]:


plt.figure(figsize=(12,8))
sns.countplot('rating',data=netflix_raw_df,hue='type');


# In[49]:


#TODO- Which country had most releases


# In[50]:


get_ipython().system('pip install Wordcloud')
from wordcloud import WordCloud
plt.subplots(figsize=(25,15))
wordcloud = WordCloud(
                          background_color='white',
                          width=1920,
                          height=1080
                         ).generate(" ".join(netflix_raw_df.country))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('country.png')
plt.show();


# In[51]:


# Asking and answering Questions


# In[52]:


# Here, I have taken a look at some of the questions that I can answer


# In[53]:


# Q1: TODO - Total frequency of both the types


# In[54]:


type_count=netflix_raw_df[['type','show_id']].groupby('type').count().sort_values('type',ascending=True)
type_count


# In[55]:


# Q2: TODO - Find the longest and shortest movie as well as TV show


# In[56]:


longest_movie= netflix_raw_df.loc[netflix_raw_df.type=='Movie'].duration.str.replace('min','').astype(float).max()
shortest_movie= netflix_raw_df.loc[netflix_raw_df.type=='Movie'].duration.str.replace('min','').astype(float).min()
print("longest_movie is",longest_movie)  
print("shortest_movie is",shortest_movie)


# In[57]:


longest_tv_show=netflix_raw_df[netflix_raw_df.type=='TV Show'].duration.str.replace('min','').max()
shortest_tv_show=netflix_raw_df[netflix_raw_df.type=='TV Show'].duration.str.replace('min','').min()
print("longest_tv_show is",longest_tv_show)
print("shortest_tv_show is",shortest_tv_show)

