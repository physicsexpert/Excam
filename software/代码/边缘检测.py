# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Edge detection with Canny:
#
# This example demonstrates the Canny edge detector.
import sensor
import image
import time
import display
lcd = display.SPIDisplay()
sensor.reset()  # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE)  # or sensor.RGB565
sensor.set_framesize(sensor.QQVGA)  # or sensor.QVGA (or others)
sensor.skip_frames(time=2000)  # Let new settings take affect.
sensor.set_gainceiling(8)

clock = time.clock()  # Tracks FPS.
while True:
    clock.tick()  # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot()  # Take a picture and return the image.
    # Use Canny edge detector
    img.find_edges(image.EDGE_CANNY, threshold=(60, 100))
    # Faster simpler edge detection
    # img.find_edges(image.EDGE_SIMPLE, threshold=(100, 255))
    img_processed = img.scale(x_scale=1, y_scale=1, hint=image.ROTATE_90)
    lcd.write(img)  # Take a picture and display the image.
    print(clock.fps())  # Note: Your OpenMV Cam runs about half as fast while
