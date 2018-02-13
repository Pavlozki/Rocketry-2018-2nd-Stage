#########################################
# camera_module.py                      #
# MANSEDS Self-Landing Rocket Code      #
# Contributors: Matthew Asker           #
# Uses data written to a file from      #
# barometer to indicate when to start   #
# and stop recording using the PiCamera #
#########################################

from picamera import PiCamera # imports module from picamera needed

camera = PiCamera # create an object of the type PiCamera called camera which we can use to control the camera onboard the rocket
recording = 0 # a boolean variable to be set to 0 when camera is not recording and 1 when camera is recording

f = open('video_start.txt','r') # create an object f containing the file written to by the barometer

while True:
    start = f.read() # reads the text from the file and stores in start
    if start == "down" and recording == 0: # if the rocket is travelling downwards and recording has not yet been started
        camera.start_recording('/home/pi/video.h264') # uses PiCamera method for camera object to start recording
        recording = 1 # indicate that recording is started
    elif start == "landed": # if the rocket is stationary then it has landed
        camera.stop_recording() # uses PiCamera method for camera object to stop recording