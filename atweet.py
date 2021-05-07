import tweepy

auth = tweepy.OAuthHandler("API key", "API key secret")
auth.set_access_token("access token", "access token secret")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication ok")
except:
    print("Error during authentication")

try:
    api.update_status("Tweeting from Tweepy Python @ytbryan")
    print("tweeted")
except:
    print("Error creating a tweet")
