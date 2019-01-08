# -*- coding = utf-8 -*-

#导入相应模块
from pygame import mixer
from pynput import keyboard
from pynput.keyboard import Key

#音量初始值(范围是 0~1 )
value = 0.5

#混音器初始化、加载音乐、播放音乐
mixer.init()
mixer.music.load("abandon.mp3")
mixer.music.play()

#设置初始音量
mixer.music.set_volume(value)

def on_press(key):
    global value

    if key == Key.left:
        #暂停
        mixer.music.pause()
    elif key == Key.right:
        #恢复暂停
        mixer.music.unpause()
    elif key == Key.up:
        if value < 1:
            value += 0.1
        mixer.music.set_volume(value)
    elif key == Key.down:
        if value > 0:
            value -= 0.1
        mixer.music.set_volume(value)

#开始监听键盘的动作
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

while True:
    pass