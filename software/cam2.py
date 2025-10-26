import sensor
import display
import image
import gc

sensor.reset()  # 初始化相机传感器
sensor.set_framesize(sensor.QQVGA)  # 设为较小尺寸，减少内存占用
sensor.set_pixformat(sensor.RGB565)  # 像素格式

# ========== 调整IDE预览方向的关键配置 ==========
# sensor.set_hmirror(True)  # 水平镜像（左右翻转，取消注释生效）
# sensor.set_vflip(True)   # 垂直翻转（上下翻转，取消注释生效）
# 若要“旋转180度”，可同时开启：sensor.set_hmirror(True); sensor.set_vflip(True)
# ==============================================

lcd = display.SPIDisplay(width=132, height=160)  # 初始化显示屏
ROTATION_HINT = image.ROTATE_270  # LCD显示的旋转（按需调整）
SCALE_X, SCALE_Y =1, 1     # 缩放比例

while True:
    img = sensor.snapshot()  # 采集图像

    # 缩放+可选旋转（针对LCD显示）
    img_processed = img.scale(x_scale=SCALE_X, y_scale=SCALE_Y, hint=ROTATION_HINT)

    # 绘制文字（位置按需调整）
    text_pos = (100, 100) if ROTATION_HINT in (image.ROTATE_90, image.ROTATE_270) else (50, 5)
    img_processed.draw_string(
        *text_pos, "Hello!",
        color=(255, 255, 255),
        scale=1,
        string_rotation=270,

    )

    lcd.write(img_processed)  # 显示到LCD
    print("Free MEM:", gc.mem_free())  # 监控内存使用
