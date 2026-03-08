
import socket

def is_port_open(host, port, timeout=0.5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

print(f"7497: {is_port_open('127.0.0.1', 7497)}")
print(f"4002: {is_port_open('127.0.0.1', 4002)}")
print(f"7496: {is_port_open('127.0.0.1', 7496)}")
