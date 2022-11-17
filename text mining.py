# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:21:31 2022

@author: Gopinath
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import string # special operations on strings
import spacy # language models
import string

from matplotlib.pyplot import imread
from matplotlib import pyplot as plt
import seaborn as sns
from wordcloud import WordCloud,STOPWORDS
%matplotlib inline
from matplotlib.pyplot import imread
tweets=pd.read_csv("Elon_musk.csv",encoding='latin1',error_bad_lines=False,index_col=0)
#error_bad_lines=False means where there is empty lines just ignore that making it False
tweets
tweets=[Text.strip() for Text in tweets.Text] # remove both the leading and the trailing characters
tweets=[Text for Text in tweets if Text] # removes empty strings, because they are considered in Python as False
tweets[0:10]
# Joining the list into one string/text
tweets_text=' '.join(tweets)
tweets_text




