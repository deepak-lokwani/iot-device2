'''
Created on 20-Jan-2020

@author: deepak
NUID: 001316769
'''
import psutil
class SystemMemUtilTask():
    
    def getDataFromSensor(self):
        memUtil = psutil.virtual_memory().percent
        return memUtil
    