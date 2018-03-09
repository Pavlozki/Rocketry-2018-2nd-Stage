#########################################
# camera_module.py                      #
# MANSEDS Self-Landing Rocket Code      #
# Contributors: Matthew Asker           #
# Uses data written to a file from      #
# barometer to indicate when to start   #
# and stop recording using the PiCamera #
#########################################

import picamera # imports module from picamera needed
import time
from global_variables import *

def initialise_camera():
    with picamera.PiCamera() as camera:

        camera.resolution = (640,480)

        while is_running:
            if recording:
                camera.start_recording('video.h264') # uses PiCamera method for camera object to start recording
                recording = 1 # indicate that recording is 
            
            elif !recording:
                camera.stop_recording() # uses PiCamera method for camera object to stop recording
            time.sleep(2)
