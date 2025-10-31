import sensor
import image
import pyb
# 初始化摄像头
def init_camera():
    sensor.reset()  # 重置摄像头
    sensor.set_pixformat(sensor.RGB565)  # 设置像素格式为RGB565（彩色）
    sensor.set_framesize(sensor.SXGAM)    # 设置分辨率为QVGA (320x240)，可根据需要修改
    # 可选：设置更高分辨率（如VGA 640x480），但文件会更大
    # sensor.set_framesize(sensor.VGA)
    sensor.skip_frames(time=2000)  # 等待摄像头稳定（2秒）
    print("摄像头初始化完成")

# 初始化按键（P1引脚）
def init_button():
    # P1引脚设置为输入模式，启用内部上拉电阻（默认高电平，按下时为低电平）
    return pyb.Pin('P1', pyb.Pin.IN, pyb.Pin.PULL_UP)

def main():
    init_camera()
    button = init_button()
    photo_count = 0  # 照片计数器，用于生成唯一文件名

    print("就绪：按下P1按键拍照")
    while True:
        # 检测按键是否按下（低电平）
        if button.value() == 0:
            # 按键消抖：等待50ms后再次检测
            pyb.delay(50)
            if button.value() == 0:  # 确认按键确实按下
                print(f"正在拍摄第 {photo_count + 1} 张照片...")

                # 拍摄图像
                img = sensor.snapshot()

                # 保存图像到SD卡（需确保SD卡已插入）
                filename = f"photo_{photo_count}.jpg"
                img.save(filename)
                print(f"照片已保存：{filename}")

                photo_count += 1  # 计数器递增
                pyb.delay(10)
                # 等待按键释放，避免一次按下多次拍照
                while button.value() == 0:
                    pyb.delay(10)

if __name__ == "__main__":
    main()
