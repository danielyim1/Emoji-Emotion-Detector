import os
import requests
import json

# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
KEY = os.environ['FACE_SUBSCRIPTION_KEY']

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://emojidetector.cognitiveservices.azure.com/face/v1.0/detect'
def getEmotion(image_url):

    headers = {'Ocp-Apim-Subscription-Key': KEY}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion',
    }

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image_url})
    print(json.dumps(response.json()))



