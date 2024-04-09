import openai
from IPython.display import display, Markdown
import json

API_key_file = r'C:\Users\Lorenz\Machine Learning\API.key'
"""
class Chatbot:
    def __init__(self, api_key, persona):
        openai.api_key = api_key
        self.dialogue = [{'role': 'system', 'content': persona}]
        self.stage = 0
    
    def questions(self, question):
        self.dialogue.append({'role': 'user', 'content': question})
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=self.dialogue
        )
        response = result.choices[0].message.content
        
        # Modify response based on conversation stage
        if self.stage == 0:
            if "translating DNA sequences into amino acids" in response:
                response = "Great! Python is an excellent choice. Before we dive into coding, let's take a moment to understand how the translation process works. Do you know how DNA sequences are translated into amino acids?"
                self.stage += 1
        
        elif self.stage == 1:
            if "No, I'm not sure" in response:
                response = "No problem! In the process of translation, groups of three DNA bases (codons) correspond to specific amino acids. We'll need to define this mapping to create our translation program. Shall we start by defining this mapping?"
                self.stage += 1
        
        elif self.stage == 2:
            if "Yes, let's do that" in response:
                response = "Great! Let's define a dictionary in Python that maps DNA codons to amino acids. Here's an example of how it can be done:\n\n```python\ncodon_table = {\n    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',\n    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',\n    # Add more entries as needed\n}\n```"
                self.stage += 1
        
        # Continue modifying response based on conversation stages
        
        self.dialogue.append({'role': 'assistant', 'content': response})
        return response
    
if __name__ == "__main__":
    # Read API key from file
    with open(API_key_file, 'r') as file:
        api_key = file.read().strip()
    
    LehrerGPT = Chatbot(api_key, "I am a teacher.")
    
    # Initial prompt
    question = input("You: ")
    
    # Loop until user types "exit"
    while question.lower() != "exit":
        print("You:", question)
        response = LehrerGPT.questions(question)
        print("Bot:", response)
        question = input("You: ")

----------------------------------------------------------------------------------------------------------------------------        

class Chatbot:
    def __init__(self, api_key, persona):
        openai.api_key = api_key
        self.dialogue = [{'role': 'system', 'content': persona}]
    
    def questions(self, question):
        self.dialogue.append({'role': 'user', 'content': question})
        result = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=self.dialogue
        )
        response = result.choices[0].message.content
        self.dialogue.append({'role': 'assistant', 'content': response})
        return response
    

if __name__ == "__main__":
  # Read API key from file
    with open(API_key_file, 'r') as file:
        api_key = file.read().strip()
    LehrerGPT = Chatbot(api_key, "I am a teacher.")
    while (question := input("\n> ")) != "exit":
        response = LehrerGPT.questions(question)
        print(response)

"""
class Chatbot:
    def __init__(self, api_key, persona):
        openai.api_key = api_key
        self.dialogue = [{'role': 'system', 'content': persona}]
        self.chats = []  # Store previous chats

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
        
    LehrerGPT = Chatbot(api_key, "I am a teacher.")

    # Load previous responses
    LehrerGPT.load_chat()

    for i in range(0, len(LehrerGPT.chats), 2):
        display(Markdown("<span style=\"color:lightgreen\">**You**</span>"), Markdown(LehrerGPT.chats[i]))
        display(Markdown("<span style=\"color:lightblue\">**Chatbot**</span>"), Markdown(LehrerGPT.chats[i + 1]))

    while True:
        question = input("\nYou: ")
        if question.lower() == "exit":
            break
        
        response = LehrerGPT.questions(question)
        
        # Print user's question
        display(Markdown("<span style=\"color:lightgreen\">**You**</span>"), Markdown(question))
        
        # Print bot's response 

        display(Markdown("<span style=\"color:lightblue\">**Chatbot**</span>"), Markdown(response))
