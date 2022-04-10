import os
import pandas as pd

#---------------------------------------------------------------------------------------------------------------------------------------
#AUTHOR: Anton Dahl
#LICENSE: MIT
#---------------------------------------------------------------------------------------------------------------------------------------

# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --max-results 10000 --since 2016-03-09 twitter-search 'Garo AB until:2016-03-16' > ../TwitterScrape/json-files/Garo.json")

# Reads from the json generated from the CLI commands above and creates a pandas dataframe object
tweets_df = pd.read_json('../TwitterScrape/json-files/Garo.json', lines=True)

tweets_df_processing = tweets_df[['date','content','id','likeCount','retweetCount','retweetedTweet','user']]

#The following functions are used to extract relevant attributes from the object 'user' in tweets_df_processing
def get_username(user):
    try:
        return user['username']
    except Exception:
        return 'n/a'

def get_verified(user):
    try:
        return user['verified']
    except Exception:
        return 'n/a'

def get_followersCount(user):
    try:
        return user['followersCount']
    except Exception:
        return 'n/a'

#calling functions to extract attributes from 'user'
tweets_df_processing['username'] = tweets_df_processing['user'].apply(get_username)
tweets_df_processing['verified'] = tweets_df_processing['user'].apply(get_verified)
tweets_df_processing['followersCount'] = tweets_df_processing['user'].apply(get_followersCount)

#remove 'user' object from the dataframe
tweets_df_clean = tweets_df_processing[['date','content','id','likeCount','retweetCount','retweetedTweet','username','verified','followersCount']]

#convert dataframe object into csv format and export to local machine as <filename.csv>
tweets_df_clean.to_csv('../TwitterScrape/csv-files/Garo.csv')

#check if we can convert csv back to pandas dataframe without problems
new_df = pd.read_csv('../TwitterScrape/csv-files/Garo.csv', index_col=[0])

print(new_df)




    
