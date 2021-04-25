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
# This file is used to print messages to the console

from os import system


def clear():
    _ = system('clear')


def welcome():
    clear()
    print('Welcome to TemperatureLights!\n')
    print('Press + or - to change brightness level')
    print('Press Q to quit')


def goodbye():
    clear()
    print('\nGoodbye!')


def exiting():
    print('\nExiting... please wait')


def pigpio():
    print('\nPiGPIO is either not installed or not currently running.')
    print('Please install/start PiGPIO and try again.\n')
    print('$ sudo pigpiod\n')
