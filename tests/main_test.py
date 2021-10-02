import unittest

from Calculator import run
class TestMainMethod(unittest.TestCase):

    def test_run(self):
        self.assertEqual(run("2+(3*5)"), 17)
        self.assertEqual(run("2.54+3.41"), 5.95)
        self.assertEqual(run("2.9+3.9"), 6.8)

if __name__ == '__main__':
    unittest.main()