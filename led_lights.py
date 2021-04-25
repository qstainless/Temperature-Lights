#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CEN-4930C-27086 Seminar in Advanced Software Dev
#
# Author: Guillermo Castaneda Echegaray
# License: MIT
# Version: 1.0.1
# Maintainer: Guillermo Castaneda Echegaray
# Email: gce517@gmail.com
# Status: Development
#
# This file initializes and controls the LED strip lights of the project
#
# Uses Led Strip Lights 16.4 Feet Led Lights for Bedroom Party and Home Decoration
#
# See: https://www.amazon.com/stores/L8star/page/E9622CB2-2751-4176-99B9-8BB2EB25ECF5?ref_=ast_bln
#
# See: https://dordnung.de/raspberrypi-ledstrip/


# Libs
import psutil
import pigpio
import common as c

# LED Strip configuration
# Raspberry Pi GPIO Pin assignments
RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

bright = 50

# Limit the project's temperature boundaries
MAX_TEMP = 30.0
MIN_TEMP = 4.0

# RGB values to light up the LED lights based on temperature
RGB_PALETTE = {
    '4.0': '0,0,255',
    '4.5': '0,15,255',
    '5.0': '0,31,255',
    '5.5': '0,48,255',
    '6.0': '0,64,255',
    '6.5': '0,64,255',
    '7.0': '0,96,255',
    '7.5': '0,110,255',
    '8.0': '0,128,255',
    '8.5': '0,144,255',
    '9.0': '0,160,255',
    '9.5': '0,176,255',
    '10.0': '0,192,255',
    '10.5': '0,208,255',
    '11.0': '0,224,255',
    '11.5': '0,219,255',
    '12.0': '0,255,255',
    '12.5': '0,255,230',
    '13.0': '0,255,213',
    '13.5': '0,255,195',
    '14.0': '0,255,170',
    '14.5': '0,255,149',
    '15.0': '0,255,128',
    '15.5': '0,255,106',
    '16.0': '0,255,85',
    '16.5': '0,255,65',
    '17.0': '0,255,42',
    '17.5': '0,255,20',
    '18.0': '0,255,0',
    '18.5': '20,255,0',
    '19.0': '42,255,0',
    '19.5': '65,255,0',
    '20.0': '85,255,0',
    '20.5': '106,255,0',
    '21.0': '128,255,0',
    '21.5': '149,255,0',
    '22.0': '170,255,0',
    '22.5': '195,255,0',
    '23.0': '213,255,0',
    '23.5': '230,255,0',
    '24.0': '255,255,0',
    '24.5': '255,230,0',
    '25.0': '255,213,0',
    '25.5': '255,195,0',
    '26.0': '255,170,0',
    '26.5': '255,149,0',
    '27.0': '255,128,0',
    '27.5': '255,106,0',
    '28.0': '255,85,0',
    '28.5': '255,65,0',
    '29.0': '255,42,0',
    '29.5': '255,20,0',
    '30.0': '255,0,0'
}

abort = False


def init():
    if not check_pigpio():
        c.pigpio()
        quit()
    else:
        c.welcome()
        global pi, pixels
        pi = pigpio.pi()


# Check if the PiGPIO library is running
def check_pigpio():
    process_name = 'pigpio'
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def set_lights(pin, brightness):
    real_brightness = int(int(brightness) * (float(bright) / 255.0))
    pi.set_PWM_dutycycle(pin, real_brightness)


def show(r, g, b):
    set_lights(RED_PIN, r)
    set_lights(GREEN_PIN, g)
    set_lights(BLUE_PIN, b)


# Gets a pre-defined RGB value assigned to a specific temperature
def get_rgb_values(t):
    temp_rgb = round(t * 2) / 2

    if temp_rgb > MAX_TEMP:
        temp_rgb = MAX_TEMP
    if temp_rgb < MIN_TEMP:
        temp_rgb = MIN_TEMP

    return RGB_PALETTE[str(temp_rgb)]


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


