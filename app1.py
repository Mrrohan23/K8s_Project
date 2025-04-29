import socket
import time
import random

RTU_IP = '127.0.0.1'   # RTU IP address
RTU_PORT = 15000       # RTU listening port

binary_state = 0

# Define sensor IDs
SENSOR_IDS = {
    'temperature': 'T001',
    'pressure': 'P001',
    'humidity': 'H001',
    'binary': 'B001'
}

while True:
    try:
        # Generate random sensor values
        temperature = round(random.uniform(20.0, 30.0), 2)   # °C
        pressure = round(random.uniform(1000.0, 1025.0), 2)  # hPa
        humidity = round(random.uniform(40.0, 70.0), 2)      # %
        # Toggle binary state (0 or 1)
        binary_state = 1 if binary_state == 0 else 0

        # Create the payload including sensor IDs
        payload = f"{SENSOR_IDS['temperature']}:{temperature}," \
                  f"{SENSOR_IDS['pressure']}:{pressure}," \
                  f"{SENSOR_IDS['humidity']}:{humidity}," \
                  f"{SENSOR_IDS['binary']}:{binary_state}"

        print(f"[SENDING] {payload}")

        # Send it over TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((RTU_IP, RTU_PORT))
            s.sendall(payload.encode('utf-8'))

    except Exception as e:
        print(f"[ERROR] {e}")

    time.sleep(1)

