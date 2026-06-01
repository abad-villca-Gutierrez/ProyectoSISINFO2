
import unittest
from modelo.revision import Revision

class TestUS2(unittest.TestCase):
    def test_aprobar(self):
        r=Revision('a','b')
        r.aprobar()
        self.assertEqual(r.estado,'Aprobada')

if __name__ == '__main__':
    unittest.main()
