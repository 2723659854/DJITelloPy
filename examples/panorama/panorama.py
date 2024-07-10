#Simply import of "panoramaModule.py" and you can use each function by calling it with name of the drone inside arguments.
""" 无人机 """
from djitellopy import Tello
import cv2
import time
""" 全景模式 """
import panoramaModule

""" 实例化一个无人机 """
tello = Tello()
""" 链接无人机 """
tello.connect()
""" 获取无人机电量 """
print(tello.get_battery())
""" 起飞 """
tello.takeoff()
""" 向上飞行500cm """
tello.move_up(500)
""" 顺时针全景 """
panoramaModule.panorama_half_clockwise(tello)
""" 自动着陆 """
tello.land()
