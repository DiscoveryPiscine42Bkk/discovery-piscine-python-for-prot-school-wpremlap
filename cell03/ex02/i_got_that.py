while True:
    # Accept user input
    user_input = input("Say something (or type 'STOP' to quit): ")

    # If the user enters "STOP", exit the loop
    if user_input == "STOP":
        break

    # Otherwise, respond to the user
    print(f"I got that: {user_input}")