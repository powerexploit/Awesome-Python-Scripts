
import pyautogui
import math
import sys


SIZE_X, SIZE_Y = pyautogui.size()
STEPS = 90
TIME_STEP = 0.001


for i in range(0,STEPS):	
	
	pyautogui.click()
	
	j = (((i/STEPS)*2)*math.pi)
	x = math.cos(j) 
	y = math.sin(j) 
	pyautogui.moveTo( SIZE_X/2 + (SIZE_Y/3)*x
			,SIZE_Y/2 + (SIZE_Y/3)*y, duration=TIME_STEP)
