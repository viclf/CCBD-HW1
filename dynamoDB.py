import boto
from boto.dynamodb2 import connect_to_region
from boto.dynamodb2.items   import Item
from boto.dynamodb2.table   import Table
import time
from datetime import datetime

class DynamoDB:

    def __init__(self, keyid, secretkey,region,name,endpoint=None, port=None):
        self.tweetsTable = None
        self.db = None
        
        if endpoint is None:
            endpoint = 'localhost'
        if port is None:
            port = 8000
        
        self.db = connect_to_region(region, aws_access_key_id=keyid, aws_secret_access_key=secretkey)
        self.tweetsTable = Table(name,connection=self.db)


    def addToTweetsTable(self,tweet):
        tweetItem = Item(self.tweetsTable, data= {
                    "TweetID"  :tweet.keyid,
                    "text"     : tweet.text,
                    "longitude"     : tweet.long,
                    "latitude"      : tweet.lat,
                    "time"     : tweet.timeStamp,
                    "screenName"     : tweet.user,
                    })
        return tweetItem.save(overwrite=True)
    

    def getTweetsForView(self):
        tweets=[]
        result = self.tweetsTable.scan()
        timenow = time.time()
        for x in result:
            timetweet=self.set_date(x['time'])
            if x['latitude']!=None and timenow+14400-timetweet<2000:
                tweets.append([float(str(x['latitude'])),float(str(x['longitude'])),x['text']])
        return tweets


    def getTweetsBySearch(self,search):
        tweets=[]
        search='#'+search
        result = self.tweetsTable.scan()
        for x in result:
            if x['latitude']!=None and x['longitude']!=None:
                if search in x['text']:
                    tweets.append([float(str(x['latitude'])),float(str(x['longitude'])),x['text']])
        return tweets


    def set_date(self, date_str):
        time_struct = time.strptime(date_str, "%a %b %d %H:%M:%S UTC %Y")
        date = time.mktime(time_struct)
        return date





