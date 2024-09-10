from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys, os

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')
stop_words = stopwords.words('english')