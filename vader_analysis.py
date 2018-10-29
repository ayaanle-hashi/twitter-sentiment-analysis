import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()

def sentiment_scores(sentence):
    snt = sia.polarity_scores(sentence)
    print(sentence + "\n")
    
    neg,neu,pos,compound = snt.values()
    positive = 0
    neutral =  0
    negative = 0

    if pos > neg and pos > neu:
            positive =+ 1
    elif neg > pos and neg > neu:
            negative =+ 1
    elif neu > pos and neg > pos:
            negative =+ 1
    elif neu > neg and pos > neg:
             positive =+ 1  
    elif neu == 1.0:
            neutral =+ 1
    return [positive,negative,neutral]