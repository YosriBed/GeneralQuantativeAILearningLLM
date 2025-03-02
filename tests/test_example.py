"""
Basic test file for example_module.
"""

import unittest
from my_python_project.modules.example_module import example_function

class TestExampleModule(unittest.TestCase):
    def test_example_function(self):
        self.assertIsNone(example_function())  # Just checking if it runs

if __name__ == "__main__":
    unittest.main()
