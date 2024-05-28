import webbrowser


# Function to handle commands
def handle_command(intent):
    if intent == "open_browser":
        print("Bot: Opening your default browser...")
        webbrowser.open('http://www.google.com')  # You can customize the URL
    else:
        print("Bot: I'm not sure how to handle this command.")