#!/usr/bin/env python
# coding: utf-8

# In[2]:



get_ipython().system('pip install Faker')

from random import randint
import pandas as pd
from faker import Faker
from faker.providers import DynamicProvider


# In[5]:


fake = Faker()


# In[19]:


import random

elements=["primary", "high school", "bachelor", "master", "phD"]

education_level=[]
for i in range(500):

    sample_education=random.sample(elements, k=1)
    education_level.append(sample_education[0])
    
    


# In[20]:


education_level

