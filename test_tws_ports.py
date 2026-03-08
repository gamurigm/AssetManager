import socket

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        try:
            s.connect((host, port))
            return True
        except:
            return False

ports = [7496, 7497, 4001, 4002, 4000]
print("Checking TWS/Gateway ports...")
for p in ports:
    status = "OPEN" if check_port("127.0.0.1", p) else "CLOSED"
    print(f"Port {p}: {status}")
