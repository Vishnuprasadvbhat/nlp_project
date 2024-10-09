"""
Here we perform extractive summarization on the sentiment data returned form sentiment_analysis.py

We split the data on basis of label and perform extractive summarization on both negative and positive data
"""

from src.components.sentiment_analysis import Sentiment_Analysis
from heapq import nlargest
from utils import save_to_file


class Extractive_Sum():


    def extractor(self):

        # Initialize the Sentiment Analysis class
        sentiment_analy = Sentiment_Analysis()

        # Process the data and obtain sentiment scores
        sentiment_result = sentiment_analy.data_preprocess()
        sent_score = sentiment_result[0]  # Overall sentiment score
        pos_score = sentiment_result[1]  # Positive sentiment score
        neg_score = sentiment_result[2]  # Negative sentiment score

        # Calculate the number of sentences with a sentiment score greater than 0.3
        num_sentences = len([value for value in sent_score.values() if value > 0.3])

        # Get the number of positive and negative sentences
        num_pos_sentences = len(pos_score)
        num_neg_sentences = len(neg_score)

        # Extract the top positive and negative sentences based on sentiment score
        pos_n = nlargest(num_pos_sentences, pos_score, key=pos_score.get)
        neg_n = nlargest(num_neg_sentences, neg_score, key=neg_score.get)

        # Combine the top positive and negative sentences
        pos_sentences = ''.join(pos_n)
        neg_sentences = ''.join(neg_n)
        extractive_sentences = pos_sentences + neg_sentences

        # Uncomment if you want to print the number of positive/negative sentences
        # print(num_sentences)
        # print(num_pos_sentences)
        # print(num_neg_sentences)

        # Output the combined sentences
        # print(extractive_sentences)

        # Save the combined sentences to a file
        saved_location =save_to_file(extractive_sentences,'C:\\Users\\vishn\\summarizer\\extracted_data' )
    
        return saved_location



if __name__ == '__main__':
    obj = Extractive_Sum()

    output =obj.extractor()
    print(output)