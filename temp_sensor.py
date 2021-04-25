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
# This file initializes and reads the temperature from the sensore module
#
# Uses DS18B20 Temperature Sensor Module Kit with Waterproof Stainless Steel Probe for Raspberry Pi
#
# See: https://www.taygan.co/blog/2018/03/10/how-to-build-a-raspberry-pi-temperature-sensor
# See: https://albertherd.com/2019/01/02/connecting-a-ds18b20-thermal-sensor-to-your-raspberry-pi-raspberry-pi-temperature-monitoring-part-1/


# Built-in/Generic Imports
import os

# Default location
BASE_DIR = '/sys/bus/w1/devices/'

# Use the device's unique ID found in BASE_DIR
DEVICE_ID = '28-01204e863250'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()

    return lines


def read_temp():
    lines = read_temp_raw()

    while lines[0].strip()[-3:] != 'YES':
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_c = round(temp_c, 2)
        temp_f = round((temp_c * 1.8) + 32, 2)

        return temp_c, temp_f


def init():
    global device_file

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    device_file = BASE_DIR + DEVICE_ID + '/w1_slave'
