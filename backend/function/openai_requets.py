from openai import OpenAI 
from decouple import config 
import json
client = OpenAI()

# Import custom function
from function.database import get_recent_message

# Retrieve environment variables
client.organization = config("OPEN_AI_ORG")
client.api_key = config("OPENAI_API_KEY")

# OpenAI - Whisper
# Convert audio to text
def convert_audio_to_text(audio_file):
    try:        
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="ja"            
        )
        message_text = response.text
        return message_text
    except Exception as e:
        print(e)
        return

# OpenAI - ChatGPT
# Send message to ChatGPT and get response

def openai_chat_response(message_input):
    messages = get_recent_message()
    user_message = {
        "role": "user",
        "content": message_input
    }
    messages.append(user_message)
    print(json.dumps(messages, indent=2, ensure_ascii=False))
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Sửa lỗi chính tả "gpt-4o" thành "gpt-4"
            messages=messages
        )
        
        message_text = response.choices[0].message.content
        return message_text
    except Exception as e:
        print(f"Lỗi khi gọi OpenAI API: {str(e)}")
        return None  # Trả về None thay vì không trả về gì cả
# Send message to ElevenLabs
