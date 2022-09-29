import snscrape.modules.twitter as sntwitter
import pandas as pd

query="python"
tweets=[]
limits=100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
     #print(vars(tweet))
     #break
     if len(tweets)==  limits:
        break
     else:
    
        tweets.append([tweet.date,tweet.user.username,tweet.content])
        df=pd.DataFrame(tweets,columns=['Date','User','Tweet'])
        print(df)
