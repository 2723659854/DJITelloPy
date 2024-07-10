#Module with individual panorama types defined. You can just import it and use hovever you like
#
#It will save photos from Tello inside folder that's in. You can change this by changing path inside every function.
""" 无人机 """
from djitellopy import Tello
""" 画布 """
import cv2
import time
""" 图像 """
global img

""" 全景图像 """
def panorama_full_clockwise(tello_name):
    """ 无人机名称 """
    tello = tello_name
    """ 关闭画面 """
    tello.streamoff()
    """ 开启画面 """
    tello.streamon()
    """ 执行4次命令 """
    for i in range(4):
        """ 获取当前画面 """
        img = tello.get_frame_read().frame
        """ 写入图像数据 """
        cv2.imwrite(f'Panorama-full-clockwise_{time.time()}.jpg', img)
        """ 暂停1秒 """
        time.sleep(1)
        """ 顺时针旋转80度 """
        tello.rotate_clockwise(80)

    """ 获取当前画面 """
    img = tello.get_frame_read().frame
    """ 写入图像 """
    cv2.imwrite(f'Panorama-full-clockwise_{time.time()}.jpg', img)
    """ 暂停1秒 """
    time.sleep(1)
    """ 顺时针旋转40度 此时无人机回到原来的位置，刚好旋转一周 80*4 + 40 = 360 """
    tello.rotate_clockwise(40)
    """ 关闭图像传输 """
    tello.streamoff()

""" 半全景图像 """
def panorama_half_clockwise(tello_name):
    """ 无人机 """
    tello = tello_name
    """ 关闭画面传输 """
    tello.streamoff()
    """ 开启画面传输 """
    tello.streamon()
    """ 顺时针旋转90度 """
    tello.rotate_counter_clockwise(90)
    """ 重复三次 """
    for i in range(3):
        """ 获取当前画面 """
        img = tello.get_frame_read().frame
        """ 传输图像 """
        cv2.imwrite(f'Panorama-half-clockwise_{time.time()}.jpg', img)
        """ 暂停1秒 """
        time.sleep(1)
        """ 顺时针旋转60度 """
        tello.rotate_clockwise(60)
    """ 获取当前图像 """
    img = tello.get_frame_read().frame
    """ 传输数据 """
    cv2.imwrite(f'Panorama-half-clockwise_{time.time()}.jpg', img)
    """ 暂停1秒 """
    time.sleep(1)
    """ 旋转90度 """
    tello.rotate_counter_clockwise(90)
    """ 关闭数据传输 """
    tello.streamoff()

""" 逆时针全景图像采集 """
def panorama_full_counter_clockwise(tello_name):
    tello = tello_name
    tello.streamoff()
    tello.streamon()
    """ 获取当前画面，然后旋转80度，执行4次命令，无人机累计旋转320度 """
    for i in range(4):
        img = tello.get_frame_read().frame
        cv2.imwrite(f'Panorama-full-counter-clockwise_{time.time()}.jpg', img)
        time.sleep(1)
        tello.rotate_counter_clockwise(80)
    """ 然后获取画面，在旋转40度，归位 """
    img = tello.get_frame_read().frame
    cv2.imwrite(f'/Panorama-full-counter-clockwise_{time.time()}.jpg', img)
    time.sleep(1)
    tello.rotate_counter_clockwise(40)

    tello.streamoff()

""" 逆时针半全景采集 """
def panorama_half_counter_clockwise(tello_name):
    tello = tello_name
    tello.streamoff()
    tello.streamon()
    """ 先旋转90度 """
    tello.rotate_clockwise(90)
    """ 获取画面，旋转60度，执行三次，累计旋转180度 """
    for i in range(3):
        img = tello.get_frame_read().frame
        cv2.imwrite(f'Panorama-half-counter-clockwise_{time.time()}.jpg', img)
        time.sleep(1)
        tello.rotate_counter_clockwise(60)
    """ 获取当前画面，传输图像，然后旋转90度，归位 """
    img = tello.get_frame_read().frame
    cv2.imwrite(f'Panorama_half_counter_clockwise-{time.time()}.jpg', img)
    time.sleep(1)
    tello.rotate_clockwise(90)

    tello.streamoff()
