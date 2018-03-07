import time
import numpy as np
 
import board
# import digitalio # For use with SPI
import busio
 
import adafruit_bmp280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)


# Give it a second before we take readings
sleep(1)
Sea_Level_Pressure_Readings = []
#Takes 5 readings over half a second to find the average ground level pressure
for i in range 5:
    Sea_Level_Pressure.append(bmp280.pressure)
    sleep(0.1)

bmp280.sea_level_pressure = np.mean(Sea_Level_Pressure_Readings)

Altitude_file = open ("Altitude.txt", "a")

Readings = []
Ascent = True
# Writes the temperature, pressure and altitude to a text file every second. 
# There are 10 measurements per second
while True:
    Temperature = bmp280.temperature
    Pressure = bmp280.pressure
    Altitude = bmp280.altitude
    
    # Altitude = (R/g)*T*ln(Po/P)
    # But I think the borometer can find this itself from surface pressure.
    
    Temp_array = [Temperature, Pressure, Altitude]
    
    Readings.append(Temp_array)
    sleep(0.05)
    
    # Writes in the values every 1 second (10 readings)
    if len(readings) = 10:
        
        # Writes the readings to the file
        for i in Readings:
            Altitude_file.write(i + "   ")
        Altitude_file.write("\n")
        
        # If the altitude at the start of the second is greater than the end of the second, 
        #it must be falling
        
        # Can be changed if 1 second is too long
        if Readings[0][2] > Readings[9][2]:
            Ascent = False
            Descent = True
            with open("video_start.txt", "w") as apogee:
                apogee.write("Going down!\n")
            
        Readings = []  # Resets the 'readings' array

    
    
