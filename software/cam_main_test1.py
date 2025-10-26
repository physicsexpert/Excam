import sensor
import image
import time
import display
import pyb
from pyb import Pin, Timer

from machine import LED
led = LED("LED_BLUE")
light = Timer(2, freq=50000).channel(1, Timer.PWM, pin=Pin("P6"))
light.pulse_width_percent(0)  # adjust light 0~100
led.on()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)  # or GRAYSCALE...
sensor.set_framesize(sensor.QCIF)  # or QQVGA...
sensor.skip_frames(time=2000)
clock = time.clock()
lcd = display.SPIDisplay()
ROTATION_HINT = image.ROTATE_180  # LCD显示的旋转（按需调整）
SCALE_X, SCALE_Y =1, 1
# 缩放比例


# 配置按键引脚 (可根据实际硬件连接修改引脚号)
button_pin = pyb.Pin('P1', pyb.Pin.IN, pyb.Pin.PULL_UP)

# 按键状态变量
button_state = False
last_state = False
debounce_time = 50  # 去抖时间(毫秒)
last_debounce_time = 0


vflip_state = 0


def check_button():
    """检测按键状态，包含去抖处理"""
    global button_state, last_state, last_debounce_time

    # 读取当前引脚状态
    current_state = not button_pin.value()  # 因为使用上拉电阻，按下时为低电平
    current_time = time.ticks_ms()

    # 检测到状态变化
    if current_state != last_state:
        last_debounce_time = current_time

    # 状态稳定超过去抖时间
    if time.ticks_diff(current_time, last_debounce_time) > debounce_time:
        if current_state != button_state:
            button_state = current_state
            return True  # 状态发生变化
    last_state = current_state
    return False  # 状态未发生变化




while True:
    clock.tick()

    img = sensor.snapshot()


    if check_button():
        if button_state:
            print("按键被按下")
            if vflip_state == 0:
                sensor.set_vflip(True)  # 开启翻转
                print("开启翻转")
                vflip_state = 1
            else:
                sensor.set_vflip(False)  # 关闭翻转
                print("关闭翻转")
                vflip_state = 0


#     for i in range(10):
#         x0 = randint(0, 2 * img.width()) - img.width() // 2
#         y0 = randint(0, 2 * img.height()) - img.height() // 2
#         x1 = randint(0, 2 * img.width()) - img.width() // 2
#         y1 = randint(0, 2 * img.height()) - img.height() // 2

#         r = randint(0, 127) + 128
#         g = randint(0, 127) + 128
#         b = randint(0, 127) + 128

        # If the first argument is a scaler then this method expects
        # to see x0, y0, x1, and y1. Otherwise, it expects a (x0,y0,x1,y1) tuple.
#         img.draw_arrow(x0, y0, x1, y1, color=(r, g, b), size=30, thickness=2)
    img_processed = img.scale(x_scale=SCALE_X, y_scale=SCALE_Y, hint=image.ROTATE_90)
    lcd.write(img)  # Take a picture and display the image.
    img_processed = img.scale(x_scale=SCALE_X, y_scale=SCALE_Y, hint=image.ROTATE_90)

    print(vflip_state)
