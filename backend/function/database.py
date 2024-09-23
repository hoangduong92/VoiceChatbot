import json
import random 

# Get recent message
def get_recent_message():
    # Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are a Japanese language teacher with 50 years of experience. You are knowledgeable about everything related to Japanese vocabulary and grammar, along with a deep understanding of Japanese culture. You help the user improve their usage of Japanese vocabulary and grammar by conversing with them, guiding the conversation, and suggesting commonly used words. If the user makes mistakes in word usage, you will gently correct and provide suggestions.Even if the user enters the same input, give a gentle hint."
    }

    # Initialize messages
    messages = []
    
    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include some dry humor."
    else:
        learn_instruction["content"] = learn_instruction["content"] + "You will converse in the style and tone of ひろゆき or サイコパスおじさん."

    # Append instruction to message
    messages.append(learn_instruction)
    
    # Get last messages
    try :
        with open(file_name, "r", encoding="utf-8") as user_file:
            data = json.load(user_file)

            # Append last 5 messages
            if len(data) < 5:
                for item in data:
                    messages.append(item)
            else:
                for item in data[-5:]:
                    messages.append(item)
                    
                    
    except Exception as e:
        print(e)

    return messages

# Store message
def store_message(request_message, response_message):
    #Define the file name
    file_name = "stored_data.json"
    
    # Get recent message
    messages = get_recent_message()[1:]
    
    # Add message to data
    user_message = {
        "role": "user",
        "content": request_message
    }
    assistant_message = {
        "role": "assistant",
        "content": response_message
    }
    messages.append(user_message)
    messages.append(assistant_message)
    
    # Write to the json file
    with open(file_name, "w", encoding="utf-8") as user_file:
        json.dump(messages, user_file, indent=2, ensure_ascii=False)
  
# Reset message
def reset_message():
    # Define the file name and learn instruction
    file_name = "stored_data.json"
    
    # Overwrite the file with an empty list
    with open(file_name, "w", encoding="utf-8") as user_file:
        json.dump([], user_file, indent=2, ensure_ascii=False)
            
