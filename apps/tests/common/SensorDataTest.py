import unittest
from labs.common import SensorData 
from builtins import isinstance


"""
Test class for all requisite SensorData functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class SensorDataTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		self.sensorData	=	SensorData.SensorData()
		
	

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.sensorData = None
		
	
	"""
	Place your comments describing the test here.
	"""
	def testGetSensorData(self):
		
		self.assertTrue(isinstance(self.sensorData.getValue(), 		int), 'The Current Value is not float')
		self.assertTrue(isinstance(self.sensorData.getAvgValue(), 	int), 'The Average Value is not float')
		self.assertTrue(isinstance(self.sensorData.getMaxValue(), 	int), 'The Maximum Value is not Float')
		self.assertTrue(isinstance(self.sensorData.getMinValue(), 	int), 'The Minimum Value is not Float')
		self.assertTrue(isinstance(self.sensorData.getCount(), 		int), 'The Count Value is not integer')
		self.assertTrue(isinstance(self.sensorData.name, str), 			  'The name is not String')

if __name__ == "__main__":
# 	import sys;sys.argv = ['', 'Test.testName']
	unittest.main()