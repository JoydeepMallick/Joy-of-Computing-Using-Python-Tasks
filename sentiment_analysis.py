'''
please note this wont rn withour the excel file
nltk is not installed moreover

please see the screen shot for refernce
'''

import pandas as pd
import nltk # not in pc
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download("vader_lexicon")

file = "" # locaiton of excel file
xl = pd.ExcelFile(file) # read the excel file

'''
pandas provideS facilties of dataframes which is a 2 dimensional structure of
representing data
'''
dfs = xl.parse(xl.sheet_names[0]) # parsing excel sheet to data 

'''
We will work on timeline column of datframe hence ocnverting it into list
'''
dfs = list(dfs["Timeline"]) # removes blank rows(maybe blank line indicates new data)
print(dfs) # removes blank rows of data

sid = SentimentIntensityAnalyzer() # intializing sentiment analyzer

str1="UTC+05:30" # skipping the time dtaa of row form sentiment analysus
for data in dfs:
    a = data.find(str1)
    if a == -1 : # not found
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])

