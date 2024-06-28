"""
Contains functions to perform emotion analysis
"""
import requests
import json

def emotion_detector(text_to_analyze):
    """
    Performs emotion detection on the input text
    """
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    injson = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL, json=injson, headers=header)#, timeout=10)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        predicted_emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(predicted_emotions, key=predicted_emotions.get)
        predicted_emotions.update({"dominant_emotion": dominant_emotion})

    elif response.status_code == 400:
        predicted_emotions = {'anger': None, 
                              'disgust': None, 
                              'fear': None, 
                              'joy': None, 
                              'sadness': None, 
                              'dominant_emotion': None
        }
    
    return predicted_emotions
