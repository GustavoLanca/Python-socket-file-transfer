import socket
import os
import hashlib

HOST = '0.0.0.0'
PORT = 5000
SAVE_DIR = os.path.expanduser('~/Pictures/')

def start_server():
    os.makedirs(SAVE_DIR, exist_ok=True)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                image_data = b""
                while True:
                    chunk = conn.recv(4096)
                    if not chunk:
                        break
                    image_data += chunk
                
                if image_data:
                    file_hash = hashlib.sha256(image_data).hexdigest()
                    file_path = os.path.join(SAVE_DIR, f"{file_hash}.png")
                    
                    with open(file_path, 'wb') as f:
                        f.write(image_data)

if __name__ == "__main__":
    start_server()