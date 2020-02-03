import unittest

from labs.module02 import SMTPClientConnector
from labs.module02 import TempSensorEmulatorTask
import smtplib
from _ast import If

"""
Test class for all requisite Module02 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module02Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		self.smtpconnect = SMTPClientConnector.SMTPClientConnector()
		self.tempEmul	=	TempSensorEmulatorTask.TempSensorEmulatorTask(10)
		self.currentValue = self.tempEmul.sensorData.getValue()
		self.smtp = smtplib.SMTP()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.smtpconnect = None
		self.tempEmul	 = None
		self.currentValue= None
		
	"""
	Test Class for TempSensorEmulatorTask
	"""
	def testTempSensorEmulatorTask(self):
		#checks if the sensor data is float and between 0 to 30
		self.assertTrue(isinstance(self.currentValue, int), "Current Sensor Data Value is not Float")
		self.assertGreaterEqual(self.currentValue, 0, "Current Value is lesser than 0")
		self.assertLessEqual(self.currentValue, 30, "Current Value is greater than 30")
	
	'''
	This test class checks the integrity of the SMTP clinet Connector class by checking if the internet connection is available or not
	'''	
	def testSMTPCLientConnector(self):
		self.assertTrue(self.connectT(), "No SMTP Server/Internet Connection Available")
		self.assertTrue(self.smtpconnect.publishMessage("This is a Test", "Data"), "connection Not established")

	'''
	this class is created to test the internet connectivity
	'''
	def connectT(self):
		if(self.smtp.connect('smtp.gmail.com', 587)):
			return True
		else:
			return False
			
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()