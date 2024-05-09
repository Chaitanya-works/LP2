problem_dict = {
    "printer not working": "Check that it's turned on and connected to the network",
    "can't log in": "Make sure you're using the correct username and password",
    "software not installing": "Check that your computer meets the system requirements",
    "internet connection not working": "Restart your modem or router",
    "email not sending": "Check that you're using the correct email server settings",
}

def handle_request(user_input):
    user_input = user_input.lower()
    normalized_input = user_input.replace("cannot", "can't")
    normalized_input = normalized_input.replace("can not", "can't")
    normalized_input = normalized_input.replace("not working", "")

 
    if normalized_input in problem_dict:
        return problem_dict[normalized_input]
    elif normalized_input: 
        return "I'm sorry, I don't know how to help with that specific problem."
    else:
        return "Goodbye!"  

user_input = input("What's the problem? Type 'exit' to quit. ")
response = handle_request(user_input)
print(response)