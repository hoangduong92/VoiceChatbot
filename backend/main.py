# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import json 


# Custom function imports
from function.openai_requets import convert_audio_to_text, openai_chat_response
from function.database import store_message, reset_message
from function.text_to_speech import convert_text_to_speech

# Initiate App
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Health check
@app.get("/health")
async def check_health():
    return {"message": "healthy"}

# Reset message
@app.get("/reset")
async def reset_conversation():
    reset_message()
    return {"message": "Conversation reset"}

# Get audio
@app.get("/post-audio-get/")
async def get_audio():
    try:
        # Get saved audio
        audio_input = open("voice.mp3", "rb")
        
        # Decode audio
        message_decoded = convert_audio_to_text(audio_input)

        # Guard: Ensure message is decoded
        if not message_decoded:
            raise HTTPException(status_code=400, detail="Failed to decode audio")
        
        # Get response from ChatGPT
        chat_response = openai_chat_response(message_decoded)

        # Guard: Ensure response is generated
        if not chat_response:
            raise HTTPException(status_code=400, detail="Failed to generate response")

        # Store message
        store_message(message_decoded, chat_response)
        
        # Convert chat response to audio
        audio_output = convert_text_to_speech(chat_response)

        # Guard: Ensure audio is generated
        if not audio_output:
            raise HTTPException(status_code=400, detail="Failed to get ElevenLabs audio response")


        # Tạo một generator để trả về dữ liệu theo từng phần
        def iterfile():
            yield audio_output

        # Trả về audio file
        return StreamingResponse(iterfile(), media_type="audio/mpeg")

        # Thêm logging
        print(f"Audio decoded: {message_decoded}")
        print(f"Chat response: {chat_response}")
        print(f"Audio output generated: {bool(audio_output)}")
        
    except Exception as e:
        print(f"Lỗi trong get_audio: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

    # Xóa dòng return "DONE" vì nó không cần thiết và có thể gây ra lỗi


# Post bot response
# Note : Not playing in browser when using post request
    
