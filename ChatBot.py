import re

def chatbot(user_input):
    responses = {
        r"(hello|hi|hey|greetings|Good morning|evening|afternoon|night)": "Hello! How can I assist you today?",
        r"(how are you|how's it going|hru|how are u|how r u)": "I'm fine, What about you?",
        r"(i am fine|fine|good|well|perfect)": "Glad to hear this, How can I assist you?",
        r"(what is your name|who are you)": "I'm a simple chatbot.",
        r"(bye|goodbye|see you later|nice to meet you|thank you)": "Goodbye! Have a great day!",
        r"(what do you like to do most of the time)": "Helping people",
        r"(I want to speak to a human|live agent|customer service)": "Let me know your requirements so the agent can solve it for you then",
        r"(How old are you|What's your age)": "I don't have an age because I am a robot"
    }
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand what you mean."

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day!")
        break
    response = chatbot(user_input)
    print("Bot:", response)
