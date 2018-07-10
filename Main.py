# Make all imports
import tweepy
import credentials as crd

# Load all options from options.csv
file = open('options.csv','r')

# Set up Twitter interaction
auth = tweepy.OAuthHandler(crd.consumer_key, crd.consumer_secret)
auth.set_access_token(crd.access_token, crd.access_token_secret)
api = tweepy.API(auth)

# TEST
user = api.me()
print (user.name)