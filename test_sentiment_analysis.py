from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):

        positive_analysis = sentiment_analyzer("I love working with Python")
        self.assertEqual(positive_analysis['label'], 'SENT_POSITIVE')

        negative_analysis = sentiment_analyzer("I hate working with Pyhton")
        self.assertEqual(negative_analysis['label'], 'SENT_NEGATIVE')

        neutral_analysis = sentiment_analyzer("I am neutral about Python")
        self.assertEqual(neutral_analysis['label'], 'SENT_NEUTRAL')

unittest.main()