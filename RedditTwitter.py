import tweepy
import praw

#Twitter tokens handled by tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

reddit = praw.Reddit(client_id='',
    client_secret='',
    user_agent='',)
#print(reddit.read_only)

subreddit = reddit.subreddit('calvinandhobbes')

print("Today's top post on /r/" + subreddit.display_name + ":")
#print(subreddit.description)

top_daily = subreddit.top(time_filter='day', limit=1)

char_limit = 140 - 24 -2 #Twitter alters the URL to 23 characters, plus a space and two quotation marks
post_title = []
post_url = []

for submission in top_daily:
    post_title = submission.title
    post_url = submission.url

print(len(post_title))
if len(post_title) > char_limit:
    post_title=post_title[:char_limit-3] + "..."
print(post_title)

tweet = '"' + post_title + '"' + " " + post_url
print(tweet)
api.update_status(tweet)
