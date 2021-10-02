import unittest
import utils.utils as utils
class TestUtilsMethods(unittest.TestCase):

    def test_parenthesisChecker(self):
        self.assertTupleEqual(utils.isParenthesisMatching("2+(3*5)"), (True,''))
        self.assertTupleEqual(utils.isParenthesisMatching("2+(3*5  )  "), (True,''))
        self.assertTupleEqual(utils.isParenthesisMatching("2+(3*(5  )  "), (False, 'Invalid expression paranthesis not matching'))
    
    def test_isValidExpression(self):
        self.assertEqual(utils.isValidIdentifiers("2+(3*5)"), (True,''))
        self.assertEqual(utils.isValidIdentifiers("2.0+(3*5  )  "), (True, ''))
        self.assertEqual(utils.isValidIdentifiers("2aa+(3*(5  )  "), (False, 'Invalid character a'))

if __name__ == '__main__':
    unittest.main()