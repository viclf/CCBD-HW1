import flask
from dynamoDB import DynamoDB
from flask import Flask, render_template, request, session, flash, redirect, jsonify, json
from tweet import Tweet
from datetime import datetime
from flask import request, Response


#init
application = flask.Flask(__name__)
application.debug=True


#Connect the Dynamo DB and get the Tweets Table
DB = DynamoDB('keyID','privateKey','us-east-1','TweetsTable')
tweets = DB.getTweetsForView()

#fill with bs example 
#tweet1 = Tweet('1','ahha #ah','usr','40.809107','-73.961068',str(datetime.now()),'userid1')
#tweet2 = Tweet('2','ahho','usr2','40.780728','-73.953032',str(datetime.now()),'userid1')
#tweet3 = Tweet('3','ohho #yo','usr2','40.780728','-74.953032',str(datetime.now()),'userid1')
#DB.addToTweetsTable(tweet1)
#DB.addToTweetsTable(tweet2)
#DB.addToTweetsTable(tweet3)



#application
@application.route('/')
def displayTweets():
    tweets = DB.getTweetsForView()
    return render_template('index.html',tweets=json.dumps(tweets))


@application.route('/',methods=['POST','GET'])
def searchTweets():
    search = request.form['searchTweets']
    tweets = DB.getTweetsBySearch(search)
    return render_template('index.html',tweets=json.dumps(tweets))

#DB check for for new tweets
@application.context_processor
def my_utility_processor():
    def getNewTweets():
        tweetsbis = DB.getTweetsForView()
        newtweets=[item for item in tweetsbis if item not in tweets]
        newtweets=json.dumps(newtweets)
        print "OK"
        return newtweets
    return dict(getNewTweets=getNewTweets)

if __name__ == '__main__':
    application.run(host='localhost')

