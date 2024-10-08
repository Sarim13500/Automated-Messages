# main.py

# Importing from the morning_greetings package
from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message


def run_greeting():
    # Initialize contact manager
    cm = ContactsManager()

    # Retrieve contacts
    contacts = cm.get_contacts()

    if not contacts:
        print("No contacts found!")
        return

    # Loop through contacts and send messages
    for contact in contacts:
        name = contact['name']
        email = contact['email']
        message = generate_message(name)

        try:
            # Simulate sending the message
            send_message(email, message)

            # Log the message
            log_message(contact, message)

        except Exception as e:
            print(f"Failed to send message to {name}: {e}")


if __name__ == "__main__":
    run_greeting()
