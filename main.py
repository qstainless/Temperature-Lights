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
# This project uses a DS18B20 temperature sensor to display the current temperature
# and simultaneously shines a LED strip to a color that matches that current temperature.
# The temperature and HSL values of the LED lights are displayed in a OLED screen.
#
# The project was built using a Raspberry Pi 3B running Ubuntu Server 20.04


# Built-in/Generic Imports
import _thread
import sys
import termios
import time
import tty

# Own modules
import common as c
import oled_display as o
import led_lights as l
import temp_sensor as t
import mqtt_publish as mp
import mqtt_subscribe as ms


# The user may press q or Q to exit the program
def get_ch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


def check_key():
    global abort

    while True:
        c = get_ch()

        if c == '+' and l.bright < 255:
            l.bright = l.bright + 5

        if c == '-' and l.bright > 0:
            l.bright = l.bright - 5

        if (c == 'q' or c == 'Q') and not abort:
            abort = True
            break


# Displays a goodbye message and turns the display off
def exit_program():
    o.refresh_display()

    c.exiting()

    o.display_text("Goodbye!", 0)
    o.display_text("Thanks for all", 16)
    o.display_text("the fish!", 25)

    o.display_output()
    time.sleep(.1)

    # Turn the LED strip lights off
    l.show(0, 0, 0)

    time.sleep(3)

    o.refresh_display()
    o.display_output()

    l.pi.stop()

    c.goodbye()


if __name__ == "__main__":
    l.init()
    o.init()
    t.init()

    _thread.start_new_thread(check_key, ())

    abort = False

    while not abort:
        o.refresh_display()

        # Read the current temperature
        temp_c, temp_f = t.read_temp()

        # Get the RGB values for the current temperature
        rgb_values = l.get_rgb_values(temp_c)
        r, g, b = rgb_values.split(",")

        # Display current temperature and RGB values
        o.display_text("Current Temperature", 0, True)

        text = str(temp_c) + " C / " + str(temp_f) + " F"
        o.display_text(text, 16, True)

        # Display brightness level and color values
        brightness = str(l.bright)
        hex_color = l.rgb_to_hex((int(r), int(g), int(b)))

        text = "Brightness: " + brightness
        o.display_text(text, 30)

        text = "Color: RGB(" + rgb_values + ")"
        o.display_text(text, 43)

        o.display_output()

        # Changes the LED strip lights' color to match the temperature
        l.show(r, g, b)

    exit_program()
