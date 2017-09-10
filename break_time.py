# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import webbrowser
import time

numberOfIterations = 0


while (numberOfIterations < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=OT4oyuGlCmQ")
    numberOfIterations = numberOfIterations + 1