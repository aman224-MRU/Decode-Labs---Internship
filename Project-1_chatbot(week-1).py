"""Simple rule-based chatbot.

This chatbot responds to a few predefined user inputs using if/else logic.
It runs in a continuous loop until the user types an exit command.
"""

print("Welcome to the rule-based chatbot!")
print("Type a greeting, ask how I am, or type 'exit' to quit.")

exit_commands = {"exit", "quit", "bye", "goodbye"}

greetings = {"hello", "hi", "hey", "good morning", "good afternoon", "good evening"}

while True:
    user_input = input("You: ").strip().lower()

    if user_input in exit_commands:
        print("Bot: Goodbye! Have a great day.")
        break

    if user_input in greetings:
        print("Bot: Hello! How can I help you today?")
    elif "how are you" in user_input or "how are you doing" in user_input:
        print("Bot: I'm a simple chatbot, but I'm here to help!")
    elif "your name" in user_input:
        print("Bot: My name is Chatbot. I respond to simple rules.")
    elif "help" in user_input:
        print("Bot: I can respond to greetings, tell you my name, answer simple questions, and say goodbye.")
    elif "thank" in user_input or "thanks" in user_input:
        print("Bot: You're welcome!")
    elif "what can you do" in user_input or "capability" in user_input or "what are you" in user_input:
        print("Bot: I can greet you, answer simple questions, and end the conversation when you say goodbye.")
    elif "joke" in user_input:
        print("Bot: Why did the computer show up at work late? It had a hard drive!")
    elif "weather" in user_input:
        print("Bot: I can't check the real weather, but I hope it is nice where you are.")
    elif "time" in user_input:
        from datetime import datetime
        print(f"Bot: The current time is {datetime.now().strftime('%H:%M')}.")
    elif "age" in user_input:
        print("Bot: I am a brand new chatbot created in Python, so I don't really have an age.")
    elif "favorite" in user_input and "color" in user_input:
        print("Bot: I like all colors, but if I had to choose, I'd say blue.")
    else:
        print("Bot: Sorry, I don't understand that yet. Try a greeting, ask 'how are you', or say 'help'.")

print("Chatbot session ended.")