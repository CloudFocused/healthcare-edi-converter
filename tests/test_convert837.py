import unittest

# Import the convert837 module
from healthcare_edi_converter.converter import process_file



class TestHealthClaimConverter(unittest.TestCase):
    # ARRANGE
    def setUp(self):
        with open("tests/sample837Claim.txt", "r") as f:
            self.edi_content = f.read() 

    def test_parse(self):
        #ACT        
        converter = process_file('837', self.edi_content)
        result = converter
        #ASSERT
        self.assertIn("Claim", result)

 
        

if __name__ == "__main__":
    unittest.main()
