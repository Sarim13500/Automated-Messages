# message_sender.py
def send_message(email, message):
    if not email:
        raise ValueError("Email address is missing")
    # Simulate sending a message
    print(f"Sending message to {email}: {message}")
