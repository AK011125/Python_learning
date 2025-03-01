def chatbot_response(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot. You can call me ChatBot!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you rephrase or ask something else?"

# Main loop to interact with the chatbot
print("ChatBot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("ChatBot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print(f"ChatBot: {response}")