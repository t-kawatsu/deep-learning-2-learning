#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd

dataset_dir = os.path.dirname(os.path.abspath(__file__))

def load_recipes():
    return pd.read_json(dataset_dir + "/kurashiru-recipes.jsonl", lines=True)
    

