import unittest
from labs.module01.SystemCpuUtilTask import SystemCpuUtilTask
from labs.module01.SystemMemUtilTask import SystemMemUtilTask
# from base64 import test

# from test.test_deque import fail


"""
Test class for all requisite Module01 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module01Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
# 	def setUp(self):
# 		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
# 	def tearDown(self):
# 		pass
	
	"""
	Place your comments describing the test here.
	"""
# 	def testSomething(self):
# 		pass

	'''
	this test class tests if the CPU Utilization data received is a float and 
	then verifies if it's in within the permissible range of 0-100%, both inclusive
	'''
	def testSystemCpuUtilTask(self):

		cpuTestData = SystemCpuUtilTask.getDataFromSensor(self)
		self.assertTrue(isinstance(cpuTestData, float), 'CPU Utilization is not a float type number') 	#Default Case
		self.assertTrue(0 <= cpuTestData , 'CPU Usage dropped below 0%') 								#Exception Case 1
		self.assertTrue(cpuTestData <= 100 , 'CPU Usage shot-up above 100%') 							#Exception Case 2
		
		
	'''
	This test class tests if the Memory Utilization data received is a float and 
	then verifies if it's in within the permissible range of 0-100%, both inclusive
	'''	
	def testSystemMemUtilTask(self):

		memoryTestData = SystemMemUtilTask.getDataFromSensor(self)
		self.assertTrue(isinstance(memoryTestData, float), 'Memory utilization is not a float type number')	#Default Case
		self.assertTrue(0 <= memoryTestData , 'Memory Usage dropped below 0%')								#Exception Case 1
		self.assertTrue(memoryTestData <= 100, 'Memory Usage shot-up above 100%')							#Exception Case 2
	
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()