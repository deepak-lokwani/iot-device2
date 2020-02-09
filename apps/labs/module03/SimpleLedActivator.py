'''
Created on 08-Feb-2020

@author: deepa
'''
from time import sleep
import threading
import RPi.GPIO as GPIO

class SimpleLedActivator(threading.Thread):
    '''
    classdocs
    '''
    # boolean to enable led
    enableLed = False
    #thread sleep duration
    sleepTimeLed = 30
    
    def __init__(self, rateInSec = 1):
        '''
        Constructor
        '''
        super(SimpleLedActivator,self).__init__()
        if(rateInSec > 0):
            self.sleepTimeLed = rateInSec
        #set the mode of GPIO
        GPIO.setmode(GPIO.BCM)
        #set the pin and pin value 
        GPIO.setup(17, GPIO.LOW)
        
    def run(self):
        '''
        thread start
        '''
        while True:
            # check the enable led flag
            if self.enableLed:
                #set the output value as high for GPIO pin 17
                GPIO.output(17, GPIO.HIGH)
                sleep(self.sleepTimeLed)
                #set the output value as low for GPIO pin 17
                GPIO.output(17, GPIO.LOW)
        sleep(self.sleepTimeLed)
        
        
    def getSleepTimeLed(self):
        return self.sleepTimeLed
    
    
    def setEnableLedFlag(self, enable):
        GPIO.setup(17, GPIO.LOW)
        self.enableLed = enable
        
        
        
        
    
    
            