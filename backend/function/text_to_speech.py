import requests
from decouple import config

# ElevenLabs
ELEVENLABS_API_KEY = config("ELEVENLABS_API_KEY")

# Convert text to speech
def convert_text_to_speech(message):
    
    body = {
    "text": message,
    "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
    }, 
    "model_id": "eleven_multilingual_v2",
    # "language_code": "ja",
    }
    
    # Define voice
    voice_Jessica = "cgSgspJ2msm6clMCkdW9"

    headers = { "xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"}

    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_Jessica}"

    # Send request to ElevenLabs
    try:        
        response = requests.post(endpoint, json=body, headers=headers)      
    except Exception as e:       
        return

    # handle the response
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to convert text to speech. Status code: {response.status_code}")
