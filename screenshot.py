import os
import sys
import time
import winsound
from datetime import datetime
import pyautogui as pyag
from pynput import keyboard

APP_NAME = 'Screenshot maker'
APP_VER = '1.2.2'
KEY_SCREEN = 'f12'
KEY_EXIT = 'ctrl+end'
HELP_1 = 'Make a screenshot: ' + KEY_SCREEN.upper()
HELP_2 = 'Exit: ' + KEY_EXIT.upper()
DIR_SEP = '/'
SAVE_PATH = 'C:' + DIR_SEP + 'screenshot'
GAME_DIR_DEFAULT = '_default'
# .jpg or .png
FILE_EXT = '.jpg'
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
SOUND_FILE = os.path.join(BASE_DIR, 'shot.wav')

class Screenshot:
    def __init__(self):
        self.show_about()
        self.save_path = SAVE_PATH
        self.ensure_save_path_exists()
        self.game_dir = self.get_game_dir()
        self.full_path = self.get_full_path()
        self.img_path = ''
        print('The application is ready to use')
        print()
        self.ctrl_pressed = False

    def ensure_save_path_exists(self):
        if os.path.exists(self.save_path):
            print('Save directory exists: %s' % self.save_path)
        else:
            os.makedirs(self.save_path)
            print('Save directory created: %s' % self.save_path)

    @staticmethod
    def get_game_dir():
        print('Please enter the name of game or press Enter to use the default directory [%s]' % GAME_DIR_DEFAULT)
        name_of_game = str(input())
        if name_of_game != '':
            return name_of_game
        else:
            print('Using default directory: ' + GAME_DIR_DEFAULT)
            return GAME_DIR_DEFAULT

    def get_full_path(self):
        full_path = self.save_path + DIR_SEP + self.game_dir
        if os.path.exists(full_path):
            print('Directory is exist: %s' % full_path)
        else:
            os.mkdir(full_path)
            print('Directory created: %s' % full_path)
        return full_path

    def grab_screen(self):
        screen = pyag.screenshot()
        filename = self.get_format_time()
        img_name = filename + FILE_EXT
        self.img_path = self.full_path + DIR_SEP + img_name
        screen.save(self.img_path)
        del screen
        print('Screenshot saved: %s' % self.img_path)
        winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME | winsound.SND_ASYNC)

    @staticmethod
    def show_about():
        print(APP_NAME)
        print('Version: ' + APP_VER)
        print(HELP_1)
        print(HELP_2)
        print()

    def on_press(self, key):
        try:
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                self.ctrl_pressed = True
            elif key == keyboard.Key.f12:
                self.grab_screen()
            elif key == keyboard.Key.end and self.ctrl_pressed:
                print('Exit')
                return False
        except AttributeError:
            pass

    def on_release(self, key):
        # Track Ctrl key release
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = False

    def run(self):
        # print('Listening for keyboard events...')
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    @staticmethod
    def get_format_time():
        dto = datetime.now()
        year = str(dto.year)
        month = str(dto.month).zfill(2)
        day = str(dto.day).zfill(2)
        hour = str(dto.hour).zfill(2)
        minute = str(dto.minute).zfill(2)
        second = str(dto.second).zfill(2)
        micros = str(dto.microsecond)
        return year + month + day + '_' + hour + minute + second + '_' + micros

Screenshot().run()
