import unittest
from ClassCode import SharesAnalysis

class UnitTesting(unittest.TestCase):
   
    def setUp(self):
        self.share = SharesAnalysis()
        
    def test1(self):
        result = self.share.queryCompResult('Company A')
        self.assertTrue((result == '1991 Mar 3000'))
    
    def test2(self):
        result = self.share.queryCompResult('xyz')
        self.assertTrue((result == 'Invalid company name'))

if __name__ == '__main__':
    unittest.main()