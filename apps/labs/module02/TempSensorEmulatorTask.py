'''
Created on 30-Jan-2020

@author: deepa
'''
import threading
from labs.common import SensorData
from labs.module02 import SMTPClientConnector
from labs.common import ConfigUtil
from time import sleep
import random
import logging


class TempSensorEmulatorTask(threading.Thread):
   
    configUtil = ConfigUtil.ConfigUtil()
    
    '''
    @param enableEmulator:boolean state of the emulator, initialized to False
    @param timeInterval:time in seconds between each data generation/collection
    @param alertDifference: difference value required for the alert generation
    @param lowValue:lowest value of the temperature achieved/expected
    @param highValue: highest value of the temperature expected/achieved
    @param curTemp: current value of the temperature    
    '''
    def __init__(self, alertdiff):
        '''
        Constructor
        '''
        
        threading.Thread.__init__(self)
        logging.basicConfig(level=logging.INFO , format='    %(asctime)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' )
        self.enableEmulator =   False
        self.sensorData     =   SensorData.SensorData()
        self.connector      =   SMTPClientConnector.SMTPClientConnector()
        self.timeInterval   =   int(self.configUtil.getProperty(self.configUtil.configConst.CONSTRAINED_DEVICE, self.configUtil.configConst.POLL_CYCLES_KEY))
        self.alertDiff      =   alertdiff
        self.lowValue       =   0
        self.highValue      =   30
        self.curTemp        =   0
        
    def setEmulator(self, boolean):
        '''
        method to set the emulator in order to start
        '''
        self.enableEmulator     =   boolean
        
    def run(self):
        '''
        Thread.run default function called when thread 'starts'
        when running, it will generate the random numbers and will update 
        the sensor data registers accordingly. 
        further whenever the threshold is achieved, it will push an email along with logging it to the console
        
        '''
        threading.Thread.run(self)
        while True:
            if(self.enableEmulator):
                
                self.curTemp    =   random.uniform(float(self.lowValue), float(self.highValue))

                self.sensorData.addValue(self.curTemp)
                print('_______________________________________________')
                print(str(self.sensorData.getSensorData()))
            if(abs(self.curTemp  -   self.sensorData.getAvgValue())  >=  self.alertDiff):
                logging.info('/n Excessive Temperature with a difference > ' + str(self.alertDiff) + '/nTriggering Alert')
                self.connector.publishMessage('Temperature Alert:', self.sensorData.getSensorData())
                logging.info('/nEmail Sent')
            sleep(self.timeInterval)