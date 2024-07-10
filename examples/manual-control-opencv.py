# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

# 简单的演示如何用键盘控制Tello
# 欲使用全手动控制请查看 manual-control-pygame.py
#
# W, A, S, D 移动， E, Q 转向，R、F上升与下降.
# 开始运行程序时Tello会自动起飞，按ESC键降落
# 并且程序会退出

from djitellopy import Tello
import cv2, math, time
""" 无人机建立链接 """
tello = Tello()
tello.connect()

tello.streamon()
""" 画面读取器摄像头 """
frame_read = tello.get_frame_read()
""" 起飞 """
tello.takeoff()

""" 死循环，等待用户指令，控制飞行动作 """
while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    # 在实际开发里请在另一个线程中显示摄像头画面，否则画面会在无人机移动时静止
    """ 读取画面 """
    img = frame_read.frame
    """ 屏幕显示画面 """
    cv2.imshow("drone", img)
    """ 等待用户输入键盘指令 换算为16进制 """
    key = cv2.waitKey(1) & 0xff
    """ 退出 """
    if key == 27: # ESC
        break
    """ 前进 """
    elif key == ord('w'):
        tello.move_forward(30)
    """ 后退 """
    elif key == ord('s'):
        tello.move_back(30)
    """ 向左 """
    elif key == ord('a'):
        tello.move_left(30)
    """ 向右 """
    elif key == ord('d'):
        tello.move_right(30)
    """ 顺时针旋转30度 """
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    """ 逆时针旋转 """
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    """ 攀升 """
    elif key == ord('r'):
        tello.move_up(30)
    """ 下降 """
    elif key == ord('f'):
        tello.move_down(30)
    """  """
""" 自动着陆 """
tello.land()
