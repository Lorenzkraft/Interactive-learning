import openai
from IPython.display import display, Markdown
import json

API_key_file = r'C:\Users\Lorenz\Machine Learning\API.key'

class Chatbot:
    def __init__(self, api_key, persona: str, prime_chat: list = []):
        openai.api_key = api_key
        self.dialogue = [{'role': 'system', 'content': persona}]
        self.chats = []  # Store previous chats
        self.prime_chat = prime_chat

    def prime_chat(self):
        for i in range(0, len(self.prime_chat), 2):
            self.dialogue.append({'role': 'system', 'name': 'example_user', 'content': self.prime_chat[i]})
            self.dialogue.append({'role': 'system', 'name': 'example_assistant', 'content': self.prime_chat[i + 1]})

    def questions(self, question):
        self.dialogue.append({'role': 'user', 'content': question})
        result = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=self.dialogue
        )
        response = result.choices[0].message.content
        self.dialogue.append({'role': 'assistant', 'content': response})

        # Store the response in the list of previous responses
        self.chats.append(question)
        self.chats.append(response)

        # Save responses to a file
        self.save_chat()
        
        return response
    
    def save_chat(self):
        with open("chats.json", "w") as file:
            json.dump(self.chats, file)
    
    def load_chat(self):
        try:
            with open("chats.json", "r") as file:
                self.chats = json.load(file)
        except FileNotFoundError:
            # If file doesn't exist, initialize responses as an empty list
            self.chats = []
    
if __name__ == "__main__":
    # Read API key from file
    with open(API_key_file, 'r') as file:
        api_key = file.read().strip()
        
    LehrerGPT = Chatbot(api_key, persona="I am a teacher.", prime_chat=["Hello", "Hi there! How can I help you today?"])

    # Load previous responses
    LehrerGPT.load_chat()

    for i in range(0, len(LehrerGPT.chats), 2):
        display(Markdown("<span style=\"color:lightgreen\">**You**</span>"), Markdown(LehrerGPT.chats[i]))
        display(Markdown("<span style=\"color:lightblue\">**Chatbot**</span>"), Markdown(LehrerGPT.chats[i + 1]))

    while True:
        question = input("\nWhat is your question: ")
        if question.lower() == "exit":
            break
        
        response = LehrerGPT.questions(question)
        
        # Print user's question
        display(Markdown("<span style=\"color:lightgreen\">**You**</span>"), Markdown(question))
        
        # Print bot's response 

        display(Markdown("<span style=\"color:lightblue\">**Chatbot**</span>"), Markdown(response))
