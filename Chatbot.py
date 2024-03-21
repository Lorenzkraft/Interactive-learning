import openai
API_key_file = r'C:\Users\Lorenz\Machine Learning\API.key'


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

