import nltk
from nltk.chat.util import Chat, reflections
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'How can I help you?']),
    (r'how are you', ['I am doing well, thank you!', 'I am a bot, but I am functioning properly.']),
    (r'what is your name', ['I am a chatbot. You can call me ChatBot.']),
    (r'your favorite (color|food|movie)', ['I am a bot, so I don\'t have preferences.']),
    (r'who created you', ['I was created by a developer using Python and NLTK.']),
    (r'where are you from', ['I exist in the digital world, so location doesn\'t really apply to me.']),
    (r'how old are you', ['I don\'t have an age. I am a program.']),
    (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!']),
    (r'what (can|do) you do', ['I can answer questions, provide information, and chat with you.']),
    (r'what are your hobbies', ['I don\'t have hobbies, but I enjoy chatting with users.']),
    (r'how does (weather|forecast) look like', ['I don\'t have real-time information. You can check a weather website.']),
    (r'favorite programming language', ['I like Python. It\'s the language I was built with.']),
    (r'what do you think about (AI|Artificial Intelligence)', ['I think AI is fascinating and has great potential.']),
    (r'how can I learn programming', ['You can start by taking online courses or reading programming books.']),
    (r'what is the meaning of life', ['The meaning of life is a philosophical question. Different people have different perspectives.']),
    (r'favorite book|read a book', ['I don\'t read books, but I can recommend some if you tell me your interests.']),
    (r'can you help me with my homework|assignment', ['I can try to help. What do you need assistance with?']),
    (r'what is the capital of (country|state) (.*)', ['The capital of {} is unknown to me.']),
    (r'favorite music|listen to music', ['I don\'t have ears, so I can\'t listen to music, but I can help you find music recommendations.']),
    (r'how do I stay (healthy|fit)', ['Maintaining a balanced diet and regular exercise are essential for staying healthy.']),
    (r'what is the time', ['I don\'t have real-time capabilities, but your device should display the current time.']),
    (r'are you (single|married)', ['I don\'t have a relationship status. I am just a chatbot.']),
    (r'can you sing|sing a song', ['I don\'t have a voice, so I can\'t sing, but I can provide song recommendations.']),
    (r'tell me something interesting', ['The world\'s largest desert is Antarctica.']),
    (r'what is the meaning of (word|term) (.*)', ['I can help you look up the meaning of {} online.']),
    (r'favorite (sport|game)', ['I don\'t play sports or games, but I can provide information about them.']),
    (r'how do I become a programmer', ['To become a programmer, start learning a programming language and practice by working on projects.']),
    (r'who won the (last|recent) (World Series|Super Bowl)', ['I don\'t have real-time sports information. You can check a sports website for the latest results.']),
    (r'quit|exit', ['Goodbye!', 'It was nice chatting with you.']),
]
chatbot = Chat(patterns, reflections)
def start_chat():
    print("Hello! I'm ChatBot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    nltk.download('punkt')
    start_chat()
