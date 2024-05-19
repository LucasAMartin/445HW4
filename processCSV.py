# Python File that will filter TweetsElonMusk.csv to produce a dictionary of the frequency of each word.
# Author: Elijah Johnson

#import
import csv
import pandas as pd
import re
from nltk.corpus import stopwords

#set stopwords
stop_words = set(stopwords.words("english"))

# preliminary dictionary declaration
res = {}

# open the csv file with elon's tweets
with open("TweetsElonMusk.csv", "r", encoding="utf-8") as file:
    # create a csv reader
    reader = csv.reader(file)
    # skip the first row because it is just headers
    headers = next(reader)
    # go through every row and store specifically the column that contains his tweets
    # and update the dictionary with the frequency of each word
    for row in reader:
        tweet = row[10]
        tweet = tweet.lower()
        tweet = tweet.replace("\"", "")
        words = re.split(r'[~!#$%^&*()-=+`\\/?.,><;:{}\[\]\s+\“\”]\s*', tweet)
        for word in words:
            if word not in stop_words:
                res[word] = res.get(word, 0) + 1

# create csv of all the words and their frequencies
# at this point, the csv contains every word
# no cleaning has happened
with open("elonDict.csv", "w", encoding="utf-8") as f:
    f.write("word,frequency\n")
    for key in res.keys():
        f.write("%s,%s\n"%(key,res[key]))

# CLEANING
df = pd.read_csv("elonDict.csv", encoding="utf-8")
df = df.dropna()
df = df[df["word"].str.isalpha()]
df.drop((df[df["frequency"] < 55].index), inplace=True)
df = df.sort_values(by='frequency', ascending=False)
df.to_csv("elonDictSorted.csv", index=False, encoding="utf-8")