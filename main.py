#########################################
# main.py                               #
# MANSEDS Self-Landing Rocket Code      #
# Contributors: Alex Koch               #
# Defines the main entry point for the  #
# second stage code. Manages the tasks  #
# to be performed.                      #
# Version: First flight 1.0 (09/03/2018)#
# For flight on 11/03/2018              #
#########################################

from camera_module import * # import everything from camera module, this defines the recording of the camera to a file
from barometer import * 
import time
import thread # Allows multi-threading. This is important to allow two different while true loops to run at the same time. 
# This is much more efficient than defining the loop ourselves as the camera and barometer might read at different rates. The
# processor will figure out the best order to execute these processes. This works even though the pi zero is a single cored processor.
import subprocess #  for calling bash commands
import sys # For sys.exit() call
from global_variables.py import *

t_0 = time.time()

def current_time(): # returns the current time, by subtracting off the epoch time
    return time.time() - t_0

def abort(): # Defines the exit point for the application if something goes wrong
    log_file.write(str(current_time) + ": Abort called, saving files...")
    sys.exit()

def initialise_I2C(): # Initialises I2C using bash scripts
    bash_command_1 = "sudo modprobe i2c-dev"
    process = subprocess.Popen(bash_command_1.split(), stdout=subprocess.PIPE)
    bash_output, bash_error = process.communicate()
    log_file.write(str(current_time) + ": Bash command: " + bash_command_1 + " ; with output: " bash_output) # check if need to convert to string
    if(len(bash_error) != 0): # error in command
        log_file.write(str(current_time) + ": Bash command failure, error: " + bash_error)
        abort()

    bash_command_2 = "sudo modprobe i2c-bcm2708"
    process = subprocess.Popen(bash_command_1.split(), stdout=subprocess.PIPE)
    bash_output, bash_error = process.communicate()
    log_file.write(str(current_time) + ": Bash command: " + bash_command_1 + " ; with output: " bash_output) # check if need to convert to string
    if(len(bash_error) != 0): # error in command
        log_file.write(str(current_time) + ": Bash command failure, error: " + bash_error)
        abort()

    time.sleep(0.1)

    bash_command_3 = "sudo chmod 666 /dev/i2c-0"
    process = subprocess.Popen(bash_command_1.split(), stdout=subprocess.PIPE)
    bash_output, bash_error = process.communicate()
    log_file.write(str(current_time) + ": Bash command: " + bash_command_1 + " ; with output: " bash_output) # check if need to convert to string
    if(len(bash_error) != 0): # error in command
        log_file.write(str(current_time) + ": Bash command failure, error: " + bash_error)
        abort()

if '__name__' == '__main__':
    log_file.write("Time / ms     |       Comment")
    log_file.write(str(current_time) + ": Initialising...")

    # Initialise I2C using bash scripts
    initialise_I2C() # Will call abort() if failure occurrs

    # Initialise Threads

    try:
        thread_1 = thread.start_new_thread( , ("Thread 1: Barometer")) # Starts reading the Barometer
        thread_2 = thread.start_new_thread(initialise_camera, ("Thread 2: Camera")) #  Starts the camera module
        
    except:
        log_file.write(str(current_time) + ": ERROR! Initialisation of threads unsuccessful!")
        abort()
    
    log_file.write(str(current_time) + ": Successfully Initialised threads.")
    
    #  wait until the threads have executed
    thread_1.join() 
    thread_2.join()
    
    log_file.write(str(current_time) + ": Program end point reached, saving data...")

    # Save files

    log_file.close()

    # End program
    
    sys.exit()
   
