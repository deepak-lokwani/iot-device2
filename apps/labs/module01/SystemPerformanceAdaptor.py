'''
Created on 20-Jan-2020

@author: deepak
NUID: 001316769
'''

from time import sleep
from labs.module01 import SystemCpuUtilTask
from labs.module01 import SystemMemUtilTask
import logging 
import threading



class SystemPerformanceAdaptor(threading.Thread):
    
    '''
    constructor
    '''
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.begin = False
        
        logging.basicConfig(level=logging.INFO , format='    %(asctime)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' )
        
        
    '''
    setting the adaptor switch
    '''
        
    def setAdaptor(self,S):
        self.begin =S
        print('\n  ')
        print('##   System Performance Values at the Logged time (at every 4 seconds) :   ##')
        print('_____________________________________________________________________________')
        
        
    '''
    printing CPU utilization and the virtual memory utilization using psutil library
    '''
    
    def run(self):
        while(self.begin):
            
            cpuUtilObj = SystemCpuUtilTask.SystemCpuUtilTask()
            cpuUtilization = cpuUtilObj.getDataFromSensor()
           
            memUtilObj = SystemMemUtilTask.SystemMemUtilTask()
            memUtilization = memUtilObj.getDataFromSensor()
            
            logging.info('CPU    Utilization = '    +   str(cpuUtilization))           
            logging.info('Memory Utilization = '    +   str(memUtilization))
            
            sleep(2)