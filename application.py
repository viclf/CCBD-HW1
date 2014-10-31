import flask
from dynamoDB import DynamoDB
from flask import Flask, render_template, request, session, flash, redirect, jsonify, json
from datetime import datetime
from flask import request, Response
import time


#init
application = flask.Flask(__name__)
application.debug=True


#Connect the Dynamo DB and get the Tweets Table
DB = DynamoDB('..','..','us-east-1','TweetsTable')

#instantiate tweets arrays
tweets = []
newtweets=[]

#application
@application.route('/')
def displayTweets():
    searchbool=0
    global tweets
    tweets = DB.getTweetsForView()
    return render_template('index.html',tweets=json.dumps(tweets),searchbool=searchbool)

#search
@application.route('/search',methods=['POST','GET'])
def searchTweets():
    search = request.form['searchTweets']
    searchbool=0
    if search!='':
        searchbool=1
        global tweets
        tweets = DB.getTweetsBySearch(search)
    return render_template('index.html',tweets=json.dumps(tweets),searchbool=searchbool)

#DB check for for new tweets
@application.route('/stream',methods = ['POST','GET'])
def getNewTweets():
    tweetsbis = DB.getTweetsForView()
    global newtweets
    newtweets=[]
    if len(tweetsbis)!=len(tweets):
        print "new tweets"
        global newtweets
        newtweets=[item for item in tweetsbis if item not in tweets]
        global tweets
        tweets = tweetsbis
    return jsonify(newtweets=newtweets)


if __name__ == '__main__':
    global tweets
    global newtweets
    application.run(host='0.0.0.0')

