import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hi there! How can I help?']),
    (r'what is your name?', ['I am a chatbot created by OpenAI.']),
    (r'how are you?', ['I am just a bot, but I am doing fine. How are you?']),
    (r'(.*) your name (.*)', ['I am a chatbot without a name.']),
    (r'bye|exit|quit', ['Goodbye! Have a great day!']),
    (r'(.*)', ['I’m sorry, I didn’t understand that. Can you please rephrase?']),
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the conversation
def start_chat():
    print("Chatbot: Hi, I'm your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Start the chatbot
if __name__ == "__main__":
    start_chat()
