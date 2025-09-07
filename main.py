import requests
import time
import os
import http.server
import socketserver
import threading
import pytz
from datetime import datetime
from platform import system

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"VEER SHARMA ")  # Replace with any preferred response text

def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        httpd.serve_forever()

def send_messages():
    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    access_tokens = [token.strip() for token in tokens]

    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('file.txt', 'r') as file:
        text_file_path = file.read().strip()

    with open(text_file_path, 'r') as file:
        messages = file.readlines()
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]
                message = messages[message_index].strip()

                url = f"https://graph.facebook.com/v15.0/t_{convo_id}/"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}

                response = requests.post(url, json=parameters, headers=headers)

                tz = pytz.timezone('Asia/Kolkata')
                current_time = datetime.now(tz).strftime("%I:%M %p")

                if response.ok:
                    print(f"Chud Gyi iski Maa - {current_time}")
                else:
                    print(f"Lode lag gye - {current_time}")

                time.sleep(speed)

        except Exception:
            print("Lode lag gye - unknown time")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.daemon = True
    server_thread.start()

    send_messages()

if __name__ == '__main__':
    main()
    
