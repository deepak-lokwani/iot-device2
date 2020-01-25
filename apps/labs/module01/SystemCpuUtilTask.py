'''
Created on 20-Jan-2020

@author: deepak
NUID: 001316769
'''
import psutil



class SystemCpuUtilTask():
    
    def getDataFromSensor(self):
        cpuUtil = psutil.cpu_percent(0, False)
        return cpuUtil
        