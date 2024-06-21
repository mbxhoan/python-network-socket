import socket
import time
import json
import os
import threading
import random
from datetime import datetime

HOST = '0.0.0.0'
PORT = 65432
DATA_FILE = 'data.json'
PRINT_LOGS_DIR = 'print_logs'

def generate_random_numbers(n):
    return ''.join([str(random.randint(0, 9)) for _ in range(n)])

def rename_file(file_path, prefix="data"):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_numbers = generate_random_numbers(3)
    dir_name, base_name = os.path.split(file_path)
    new_name = f"{prefix}_{random_numbers}_{timestamp}.json"
    new_file_path = os.path.join(dir_name, PRINT_LOGS_DIR, new_name)
    
    # Create the print_logs directory if it doesn't exist
    os.makedirs(os.path.join(dir_name, PRINT_LOGS_DIR), exist_ok=True)
    
    # Move the file to print_logs directory
    os.rename(file_path, new_file_path)
    return new_file_path

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            client_ip = addr[0]  # Extracting the client IP address
            print(f'Connected by {client_ip}')
            try:
                while True:
                    # Serve data based on client IP address
                    data_file_path = f'data/{client_ip}.json'
                    if os.path.exists(data_file_path):
                        with open(data_file_path, 'r') as f:
                            data = json.load(f)
                        
                        print(json.dumps(data))

                        with conn:
                            print(f'Sending data to {client_ip}')
                            json_data = json.dumps(data).encode('utf-8')
                            conn.sendall(json_data)
                            
                        # After sending, rename and move the file to print_logs directory
                        renamed_file_path = rename_file(data_file_path, prefix=client_ip)
                        print(f"File '{data_file_path}' processed and moved to '{renamed_file_path}'")

            except (ConnectionResetError, BrokenPipeError):
                print(f'Connection with {client_ip} lost')
            except Exception as e:
                print(f'Error: {e}')
            finally:
                conn.close()

def _start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f'Connected by {addr}')
            try:
                while True:
                    if os.path.exists(DATA_FILE):
                        with open(DATA_FILE, 'r') as f:
                            data = json.load(f)
                        
                        print(json.dumps(data))

                        with conn:
                            print(f'Sending data to {addr}')
                            json_data = json.dumps(data).encode('utf-8')
                            conn.sendall(json_data)
                            
                        # After sending, rename and move the file to print_logs directory
                        renamed_file_path = rename_file(DATA_FILE)
                        print(f"File '{DATA_FILE}' processed and moved to '{renamed_file_path}'")

            except (ConnectionResetError, BrokenPipeError):
                print(f'Connection with {addr} lost')
            except Exception as e:
                print(f'Error: {e}')
            finally:
                conn.close()

if __name__ == '__main__':
    start_server()
