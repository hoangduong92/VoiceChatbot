from openai import OpenAI
from decouple import config
client = OpenAI()
# OpenAI API key
client.api_key = config("OPENAI_API_KEY")

# Convert text to speech
def convert_text_to_speech(message):
    try:
        response = client.audio.speech.create(
            model="tts-1",
            input=message,
            voice="echo",
            response_format="wav"
        )
        # Kiểm tra cấu trúc của response và truy cập dữ liệu phù hợp
        audio_content = response.content
        return audio_content
    except Exception as e:
        raise Exception(f"Failed to convert text to speech. Error: {str(e)}")

      