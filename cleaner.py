import pandas as pd
import numpy as numpy
import re
dataset = pd.read_csv('base_data.csv')

features = [ 'title', 'category', 'author']
#preprocessing all the attributes and combining them together 

def join_attr(row):
    s = ((row['title']+" "+row['category']+" "+row['author']).lower())
    s = " ".join(list(set(re.sub(r'[^\w\s]*','', s).split())))
    return s

dataset["combine_features"] = dataset.apply(join_attr, axis=1)
dataset = dataset.drop(['title','category','author'], axis=1)
dataset.to_csv("preprocessed_yt_data.csv")