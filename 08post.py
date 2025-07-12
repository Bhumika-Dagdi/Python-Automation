import tweepy

api_key = input("Enter your Twitter API key: ")
api_secret = input("Enter your Twitter API secret: ")
access_token = input("Enter your Twitter access token: ")
access_token_secret = input("Enter your Twitter access token: ")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

tweet = "Hello Twitter from Python!"
api.update_status(tweet)

print("Tweet posted!")
