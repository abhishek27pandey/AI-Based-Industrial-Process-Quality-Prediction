import random
import csv
import time

file_name = "industrial_data.csv"

with open(file_name, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "temperature",
        "pressure",
        "speed",
        "vibration",
        "quality"
    ])

    for i in range(100):
        temperature = round(random.uniform(60, 100), 2)
        pressure = round(random.uniform(2, 5), 2)
        speed = round(random.uniform(800, 1500), 2)
        vibration = round(random.uniform(0.1, 2.0), 2)

        if (
            temperature < 85
            and pressure < 4
            and vibration < 1.2
        ):
            quality = "Good"
        else:
            quality = "Poor"

        writer.writerow([
            temperature,
            pressure,
            speed,
            vibration,
            quality
        ])

print("Industrial data generated successfully!")