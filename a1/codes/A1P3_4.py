# -*- coding: utf-8 -*-
"""A1P3_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wao8AFKWr8EI1a4RxeWf2_BgjBSUHT1Q
"""

from collections import Counter
import numpy as np
import torch
import spacy
from sklearn.model_selection import train_test_split

import itertools
import random
import torch.optim as optim
import matplotlib.pyplot as plt

class Word2vecModel(torch.nn.Module):
    def __init__(self, vocab_size, embedding_size,i2v,v2i):
        super().__init__()
        # initialize word vectors to random numbers 
        self.word_vectors=[]
        for _ in range(vocab_size):
          vectors=[random.random() for _ in range(embedding_size)]
          self.word_vectors.append(vectors)
        self.vocab_size=vocab_size
        self.embedding_size= embedding_size
        self.v2i=v2i
        self.i2v=i2v
        self.embedding=torch.nn.Embedding(self.vocab_size,self.embedding_size)
        self.out=torch.nn.Linear(self.embedding_size,self.vocab_size)
        
    def forward(self, x):
        """
        x: torch.tensor of shape (bsz), bsz is the batch size
        """
        #TO DO
        e=self.embedding(x)
        logits=self.out(e)
        out=torch.nn.functional.log_softmax(logits, dim=1)
        
        return out