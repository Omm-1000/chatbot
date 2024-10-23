import nltk
import random
import re
import string
#please download nltk and punkt package from idle  if you use
#and please check the internet connection so that smoothly run the program
nltk.download('punkt')
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! How can I assist you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "thank_you": ["You're welcome!", "No problem!", "Happy to help!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure how to respond to that."]
}

def preprocess_input(user_input):
    user_input = user_input.lower()
    user_input = re.sub(f'[{string.punctuation}]', '', user_input)  
    return user_input
def generate_response(user_input):
    user_input = preprocess_input(user_input)

    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(responses["goodbye"])
    elif "thank" in user_input:
        return random.choice(responses["thank_you"])
    else:
        return random.choice(responses["default"])


def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
