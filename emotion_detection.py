import json
import requests 

def emotion_detector(text_to_analyze):
    # URL for emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Constracting the request layload in the expected format
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a post request for the emotion analysis APO
    response = requests.post(url, json = input_json, headers = header)
    
    #Parsing the JSON reaponse from the API
    formatted_response = json.loads(response.text)

    # extracting emotion label and score 
    anger_score = formatted_response['emotionPredictions']['emotion']['anger']

    # Return dictionary containing emotion analysis result
    return {
            'anger': anger_score,
           # 'disgust': disgust_score,
            #'fear': fear_score,
            #'joy': joy_score,
            #'sadness': sadness_score,
            #'dominant_emotion': '<name of the dominant emotion>'
            }
