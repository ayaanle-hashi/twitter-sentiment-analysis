import tweepy
import os
from vader_analysis import sentiment_scores

auth=tweepy.OAuthHandler(os.getenv("consumer_key"),os.getenv("consumer_secret"))
auth.set_access_token(os.getenv("access_token"), os.getenv("access_token_secret"))
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

search = str(input("Please select your search term:"))
no_of_tweets=int(input("How many tweets should be analysed?: "))

positive = 0
negative = 0
neutral =  0

for tweet in tweepy.Cursor(api.search,q=search +" -filter:retweets",
                            lang="en").items(no_of_tweets):
        sentiment = sentiment_scores(tweet.text)

        positive += sentiment[0]
        negative += sentiment[1]
        neutral  += sentiment[2]

positive_percentage = int(positive/(negative+neutral+positive) * 100)
negative_percentage = int(negative/(negative+neutral+positive) * 100)
neutral_percentage =  int(neutral/(negative+neutral+positive) * 100)

if positive > negative and positive > neutral:
        print ("With" + ' {} '.format(str(no_of_tweets)) + "Tweets analysed " + search + " has a strong positive sentiment on Twitter \n")
        print('{}'.format(positive_percentage) + "% " + "of these tweets are postiive")

elif negative > positive and negative > neutral:
        print("With" + ' {} '.format(str(no_of_tweets)) + "Tweets analysed " + search + " has a strong negative sentiment on Twitter \n")
        print('{}'.format(negative_percentage) + "% " + "of these tweets are negative")

elif neutral > negative and positive > negative:
        print("With" + ' {} '.format(str(no_of_tweets)) + "Tweets analysed " + search + " has a weak positive sentiment on Twitter \n")
        print('{}'.format(positive_percentage) + "% " + "of these tweets are postiive")

elif neutral > positive and negative > positive:
        print("With" + ' {} '.format(str(no_of_tweets)) + "Tweets analysed " + search + " has a weak negative sentiment on Twitter \n")
        print('{}'.format(negative_percentage) + "% " + "of these tweets are negative")

elif neutral > (positive + negative):
        print ("With" + ' {} '.format(str(no_of_tweets)) + "Tweets analysed " + search + " has a general neutral sentiment on Twitter\n")
        print('{}'.format(neutral_percentage) + "% " + "of these tweets are neutral")