# =========================================
#         SMART PYTHON CHATBOT
# =========================================

# Dictionary containing chatbot replies
responses = {
    "hello": "Hello! 👋",
    "hi": "Hi there 😊",
    "how are you": "I'm doing great! 😄",
    "what is your name": "I am Smart Python Chatbot 🤖",
    "help": "Available commands: hello, hi, help, bye",
    "bye": "Goodbye! Have a nice day 👋"
}


def chatbot():
    """Simple rule-based chatbot"""

    print("=" * 50)
    print("          🤖 SMART CHATBOT 🤖")
    print("=" * 50)
    print("Type 'bye' to close the chatbot.\n")

    while True:

        # Take user input
        user_input = input("You : ").strip().lower()

        print("-" * 50)

        # Check response
        if user_input in responses:
            print("Bot :", responses[user_input])

            # Exit condition
            if user_input == "bye":
                print("=" * 50)
                break

        else:
            print("Bot : Sorry, I don't understand that command 😅")

        print("-" * 50)
        print()


# Start chatbot
if __name__ == "__main__":
    chatbot()
