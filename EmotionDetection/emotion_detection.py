import json
import requests 

def emotion_detector(text_to_analyze):
    # URL for emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Constracting the request layload in the expected format
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a post request for the emotion analysis API
    response = requests.post(url, json = input_json, headers = header)
    
    #Parsing the JSON reaponse from the API
    formatted_response = json.loads(response.text)

    # extracting emotion label and score 
    emotion_score = formatted_response['emotionPredictions'][0]['emotion']

    #finding out the dominant emotion
    dominant_emotion = max(emotion_score, key = emotion_score.get)    

    # Return dictionary containing emotion analysis result
    return {
            'anger': emotion_score['anger'],
            'disgust': emotion_score['disgust'],
            'fear': emotion_score['fear'],
            'joy': emotion_score['joy'],
            'sadness': emotion_score['sadness'],
            'dominant_emotion': dominant_emotion
           }
