# -*- coding = utf-8 -*-

from Flags import Flags
import keyboard


flags = Flags()


def on_press_key(e):
    if e.event_type == 'up':
        if e.name == 'space': print('Pressed space')
        elif e.name == 'd':
            if not flags.dictation:
                print('Dictation start time')
                flags.dictation.switch()
            else:
                print('Dictation end time, then enter dictation env')
                input('(Dictation) >>> ')
                flags.dictation.switch()
        elif e.name == 'l':
            if not flags.lyrics:
                print('Show lyrics')
                flags.lyrics.switch()
            else:
                print('Close lyrics')
                flags.lyrics.switch()
        elif e.name == 'w':
            if flags.lyrics:
                print('Word record')


keyboard.hook(on_press_key)

keyboard.wait('esc')