# Simple Chat Room

A simple chat room implementation using Python's `http.server` module and basic HTML/JavaScript for the client-side interaction.

## Introduction

This project creates a basic chat room where users can send and receive messages in real-time using a web browser.

## How to Use

1. Clone or download the repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Run the script:
This will start the chat server on port 8000 by default.

4. Open a web browser and go to `http://localhost:8000`. This will load the chat room interface.

5. Type your message in the input field and click the "Send" button. Your message will be displayed in the chat area along with your chosen username.

6. Other users can also send messages, and the chat history will be updated in real-time.

## Features

- Users are assigned unique usernames in the format `CommonNameUserID`.
- Messages are displayed with the sender's username.
- The chat history is updated in real-time using AJAX polling.

## Customization

You can customize the chat room by modifying the script:

- Change the `port` variable in the `run_server` function to use a different port number.
- Modify the `common_names` list to add or change the list of common anonymous names.
- Adjust the `setInterval` function in the JavaScript section to control how often the chat history is updated.

## Notes

- This is a simple implementation for educational purposes and may not be suitable for production use.
- The script uses the Python `http.server` module, which is meant for basic server needs. For more advanced features, consider using dedicated web frameworks.


---

**Disclaimer**: This project was created for educational purposes and should not be used in production environments without appropriate modifications and security considerations.
