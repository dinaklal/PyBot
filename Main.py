
from scripts.greeting import check_for_greeting
from scripts.chats import chats

# greetings
sentence = input(" ")
print(check_for_greeting(sentence))

# chitchat
while sentence != "exit":
    sentence = input("User : ")
    reply = chats(sentence)
    if reply is None:
        reply = "I am not undertanding your language"
    print(reply)
    9