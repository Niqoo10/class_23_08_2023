import unittest
from App.app import multiplicacion

class TestNumber(unittest.TestCase):

    def test_mult(self):
        self.assertEqual(multiplicacion(2, 3), 
                         6,
                         )

if __name__ == '__main__':
    unittest.main()