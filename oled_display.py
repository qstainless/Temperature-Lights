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
# This file initializes and controls the OLED display of the project
#
# Uses HiLetgo 0.96" I2C IIC SPI Serial 128X64 OLED LCD Display 4 Pin Font Color Yellow&Blue
#
# See: https://learn.adafruit.com/monochrome-oled-breakouts/python-setup
# See: https://learn.adafruit.com/monochrome-oled-breakouts/python-usage-2


# Built-in/Generic Imports
import board

# Libs
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# OLED Display
# Define the Reset Pin
oled_reset = None

# Using the 128x64 display
WIDTH = 128
HEIGHT = 64
BORDER = 3
PADDING = 2


def init():
    global draw, font, image, display

    i2c = board.I2C()
    display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

    clear_display()

    # Create blank image (canvas) for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (display.width, display.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black background
    refresh_display()

    # Load default font.
    font = ImageFont.load_default()


# Clear the display
def clear_display():
    display.fill(0)
    display.show()


def refresh_display():
    draw.rectangle((0, 0, display.width, display.height), outline=0, fill=0)


def display_text(text, t, centered=False):
    (font_width, font_height) = font.getsize(text)

    if centered:
        width = display.width // 2 - font_width // 2
    else:
        width = 0

    draw.text(
        (width, t - PADDING),
        text,
        font=font,
        fill=255
    )


def display_output():
    display.image(image)
    display.show()
