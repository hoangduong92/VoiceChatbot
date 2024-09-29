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
# quy định cổng cho frontend
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
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    # Get saved audio
    # audio_input = open("voice.mp3", "rb")

    # Save file from frontend        
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")
    
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
        raise HTTPException(status_code=400, detail="Failed to get OpenAI audio response")

    # Tạo một generator để trả về dữ liệu theo từng phần
    def iterfile():
        yield audio_output

    # Trả về audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")




# Post bot response
# Note : Not playing in browser when using post request
    
