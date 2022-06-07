from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from time import sleep
import RPi.GPIO as GPIO


class Main_Screen(Screen):
    def left(self):
        step(5000, 0)


class Screen_2(Screen):
    pass


class ScrM(ScreenManager):
    pass


class RPI_SMCApp (MDApp):
    def build(self):
        return Builder.load_file('rpi_smc.kv')


if __name__ == '__main__':
    RPI_SMCApp().run()
