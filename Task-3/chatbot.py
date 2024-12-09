from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize
import nltk
import random

nltk.download('punkt')

greetings = ["hello", "hi", "hey", "greetings"]
good_byes = ["bye", "seeyou", "see you", "goodbye"]
introductions = ["what is your name", "who are you", "name please"]
name_responses = ["my name is chatbot", "i am chatbot", "chatbot is my name"]

def check_greeting(user_input):
    for greeting in greetings:
        if fuzz.ratio(user_input.lower(), greeting) > 80:
            return random.choice(["hello", "hey", "hi"])

def check_goodbye(user_input):
    for goodbye in good_byes:
        if fuzz.ratio(user_input.lower(), goodbye) > 80:
            return random.choice(["bye", "good bye", "see you"])

def check_introduction(user_input):
    for introduction in introductions:
        if fuzz.ratio(user_input.lower(), introduction) > 80:
            return random.choice(name_responses)

def get_name(user_input):
    words = word_tokenize(user_input)
    for word in words:
        if word.lower() not in greetings and word.lower() not in good_byes and word.lower() not in introductions:
            return word

def chatbot():
    user_name = None
    while True:
        user_input = input("User: ")
        if user_name is None:
            if check_greeting(user_input):
                print("Chatbot: ", check_greeting(user_input))
            elif check_introduction(user_input):
                print("Chatbot: ", check_introduction(user_input))
                user_name = get_name(user_input)
            else:
                print("Chatbot: Please greet me or introduce yourself.")
        else:
            if check_goodbye(user_input):
                print("Chatbot: ", check_goodbye(user_input))
                break
            else:
                print("Chatbot: Hello ", user_name, ". How can I assist you today?")


if __name__=="__main__":
    chatbot()