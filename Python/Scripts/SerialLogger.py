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


#888888888888888888888888888888888888888888888888888888888888888888888888888888#
import serial
import serial.tools.list_ports
import time
from datetime import datetime

# Common GPS baud rates to try
BAUD_RATES = [9600, 115200, 38400, 4800]

# How many lines to read before confirming GPS data
DETECTION_LINES = 10

def is_gps_data(line):
    return line.startswith("$GP") or line.startswith("$GN")

def find_gps_port():
    ports = serial.tools.list_ports.comports()
    print("Scanning available serial ports...")

    for port_info in ports:
        port = port_info.device
        print(f"Trying port: {port}")
        for baud in BAUD_RATES:
            try:
                with serial.Serial(port, baud, timeout=1) as ser:
                    time.sleep(2)  # Give it time to settle
                    print(f"  Trying baud rate: {baud}")
                    valid_lines = 0
                    for _ in range(DETECTION_LINES):
                        line = ser.readline().decode(errors='ignore').strip()
                        if is_gps_data(line):
                            valid_lines += 1
                    if valid_lines >= 2:
                        print(f"✅ GPS found on {port} at {baud} baud")
                        return port, baud
            except Exception as e:
                continue
    return None, None

def log_gps_data(port, baud):
    date_str = datetime.now().strftime("%d%m%Y")
    filename = f"arduino_log_{date_str}.txt"

    with serial.Serial(port, baud, timeout=1) as ser, open(filename, "a") as log:
        print(f"📡 Logging from {port} at {baud} to '{filename}'")
        try:
            while True:
                line = ser.readline().decode(errors='ignore').strip()
                if line:
                    timestamp = datetime.now().strftime("[%H:%M:%S] ")
                    print(timestamp + line)
                    log.write(timestamp + line + "\n")
        except KeyboardInterrupt:
            print("🔌 Logging stopped by user.")

# ---------- Main logic ----------
port, baud = find_gps_port()
if port:
    log_gps_data(port, baud)
else:
    print("❌ No GPS module detected on any port.")
