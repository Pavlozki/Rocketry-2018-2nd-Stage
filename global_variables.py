# global_variables.py
# MANSEDS Self-Landing Rocket Code
# contributors: Alex Koch
# Defines a set of global variables which can be accessed by the whole program, and 
# may be included in the module files for the barometer and camera


import time

recording = False # A boolean variable to be set to False when camera is not recording and True when camera is recording
is_running = True # The program is running. Is set to false by the camera module after a certain number of seconds recording video
recording_time = 10 # in seconds
log_file = open("log_file" + time.strftime("%d/%m/%Y") + ".txt", "w")
Altitude_file = open ("Altitude.txt", "a")