# LCD Example
#
# Note: To run this example you will need a LCD Shield for your OpenMV Cam.
#
# The LCD Shield allows you to view your OpenMV Cam's frame buffer on the go.

import sensor, image, lcd

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.LCD) # Special 128x160 framesize for LCD Shield.
lcd.init(width=132, height=160) # Initialize the lcd screen.

while(True):
    lcd.display(sensor.snapshot()) # Take a picture and display the image.
