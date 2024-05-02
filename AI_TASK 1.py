def chatbot():
    print("Welcome to SimpleChatBot! How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input:
            print("SimpleChatBot: Hello there!")
        elif "how are you" in user_input:
            print("SimpleChatBot: I'm just a bot, so I'm always doing well. How can I help you?")
        elif "bye" in user_input:
            print("SimpleChatBot: Goodbye! Have a great day!")
            break
        else:
            print("SimpleChatBot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
