import queue
import threading
import subprocess

from recognize_intent import get_intent
from response_generation import generate_response
from handle_commands import handle_command

input_queue = queue.Queue()


def add_input_to_queue(input_queue, user_input):
    """
    Simulate adding user inputs to the queue.
    
    Parameters:
    input_queue (queue.Queue): The queue to which inputs are added.
    """
    input_queue.put(user_input)


# Main chatbot function
def chat_with_bot(input_queue):
    print("Start chatting with the bot (type 'exit' to stop)!")
    chat_history_ids = None
    while True:
        try:
            user_input = input_queue.get()  # Get the next input from the queue
            if user_input.lower() == "exit":
                break

            intent = get_intent(user_input)
            if intent == "open_browser":
                handle_command(intent)
            else:
                bot_response, chat_history_ids = generate_response(user_input, chat_history_ids)
                print(f"Bot: {bot_response}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # input_queue = queue.Queue()

    # Start the chatbot in a separate thread
    chatbot_thread = threading.Thread(target=chat_with_bot, args=(input_queue,))
    chatbot_thread.start()

    print("Hi1")
    whisper_thread = threading.Thread(target=subprocess.Popen('''"whisper_mic", "--save_file", "--model", "small", "--english"''', shell=True, stdout=subprocess.PIPE))
    whisper_thread.start()
    print("hi2")

    # Add inputs to the queue from the main thread
    # add_input_to_queue(input_queue)

    # Wait for the chatbot thread to finish
    chatbot_thread.join()
    whisper_thread.join()
    print("hi3")
