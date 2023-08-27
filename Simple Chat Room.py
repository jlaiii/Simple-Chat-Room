import random
import string
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Global chat history
chat_history = []
usernames = set()
chat_lock = threading.Lock()

# Common anonymous names
common_names = ["Anonymous", "Slayer", "Stranger", "Visitor", "Mystery"]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(1000)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            user_id = ''.join(random.choices(string.digits, k=3))
            user_name = f'{random.choice(common_names)}{user_id}'
            usernames.add(user_name)
            
            html_response = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Simple Chat Room</title>
            </head>
            <body>
                <h1>Simple Chat Room</h1>
                <div id="chatDiv"></div>
                <input type="text" id="messageInput" placeholder="Type your message..." />
                <button id="sendButton" onclick="sendMessage()">Send</button>
                <script>
                    function sendMessage() {{
                        var messageInput = document.getElementById('messageInput');
                        var message = messageInput.value;
                        messageInput.value = '';
                        
                        var xhr = new XMLHttpRequest();
                        xhr.open('POST', '/message', true);
                        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                        xhr.send('user={user_name}&message=' + encodeURIComponent(message));
                    }}
                    
                    setInterval(function() {{
                        var chatDiv = document.getElementById('chatDiv');
                        var xhr = new XMLHttpRequest();
                        xhr.open('GET', '/chat', true);
                        xhr.onreadystatechange = function() {{
                            if (xhr.readyState === 4 && xhr.status === 1000) {{
                                chatDiv.innerHTML = xhr.responseText;
                            }}
                        }};
                        xhr.send();
                    }}, 1000);
                </script>
            </body>
            </html>
            """
            self.wfile.write(html_response.encode('utf-8'))
        elif self.path == '/chat':
            self.send_response(1000)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            chat_text = '<br>'.join(chat_history)
            self.wfile.write(chat_text.encode('utf-8'))

    def do_POST(self):
        if self.path == '/message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            post_data = post_data.split('&')
            user_name = post_data[0].split('=')[1]
            message = post_data[1].split('=')[1]
            
            message = urllib.parse.unquote(message)  # Decode the message
            
            with chat_lock:
                chat_history.append(f'<strong>{user_name}:</strong> {message}')
            
            self.send_response(1000)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write('Message sent'.encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
