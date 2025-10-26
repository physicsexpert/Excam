import sensor
import time
import display
import image
import mjpeg
import machine
sensor.reset()
sensor.set_pixformat(sensor.RGB565)  # or GRAYSCALE...
sensor.set_framesize(sensor.VGA)  # or QQVGA...
clock = time.clock()
lcd = display.SPIDisplay(width=132, height=161)
led = machine.LED("LED_RED")
led.on()
m = mjpeg.Mjpeg("example.mjpeg")
clock = time.clock()  # 创建一个时钟对象来跟踪FPS。
for i in range(10):
    clock.tick()
    m.write(sensor.snapshot())
    print(clock.fps())
m.close()
led.off()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
while True:
    img = sensor.snapshot()
    img_rgb = img.to_rgb565()  # 转换为 RGB565 格式
    img_copy = img.scale(x_scale=0.5, y_scale=0.8,hint=image.ROTATE_180)
    img.draw_string(
                130,
                10,
                "Hello World!",
                color=(255, 255, 255),
                scale=2,
                mono_space=False,
                char_rotation=0,
                char_hmirror=False,
                char_vflip=False,
                string_rotation=90,
                string_hmirror=False,
                string_vflip=False,
            )
    lcd.write(img_copy)
