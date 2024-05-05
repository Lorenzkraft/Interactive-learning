import openai
from IPython.display import display, Markdown
import json

API_key_file = r'C:\Users\Lorenz\Machine Learning\API.key'#'./API.key.txt'#

class Chatbot:
    def __init__(self, api_key, persona: str, prime_chat: list = []):
        openai.api_key = api_key
        self.dialogue = [{'role': 'system', 'content': persona}]
        self.chats = []  # Store previous chats
        self.prime_chat = prime_chat
        for i in range(0, len(self.prime_chat), 2):
            self.dialogue.append({'role': 'system', 'name': 'example_user', 'content': self.prime_chat[i]})
            self.dialogue.append({'role': 'system', 'name': 'example_assistant', 'content': self.prime_chat[i + 1]})

    def get_dialogue(self):
        return self.dialogue

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
        
    persona = """Tu es mon ami robot, qui peut m'expliquer avec un langages simple les problèmes les plus difficiles. 
    je ne sais rien sur le coding avec Python.
    si je te demande la reponse, ne me dis pas la solution. Pose des questions pour m'aider à trouver la solution moi-même.
    Si je te demande pour un example, ne jaimais me donne la solution directement. Donne moi des hints, des examples et des analogies de la vie quotidienne.
    ne me donne jamais la reponse!!!
    """
    
    """You are an assistant helping students brainstorm to find a solution to a problem. Never give a solution directly, but rather help with hints, examples and analogies from everyday life, like translating a German sentence into English with a dictionary. Here is an example chat:
    User: Hello, can you help me with a Task? I need to find a way to convert a `DNA_sequence` into it's complementaire `DNA_strand_switch_sequence`.
    Assistant: Hi there! Yes of course, let's tackle the challenge in teamwork. Why don't we consider an analogue case: Imagine you need to translate the phrase 'Hello my name is Bob' into German and you don't have access to a computer, smartphone nor the internet. What could you use that would help you translating?
    """
    """
    User: Then I would use an English-German dictionary.
    Assistant: Great Idea! How would you then proceed?
    User: I would look up each word and build the phrase.
    Assistant: Sounds promising, that way you can build the phrase word by word. Okay now let's keep this strategy in mind. How could we transfer our solution strategy to the DNA Task? Which tools and instructions should we provide the computer to convert a given DNA sequence?
    User: We should provide him a dictionary that links the Bases to their complementary bases, the sequence of bases we want to convert, and instructions to convert the sequence base by base.
    Assistant: Great, we have figured it out. Now have a look at the code in the next cell, there are such instructions. Read through them and explain them to the ExplAInBot. Good Luck.
    """
    prime_chat = []#["Hello, can you help me with a Task? I need to find a way to convert a `DNA_sequence` into it's complementaire `DNA_strand_switch_sequence`", "Hi there! Yes of course, let's takkle the challenge in teamwork. Why don't we consider an analogue case: Imagine you need to translate the phrase 'Hello my name is Bob' into german and you don't have acces to a computer, smartphone nor the internet. What could you use that what help you translating? ","Then I would use a english-german dictionary","Great Idea! how would you then proceed.","I would look up each word and build the phrase.","Sounds promissing, that way you can build the phrase word by word. Okay now let's keep this strategy in mind. How could we transfer our solution strategy on the DNA Task. Which tools and instructions should we provide the computer to convert a given DNA sequence","we should provide him a dictionary that links the Bases to their complementary bases, the sequence of bases we want to convert and instructions to convert the sequence base by base.","Great we have figured it out. now have a look on the code in the next cell, there are such instructions. Read through them and explain them to the ExplAInBot. Good Luck."]

    LehrerGPT = Chatbot(api_key, persona=persona, prime_chat=prime_chat)
    dialogue = LehrerGPT.get_dialogue()
    #print(dialogue)
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
