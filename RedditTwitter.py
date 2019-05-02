import tweepy
import praw

#Twitter tokens handled by tweepy. Enter yours here:
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Set up your tokens for PRAW
reddit = praw.Reddit(client_id='',
    client_secret='',
    user_agent='',)
#print(reddit.read_only)

#Choose the subreddit you want to scrape.
subreddit = reddit.subreddit('calvinandhobbes')

#Console message for error checking.
print("Today's top post on /r/" + subreddit.display_name + ":")
#print(subreddit.description)

#Choose the top post(s) of the day, limited to top 1.
top_daily = subreddit.top(time_filter='day', limit=1)

#Characters remaining for tweet (140 char). A little too hardcoded, replace with variables.
char_limit = 140 - 24 -2 #Twitter alters the URL to 23 characters, plus a space and two quotation marks

#Initialize variables.
post_title = []
post_url = []

#Grab title and URL of the top post. Maybe grab permalink instead.
for submission in top_daily:
    post_title = submission.title
    post_url = submission.url

#Shorten the title length and concatenate ellipsis if too long. 
#Make this a method!
print(len(post_title)) #For debugging purposes
if len(post_title) > char_limit:
    post_title=post_title[:char_limit-3] + "..."
print(post_title) #Just double checking we shortened it correctly.

#Let's string together our tweet.
tweet = '"' + post_title + '"' + " " + post_url
print(tweet) #Debugging
api.update_status(tweet)
