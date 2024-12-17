import sys
import threading
import time
import webbrowser
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
from head.mouth import speak
from Training_Model.model import mind


def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict


def save_qa_data(file_path, qa_dict):
    with open(file_path, "w", encoding="utf-8", errors="replace") as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")


qa_file_path = r"C:\Users\mohit\OneDrive\Desktop\xolo2.0\Data\brain_data\qna_logbook.txt"
qa_dict = load_qa_data(qa_file_path)


def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)
    print()


def wiki_search(prompt):
    search_prompt = prompt.replace("Wikipedia", "").strip()

    try:
        # Search Wikipedia for a summary
        wiki_summary = wikipedia.summary(search_prompt, sentences=1)

        # Create threads for animated message and speech output
        animate_thread = threading.Thread(target=print_animated_message, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        # Start and join both threads
        animate_thread.start()
        speak_thread.start()
        animate_thread.join()
        speak_thread.join()

        # Save the result to the Q&A logbook
        qa_dict[search_prompt] = wiki_summary
        save_qa_data(qa_file_path, qa_dict)

    except DisambiguationError as e:
        speak("The query is ambiguous. Please provide more data.")
        print(f"Ambiguous query. Options are: {e.options}")
    except PageError:
        # If Wikipedia page not found, search Google instead
        google_search(search_prompt)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {str(e)}")


def google_search(query):
    query = query.replace("Who is ", "").strip()

    if query:
        # Open Brave browser with the search query
        url = "https://www.google.com/search?q=" + query
        webbrowser.get("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s").open_new_tab(url)
        speak(f"Showing search results for {query} in Google.")
        print(f"Showing search results for {query} in Google.")
    else:
        speak("Sorry! I did not understand what you said.")
        print("Sorry! I did not understand what you said.")


def brain(text):
    try:
        # Attempt to get an answer from the local Q&A database
        response = mind(text)

        if not response:
            # If no response from local database, search Wikipedia
            wiki_search(text)
            return

        # Create threads for animated message and speech output
        animate_thread = threading.Thread(target=print_animated_message, args=(response,))
        speak_thread = threading.Thread(target=speak, args=(response,))

        # Start and join both threads
        animate_thread.start()
        speak_thread.start()
        animate_thread.join()
        speak_thread.join()

        # Save the valid response to the Q&A logbook
        qa_dict[text] = response
        save_qa_data(qa_file_path, qa_dict)

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred in brain: {str(e)}")
        wiki_search(text)  # Fallback to Wikipedia search
