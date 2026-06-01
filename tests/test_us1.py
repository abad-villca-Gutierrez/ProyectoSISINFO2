
import unittest
from modelo.revision import Revision

class TestUS1(unittest.TestCase):
    def test_estado_pendiente(self):
        self.assertEqual(Revision('a','b').estado,'Pendiente')

if __name__ == '__main__':
    unittest.main()
