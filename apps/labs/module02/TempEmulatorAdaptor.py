'''
Created on 30-Jan-2020

@author: deepak
NUID:001316769
This Class sets the emulator ON and starts the thread to retreive the data
'''
from labs.module02 import TempSensorEmulatorTask

simulator = None
simulator = TempSensorEmulatorTask.TempSensorEmulatorTask(10)  #initializing the instance with the threshold of 10
simulator.setEmulator(True)         #setting up the emulator
simulator.start()           #starting the thread