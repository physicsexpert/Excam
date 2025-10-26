import pyb
import time

# 配置按键引脚 (可根据实际硬件连接修改引脚号)
button_pin = pyb.Pin('P1', pyb.Pin.IN, pyb.Pin.PULL_UP)

# 按键状态变量
button_state = False
last_state = False
debounce_time = 50  # 去抖时间(毫秒)
last_debounce_time = 0

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

print("按键测试开始，按下按键查看效果...")

while True:
    # 检查按键状态
    if check_button():
        if button_state:
            print("按键被按下")
            # 在这里添加按键按下时的操作
        else:
            print("按键被释放")
            # 在这里添加按键释放时的操作

    # 短暂延时，降低CPU占用
    time.sleep_ms(10)
