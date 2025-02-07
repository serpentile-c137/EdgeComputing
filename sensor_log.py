import serial
import csv
import os
from datetime import datetime

# Set the directory where you want to store the data
directory = 'sensor_data_directory'

# Check if the directory exists, and create it if it doesn't
if not os.path.exists(directory):
    os.makedirs(directory)

# Path to the CSV file where sensor data will be stored
file_path = os.path.join(directory, 'sensor_data.csv')

# Connect to the Arduino via the correct COM port
arduino = serial.Serial('/dev/cu.usbmodem11201', 9600)  # Change 'COM3' to your Arduino port (e.g., 'COM5', '/dev/ttyACM0')

# Open or create the CSV file for storing the data
with open(file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header if the file is empty
    if file.tell() == 0:
        writer.writerow(["Timestamp", "Sensor Status"])

    while True:
        # Read the data from the Arduino
        if arduino.in_waiting > 0:
            sensor_data = arduino.readline().decode('utf-8').strip()  # Read and decode the serial data

            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Write the timestamp and sensor data to the CSV file
            writer.writerow([timestamp, sensor_data])
            print(f"{timestamp} - {sensor_data}")  # Print data to console (optional)