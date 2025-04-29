import socket
import time
import random
RTU_IP = '127.0.0.1'   # Use the IP of your RTU if it's remote
RTU_PORT = 15000       # Must match the C++ RTU listening port
binary_state = 0
while True:
    try:
        # Generate random sensor values
        temperature = round(random.uniform(20.0, 30.0), 2)   # °C
        pressure = round(random.uniform(1000.0, 1025.0), 2)  # hPa
        humidity = round(random.uniform(40.0, 70.0), 2)      # %
        # Toggle binary state (0 or 1)
        binary_state = 1 if binary_state == 0 else 0
        # Create the comma-separated payload
        payload = f"{temperature},{pressure},{humidity},{binary_state}"
        print(f"[SENDING] {payload}")
        # Send it over TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((RTU_IP, RTU_PORT))
            s.sendall(payload.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] {e}")
    time.sleep(3)
    
