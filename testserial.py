import serial

# Replace 'COM3' with your Arduino's port
arduino_port = "COM3"
baud_rate = 9600

try:
    # Initialize serial connection
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    print(f"Connected to Arduino on {arduino_port}")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    exit()

print("Listening for messages...")

try:
    while True:
        # Read a line from the Arduino
        if arduino.in_waiting > 0:
            message = arduino.readline().decode('utf-8').strip()
            if message:
                print(f"Received: {message}")
                # You can add your custom logic here
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    arduino.close()
    print("Serial connection closed.")
