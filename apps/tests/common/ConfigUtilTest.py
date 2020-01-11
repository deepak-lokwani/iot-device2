import unittest


"""
Test class for the ConfigUtil module.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class ConfigUtilTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		#self.configUtil = ConfigUtil()
		#self.configUtil.loadConfig()
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass
	
	"""
	Tests retrieval of a boolean property.
	"""
	def testGetBooleanProperty(self):
		# TODO: implement this
		pass
	
	"""
	Tests retrieval of an integer property.
	"""
	def testGetIntegerProperty(self):
		# TODO: implement this
		pass
	
	"""
	Tests retrieval of a string property.
	"""
	def testGetProperty(self):
		# TODO: implement this
		pass
	
	"""
	Tests if a property exists.
	"""
	def testHasProperty(self):
		# TODO: implement this
		pass

	"""
	Tests if a section exists.
	"""
	def testHasSection(self):
		# TODO: implement this
		pass
	
	"""
	Tests if the configuration is loaded.
	"""
	def testIsConfigDataLoaded(self):
		#if self.configUtil.isConfigDataLoaded():
		#	pass
		#else:
		#	self.fail("Configuration data not loaded.")
		pass
	
if __name__ == "__main__":
	unittest.main()
