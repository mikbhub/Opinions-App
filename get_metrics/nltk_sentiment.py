from nltk.sentiment import vader


def analyze_sentiment_using_vader(text):
    sentiment_analyzer = vader.SentimentIntensityAnalyzer()
    # sentence = "VADER is smart, handsome, and funny!"
    polarity_scores = sentiment_analyzer.polarity_scores(text)
    return polarity_scores['compound']

    #  for k in sorted(ss):
    #      print('{0}: {1}, '.format(k, ss[k]), end='')
    #  print()