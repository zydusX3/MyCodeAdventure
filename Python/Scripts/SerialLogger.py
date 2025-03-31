import serial
import time
from datetime import datetime

port = "COM22"
baud = 115200
date_str = datetime.now().strftime("%d%m%Y")
filename = f"arduino_log_{date_str}.txt"

with serial.Serial(port, baud, timeout=1) as ser, open(filename, "a") as log:
    print(f"Logging from {port} at {baud} baud...")
    print(f"Saving to file: {filename}")
    try:
        while True:
            line = ser.readline().decode(errors='ignore').strip()
            if line:
                print(line)
                log.write(line+"\n")
    except KeyboardInterrupt:
        print("Logging stopped by User")
