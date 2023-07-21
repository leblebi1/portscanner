import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{message}")
        except:
            break

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("server ip : ")  # Sunucunun açık IP adresini buraya girin
    server_port = int(input("port : ")) # Sunucunun açık portunu buraya girin

    try:
        client_socket.connect((server_ip, server_port))
        username = input("Username: ")
        client_socket.send(username.encode('utf-8'))  # Kullanıcı adını sunucuya gönder
        print(client_socket.recv(1024).decode('utf-8'))  # Bağlantı başarılı mesajı alınır
    except socket.error as e:
        print(f"Error while connecting to the server: {e}")
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_message, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

    send_thread.join()
    client_socket.close()

if __name__ == "__main__":
    start_client()
