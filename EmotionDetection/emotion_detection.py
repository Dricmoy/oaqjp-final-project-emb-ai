import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document":{"text":text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    
    formatted = (json.loads(response.text)).get('emotionPredictions',[])[0]
    
    emotions = (formatted.get('emotion'))
    anger = emotions.get('anger')
    disgust = emotions.get('disgust')
    fear = emotions.get('fear')
    joy = emotions.get('joy')
    sadness = emotions.get('sadness')
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }