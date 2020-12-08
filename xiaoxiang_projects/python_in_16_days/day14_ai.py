# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=17

'''
    制作一个智能视频播放器
    下面就把切换视频和播放的功能写进Player中。
'''


import os
from os import startfile
class Player(object):
    def __init__(self):
        # 视频文件总数
        self.fileNum = len(os.listdir('./video'))
        # 当前播放的视频编号
        self.index = 0
    def play(self):
        fileName = './video/' + str(self.index + 1) + '.mp4'
        print('开始播放：', fileName)
        startfile(fileName)
    def next(self):
        self.index = (self.index + 1) % self.fileNum
        self.play()
    def prev(self):
        self.index = (self.index - 1) % self.fileNum
        self.play()
    def start_one(self, index):
        self.index = index
        self.play()

# open cv是一个开源的计算机视觉库，它提供了很多函数，这些函数非常高效地实现了计算机视觉算法。
# 这里还需要调用百度手势识别的API接口。
import cv2 #pip3 install opencv-python
from aip import AipBodyAnalysis #pip install baidu-aip

from threading import Thread
import time
APP_ID = '20804321'
API_KEY = 'ye****************dGZ'
SECRET_KEY = 'jQ****************kPXFm'
# 初始化API调用客户端
gesture_client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
# 初始化摄像头
capture = cv2.VideoCapture(0)

# 显示摄像头拍摄效果
def camera():
    global running
    while running:
        # 获得图片
        ret, frame = capture.read()
        # 在电脑上显示摄像头内容
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
hand = {'One': '第一集', 'Two': '第二集', 'Three': '第三集', 'Four': '第四集',
        'Five': '第五集', 'Fist':'上一集','Ok':'下一集'}
def handle(words):
    # 根据手势做操作
    print('收到', words)
    if words == 'Face':
        print('我不看脸，只看手势！')
        print(hand)
    elif words in hand:
        print(hand[words])
        if words == 'One':
            player.start_one(0)
        elif words == 'Two':
            player.start_one(1)
        elif words == 'Three':
            player.start_one(2)
        elif words == 'Four':
            player.start_one(3)
        elif words == 'Five':
            player.start_one(4)
        elif words == 'Fist':
            player.prev()
        elif words == 'Ok':
            player.next()
    else:
        print('无效手势！')