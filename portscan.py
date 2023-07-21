import socket

def check_open_ports(target_host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout süresi (1 saniye), açık olmayan portları hızlı bir şekilde kontrol etmek için.
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_host = input("Hedef IP adresini girin: ")
    start_port = int(input("Başlangıç portunu girin: "))
    end_port = int(input("Bitiş portunu girin: "))

    open_ports = check_open_ports(target_host, start_port, end_port)
    if open_ports:
        print("Açık olan portlar:")
        for port in open_ports:
            print(port)
    else:
        print("Açık port bulunamadı.")
