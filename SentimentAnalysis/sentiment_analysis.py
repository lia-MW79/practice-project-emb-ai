'''Sentiment analysis tool'''
import json
import requests

# Needs to import Watson Embedded AI Libraries to use outside lab environment

# Function for running sentiment analysis using the Watson NLP BERT Seniment Analysis function
def sentiment_analyzer(text_to_analyse):
    '''Sentiment analysis function'''

    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    # Custom header specifying the model ID for the sentiment analysis service
    headers = {"grpc-metadata-mm-model-id" : "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Constructing the request payload in the expected format
    myobj = { "raw_document" : { "text" : text_to_analyse } }

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=headers, timeout=20)

    if response.status_code==500:
        return {'label' : None, 'score' : None}
    # Formatting the response to return a dictionary containing sentiment analysis results
    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label' : label, 'score' : score}
