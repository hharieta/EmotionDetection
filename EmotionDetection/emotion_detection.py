import os
import operator
from typing import Dict
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features
from ibm_watson.natural_language_understanding_v1 import SentimentOptions, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def emotion_detector(text: str) -> Dict:
    
    apikey = os.getenv("NLU_APIKEY")
    url = os.getenv("NLU_URL")

    authenticator = IAMAuthenticator(apikey)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(url)
    
    try:
        response = natural_language_understanding.analyze(
            features=Features(
                sentiment=SentimentOptions(document=True),
                emotion=EmotionOptions(document=True)
                ),
            text=text,
            return_analyzed_text=True
        )
    except Exception:
        return {"dominant_emotion": None}

    formatted_response = response.get_result()
        
    if response.status_code == 200:
        emotions = formatted_response['emotion']['document']['emotion']
        emotions.update({"dominant_emotion": max(
            formatted_response['emotion']['document']['emotion'].items(), 
            key=operator.itemgetter(1))[0]})
    elif response.status_code == 400:
        emotions = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None}


    return emotions
