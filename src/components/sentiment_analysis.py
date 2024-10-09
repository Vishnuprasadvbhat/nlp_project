"""     Here we get the data from the flaks post request and perform initial preprocessing

        also we split the text into positive and negative and label the dataset
        This file returns a dataframe with data resulting in sentiment analysis
"""
# from imports import *
from src.imports import *
from utils import save_dataframe
from reviews import texts
class Sentiment_Analysis:

    def __init__(self):
        # save_file = savefile()
        pass

    def data_preprocess(self):
        try:
          
            punc = '''!()-[]{};:,'"\<>/?@#$%^&*_~'''

            data = texts

            texts = texts.lower()

            texts = [text for text in texts if text not in punc]
            texts = ''.join(texts)

            word_token = word_tokenize(texts)

            word_token = [word for word in word_token if
                          word not in stop_words and word not in punctuation and word != '...']

            word_freq = {}
            for word in word_token:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

            max_freq = max(word_freq.values())

            prop_word = {}
            for key, values in word_freq.items():
                prop_word[key] = round(values / max_freq, 3)

            vader = SentimentIntensityAnalyzer()

            # sentiments = [vader.polarity_scores(word)['compound'] for word in word_token]

            # positive_sentiments = [sentiment for sentiment in sentiments if sentiment >= 0.5]

            positive_words = {}
            for word in word_token:
                senti = vader.polarity_scores(word)['compound']
                if senti >= 0.3:
                    positive_words[word] = senti

            negative_words = {}
            for word in word_token:
                senti = vader.polarity_scores(word)['compound']
                if senti < 0.3 and senti > -0.5 and not senti == 0:
                    negative_words[word] = senti

            sent_token = sent_tokenize(texts)

            sent_token = [sent.lower() for sent in sent_token]

            positive_sent = {}
            for sent in sent_token:
                for word in sent.split():
                    if word.lower() in positive_words.keys():
                        if sent not in positive_sent.keys():
                            positive_sent[sent] = positive_words[word.lower()]
                        else:
                            positive_sent[sent] += positive_words[word.lower()]

            pos_data = pd.DataFrame(positive_sent.items(), columns=['sentence', 'score'])

            negative_sent = {}
            for sent in sent_token:
                for word in sent.split():
                    if word.lower() in negative_words.keys():
                        if sent not in negative_sent.keys():
                            negative_sent[sent] = negative_words[word.lower()]
                        else:
                            negative_sent[sent] += negative_words[word.lower()]

            neg_data = pd.DataFrame(negative_sent.items(), columns=['sentence', 'score'])

            sent_score = {k: v for d in (positive_sent, negative_sent) for k, v in d.items()}
            sent_score = dict(sorted(sent_score.items(), key=lambda x: x[1], reverse=True))

            # sentiment_data = pd.concat([pos_data, neg_data], ignore_index=True)

            sentiment_data = pd.DataFrame(list(sent_score.items()), columns=['sentence', 'score'])

            sentiment_data['label'] = sentiment_data['score'].apply(lambda x: 1 if x > 0.3 else 0)
            # sentiment_data.drop(columns=['score'], inplace=True)

            folder_path = 'C:\\Users\\vishn\\summarizer\\sentiment_data'

            save_dataframe(sentiment_data, folder_path=folder_path, filename='sentiment.csv')
            save_dataframe(pos_data, folder_path=folder_path, filename='pos_sentiment.csv')
            save_dataframe(neg_data, folder_path=folder_path, filename='neg_sentiment.csv')

            analysis = [sent_score, positive_sent, negative_sent]

            return analysis

        except Exception as e:
            print(e)


if __name__ == '__main__':
    object = Sentiment_Analysis()

    main = object.data_preprocess()

    print(main[0])
    # print(main)
