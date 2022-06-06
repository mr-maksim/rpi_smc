
from time import sleep
import RPi.GPIO as GPIO

PUL = 17
DIR = 27
ENA = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)


def step(step, dir, speed=0.1):
    if speed <= 0:
        speed = 0.1
    GPIO.output(ENA, GPIO.HIGH)
    if dir:
        GPIO.output(DIR, GPIO.LOW)
    else:GPIO.output(DIR, GPIO.HIGH)
    for x in range(step):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(speed)
        GPIO.output(PUL, GPIO.LOW)
        sleep(speed)
    GPIO.output(ENA, GPIO.LOW)
    sleep(.5)
    return


def main():
    istep = int(input('Input step:\n'))
    idir = bool(input('Input dir (1/0):\n'))
    ispeed = float(input('Input speed (1/0):\n'))
    step(istep, idir,ispeed)


if __name__ == '__main__':
    main()
