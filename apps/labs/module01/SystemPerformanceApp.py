'''
Created on 20-Jan-2020

@author: deepak
NUID: 001316769
'''
from labs.module01 import SystemPerformanceAdaptor


systemAdaptorObject = None
#creating an instance of SystemPerformanceAdaptor
systemAdaptorObject = SystemPerformanceAdaptor.SystemPerformanceAdaptor()

#set true to the begin for threading
systemAdaptorObject.setAdaptor(True)

#start the thread
systemAdaptorObject.start()