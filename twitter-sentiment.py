import tweepy
import os
from vader_analysis import sentiment_scores
from matplotlib import pyplot as plt

auth=tweepy.OAuthHandler(os.getenv("consumer_key"),os.getenv("consumer_secret"))
auth.set_access_token(os.getenv("access_token"), os.getenv("access_token_secret"))
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

plt.style.use('seaborn-white')

search = str(input("Please select your search term:"))
no_of_tweets=int(input("How many tweets should be analysed?: "))

positive = 0
negative = 0
neutral  = 0

for tweet in tweepy.Cursor(api.search,q=search +" -filter:retweets",
                            lang="en").items(no_of_tweets):
        sentiment = sentiment_scores(tweet.text)

        positive += sentiment[0]
        negative += sentiment[1]
        neutral  += sentiment[2]

positive_percentage = int(positive/(negative+neutral+positive) * 100)
negative_percentage = int(negative/(negative+neutral+positive) * 100)
neutral_percentage =  int(neutral/(negative+neutral+positive) * 100)

print(positive,negative,neutral)

if positive > negative and positive > neutral and (positive - negative) > 10 and (positive - neutral) > 15:
        print ("With" + ' {} '.format(no_of_tweets) + "Tweets analysed " + search + " has a strong positive sentiment on Twitter \n")
        print('{}'.format(positive_percentage) + "% " + "of these tweets are postiive")

elif negative > positive and negative > neutral and (negative - positive) > 10 and (negative - neutral) > 15:
        print("With" + ' {} '.format(no_of_tweets) + "Tweets analysed " + search + " has a strong negative sentiment on Twitter \n")
        print('{}'.format(negative_percentage) + "% " + "of these tweets are negative")

elif neutral > negative and positive > negative or positive >= neutral and positive > negative:
        print("With" + ' {} '.format(no_of_tweets) + "Tweets analysed " + search + " has a weak positive sentiment on Twitter \n")
        print('{}'.format(positive_percentage) + "% " + "of these tweets are postiive")

elif neutral > positive and negative > positive or negative >= neutral and negative > positive:
        print("With" + ' {} '.format(no_of_tweets) + "Tweets analysed " + search + " has a weak negative sentiment on Twitter \n")
        print('{}'.format(negative_percentage) + "% " + "of these tweets are negative")

elif neutral > (positive + negative):
        print ("With" + ' {} '.format(no_of_tweets) + "Tweets analysed " + search + " has a general neutral sentiment on Twitter\n")
        print('{}'.format(neutral_percentage) + "% " + "of these tweets are neutral")

labels = 'Postive','Negative','Neutral'

percentages = [positive_percentage,negative_percentage,neutral_percentage]

fig1,ax1 = plt.subplots()

plt.title("Sentiment Percentages of {}".format(search))

ax1.pie(percentages,labels=labels,autopct='%1.1f%%')

ax1.axis('equal')

plt.show()