# -*- coding: utf-8 -*-
"""A2P3_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q5uaT2sKkwrh4FWo1jqrGhzRkEvCB_M5
"""

import torch
import torchtext
from torchtext import data
import torch.optim as optim
import argparse
import os
import pandas as pd

import random
import sklearn
from sklearn.model_selection import train_test_split
import csv
import matplotlib.pyplot as plt

"""#Creating Datasets"""

def get_random_data(df):
  i=random.randint(0,10000)
  return(df.iloc[i]['text'],df.iloc[i]['label'])

def check_data_split(X_train,Y_train,X_val,Y_val,X_test,Y_test): # function to check the datasets have been created correctly
  X_train_set=set(X_train)
  X_val_set=set(X_val)
  X_test_set=set(X_test)
  #check for common entries across data splits
  print('elements in common between train and the other 2 datasets-',X_train_set.intersection(X_val,X_test))
  print('elements in common between validation  and the test dataset-',X_val_set.intersection(X_test))

  #check for equal number of labels in data splits
  print('equal number of labels in the train set-' ,len(Y_train[Y_train==0])==len(Y_train[Y_train==1]))
  print('equal number of labels in the validation set-' ,len(Y_val[Y_val==0])==len(Y_val[Y_val==1]))
  print('equal number of labels in the test set-' ,len(Y_test[Y_test==0])==len(Y_test[Y_test==1]))

"""##overfit dataset"""

data_path = "/content/data.tsv"
df = pd.read_csv(os.path.join(data_path), sep="\t")

positive_samples=df[df['label'] == 1]

negetive_samples=df[df['label'] == 0]

positive= pd.concat([positive_samples.iloc[random.randint(0,4999)] for _ in range(25)],axis=1).T
negetive= pd.concat([negetive_samples.iloc[random.randint(0,4999)] for _ in range(25)],axis=1).T

overfit=pd.concat([positive,negetive])

overfit.to_csv("overfit.tsv", sep="\t")

print('equal number of labels in the overfit set-' ,len(overfit['label'][overfit['label']==0])==len(overfit['label'][overfit['label']==1]))

"""##Other datatsets"""

X=df['text']
Y=df['label']

X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.36, stratify=Y)

X_test, X_val, Y_test, Y_val = train_test_split(X_val, Y_val, test_size=0.4444, stratify=Y_val)

check_data_split(X_train,Y_train,X_val,Y_val,X_test,Y_test)

train=pd.concat([X_train, Y_train], axis = 1)
val=pd.concat([X_val, Y_val], axis = 1)
test=pd.concat([X_test, Y_test], axis = 1)

test.to_csv("test.tsv", sep="\t")
val.to_csv("val.tsv", sep="\t")
train.to_csv("train.tsv", sep="\t")