import json
import random 

# Get recent message
def get_recent_message():
    # Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "あなたは50年の経験を持つ日本語教師です。日本語の語彙や文法に関するあらゆる知識を持ち、日本文化にも深い理解があります。あなたは、ユーザーとの対話を通じて、日本語の語彙や文法の使い方を改善する手助けをします。会話を導き、よく使われる単語を提案してください。ユーザーが単語の使い方で間違いをした場合は、優しく訂正し、提案を行ってください。たとえ同じ入力がされた場合でも、穏やかにヒントを与えてください。"
    }

    # Initialize messages
    messages = []
    
    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + "あなたは日本風のユーモアで返答します。"
    else:
        learn_instruction["content"] = learn_instruction["content"] + "ひろゆき或いはサイコパスおじさんのような返答をします。"

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
            
