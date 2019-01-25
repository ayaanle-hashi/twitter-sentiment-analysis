import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()


# class sentiment_score:

                
#         def sentiment_scores(self,sentence):
#                 self.sentence = sentence
#                 snt = sia.polarity_scores(sentence)
#                 print(sentence + "\n")
    
#                 neg,neu,pos,compound = snt.values()
#                 positive = 0
#                 neutral =  0
#                 negative = 0

#                 if pos > neg and pos > neu:
#                         positive += 1
#                 elif neg > pos and neg > neu:
#                         negative += 1
#                 elif neu > pos and neg > pos:
#                         negative += 1
#                 elif neu > neg and pos > neg:
#                         positive += 1  
#                 elif neu == 1.0:
#                         neutral += 1
#                 return [positive,negative,neutral]

#         def sentiment(self,sentiment_value):
#                 self.sentiment_value = sentiment_value
#                 if sentiment_value = 'strpos':
#                         print()







def sentiment_scores(sentence):
    snt = sia.polarity_scores(sentence)
    print(sentence + "\n")
    
    neg,neu,pos,compound = snt.values()
    positive = 0
    neutral =  0
    negative = 0

    if pos > neg and pos > neu:
            positive += 1
    elif neg > pos and neg > neu:
            negative += 1
    elif neu > pos and neg > pos:
            negative += 1
    elif neu > neg and pos > neg:
             positive += 1  
    elif neu == 1.0:
            neutral += 1
    return [positive,negative,neutral]
