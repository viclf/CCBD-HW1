Cloud Computing HW1 


Working on this assignment:
vf2221 victor Ferrand
pwn2107 Peter Wakahiu Njenga


This is a tweet map using google map API and Twitter Public stream API
tweetmap.png shows how it looks like (with very few data points - testing phase !)
halloween.png shows a search with the hashtag #halloween for the last 24h.

Tweet Stream
an EC2 instance is running on the background with a java program that streams and uploads the tweets in the DynamoDB TweetsTable.
Source: Tweetsteamer folder



Database
We implemented a DynamoDB database to store the tweets with the relevant values we needed
Our database is about 40MB large for now (4 days of stream) and still growing!
Normally should approximate the 100MB at the end of the weekend.



App
This application is kind of live as it keeps track of new tweets every % seconds.
It displays only the tweets from the last hour (otherwise the map is not readable !)

The application was built using Flask framework on the server side.
There are two scripts setup.py and push.py. They create programmatically a new elastic bean stalk  environment/application(with the option provided) and launch it, and also push it (git) for updates. The program is calling command line functions to launch it with the AWS elastic beanStalk CLI.

The search function is looking for tweets by hashtags and display them on the map (only tweets from the past 24h).
Each tweet is readable on the map by clicking on it.
To go back to the main map, just enter an empty search.

The map is kind of a density map as the tweet's markers have been made transparents. The superposition of those  gives a darker color which provides an idea of the tweet's density !

Link to application: http://ccbd-hw1-env-fmvbmm7vhj.elasticbeanstalk.com/



Github source code:
https://github.com/viclf/CCBD-HW1
Keys have been removed from the python files for security purposes
