# -*- coding = utf-8 -*-

from __future__ import unicode_literals, print_function

import os
import copy

from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style
import keyboard


SELECTED_LINE = 0
MAIN_MENU = ['play', 'help', 'exit', 'text1', 'text2']

style = Style.from_dict({
    'title': '#ff0066',
    'text': '#44ff00 italic',
})


def html_wrapper(tag_name, content):
    return '<{0}>{1}</{0}>'.format(tag_name, content)


def gen_menu(origin_menu, index):
    menu = copy.deepcopy(origin_menu)
    for line in range(len(menu)):
        if line == index % len(menu):
            menu[line] = html_wrapper('title', '→ ' + menu[line])
        else:
            menu[line] = html_wrapper('text', '  ' + menu[line])
    return menu


def fill_blank(display_lines, blank_line_size):
    for i in range(blank_line_size):
        display_lines.append(html_wrapper('text', ' '))


def display():
    terminal_size = os.get_terminal_size()
    columns = terminal_size.columns
    lines = terminal_size.lines

    display_lines = ['\r']
    display_lines.append(html_wrapper('title', 'Haha'))

    menu_start_line = (lines - 1) // 2 - len(MAIN_MENU) // 2
    blank_line_size = (lines - 1 - len(MAIN_MENU)) // 2

    fill_blank(display_lines, blank_line_size)
    display_lines.extend(gen_menu(MAIN_MENU, SELECTED_LINE))
    fill_blank(display_lines, blank_line_size)

    display_lines = map(lambda x: x, display_lines)

    for line in display_lines:
        print_formatted_text(HTML('\n'.join(display_lines)), style=style)
        #print(line)


def on_press_key(e):
    global SELECTED_LINE
    if e.event_type == 'down':
        if e.name == 'down':
            SELECTED_LINE += 1
            display()
        elif e.name == 'up':
            SELECTED_LINE -= 1
            display()
        elif e.name == 'enter':
            if (SELECTED_LINE % len(MAIN_MENU) == 0):
                print("Playing music")


display()

keyboard.hook(on_press_key)

keyboard.wait('esc')
