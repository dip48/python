import socket
import requests

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return f"Error getting local IP: {e}"

def get_public_ip():
    try:
        # This service returns your public IP
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.RequestException as e:
        return f"Error getting public IP: {e}"

if __name__ == "__main__":
    print("Local IP Address  :", get_local_ip())
    print("Public IP Address :", get_public_ip())
