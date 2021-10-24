'''
nltk library used to process human language
sentiment analysis involves analysing whether a piece of text is
positive, negative or neutral

VADER - Valence Aware Dictionary and Sentiment Reasoner
it also takes into account the intensity of the sentiment

Download VADER lexicon: it acts as a dictionary here
'''
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')

file = 'data_file.xlsx'
#read from excel
xl = pd.ExcelFile(file)
#parsing the excel sheet to data frame
dfs = xl.parse(xl.sheet_names[0])
#removes the blank rows from the data frame
dfs = list(dfs['Timeline'])
print(dfs)
sid = SentimentIntensityAnalyzer()
str1 = "UTC+05:30"
for data in dfs:
    a = data.find(str1)
    if(a == -1):
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k, ss[k])










