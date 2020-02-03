import unittest
from labs.common import ConfigUtil

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
from builtins import isinstance
from xmlrpc.client import boolean

class ConfigUtilTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.configUtil = ConfigUtil.ConfigUtil()
		self.configUtil.loadConfig()
		

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.configUtil = None
		
	
	"""
	Tests retrieval of a boolean property.
	"""
	def testGetBooleanProperty(self):
		self.assertTrue(isinstance((boolean)(self.configUtil.getProperty("smtp.cloud", "port")), boolean), 'GetProperty is not integer')
		
	
	"""
	Tests retrieval of an integer property.
	"""
	def testGetIntegerProperty(self):
		self.assertTrue(isinstance((int)(self.configUtil.getProperty("smtp.cloud", "port")), int), 'GetProperty is not integer')
	
	
	"""
	Tests retrieval of a string property.
	"""
	def testGetProperty(self):
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "port"), 		"Config does not have Port") #checking for port
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "host"), 		"Config does not have Host") #checking for Host
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "fromAddr"),	"Config does not have From Address") #checking for fromAddr
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "toAddr"), 	"Config does not have toAddr") #checking for toAddr
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "AuthToken"),	"Config does not have AuthToken") #checking for AuthToken
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "toMediaAddr"),"Config does not have toMediaAddr") #checking for toMediaAddr
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "toTxtAddr"),	 "Config does not have toTxtAddr") #checking for toTxtAddr
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "enableAuth"), "Config does not have enableAuth") #checking for enableAuth
		self.assertTrue(self.configUtil.getProperty("smtp.cloud", "enableCrypt"),"Config does not have enableCrypt") #checking for enableCrypt
	
	"""
	Tests if a property exists.
	"""
	def testHasProperty(self):
		self.assertTrue(self.configUtil.hasProperty("port"), 		"Config does not have Port") #checking for port
		self.assertTrue(self.configUtil.hasProperty("host"), 		"Config does not have Host") #checking for Host
		self.assertTrue(self.configUtil.hasProperty("fromAddr"),	"Config does not have From Address") #checking for fromAddr
		self.assertTrue(self.configUtil.hasProperty("toAddr"), 		"Config does not have toAddr") #checking for toAddr
		self.assertTrue(self.configUtil.hasProperty("AuthToken"),	"Config does not have AuthToken") #checking for AuthToken
		self.assertTrue(self.configUtil.hasProperty("toMediaAddr"),	"Config does not have toMediaAddr") #checking for toMediaAddr
		self.assertTrue(self.configUtil.hasProperty("toTxtAddr"),	"Config does not have toTxtAddr") #checking for toTxtAddr
		self.assertTrue(self.configUtil.hasProperty("enableAuth"),	"Config does not have enableAuth") #checking for enableAuth
		self.assertTrue(self.configUtil.hasProperty("enableCrypt"),	"Config does not have enableCrypt") #checking for enableCrypt

	
	"""
	Tests if a section exists.
	"""
	def testHasSection(self):
		
		self.assertTrue(self.configUtil.hasSection("smtp.cloud"), "Config does not have Section")
		
		
	"""
	Tests if the configuration is loaded.
	"""
	def testIsConfigDataLoaded(self):
		self.assertTrue(self.configUtil.hasConfigData(), 'The Config data is not loaded')
		
	
if __name__ == "__main__":
	unittest.main()
