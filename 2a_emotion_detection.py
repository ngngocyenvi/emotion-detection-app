import requests

def emotion_detector(text_to_analyse):
    """
    This function sends input text to the Watson NLP emotion detection API
    and returns the detected emotions.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    # Convert response to JSON format
    result = response.json()

    # Extract emotions
    emotions = result['emotionPredictions'][0]['emotion']

    return emotions
