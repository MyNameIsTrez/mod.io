import unittest

import test.test_client
import test.test_game
import test.test_mod
import test.test_objects
import test.test_async_client
import test.test_async_game
import test.test_async_mod
import test.test_async_objects

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test.test_client))
suite.addTests(loader.loadTestsFromModule(test.test_game))
suite.addTests(loader.loadTestsFromModule(test.test_mod))
suite.addTests(loader.loadTestsFromModule(test.test_objects))
suite.addTests(loader.loadTestsFromModule(test.test_async_client))
suite.addTests(loader.loadTestsFromModule(test.test_async_game))
suite.addTests(loader.loadTestsFromModule(test.test_async_mod))
suite.addTests(loader.loadTestsFromModule(test.test_async_objects))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
