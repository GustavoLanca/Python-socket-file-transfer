import socket
import sys

HOST = '127.0.0.1'
PORT = 5000
IMAGE_PATH = 'minha_imagem_teste.png' 

def send_image():
    try:
        with open(IMAGE_PATH, 'rb') as f:
            image_data = f.read()
    except FileNotFoundError:
        sys.exit(1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(image_data)

if __name__ == "__main__":
    send_image()