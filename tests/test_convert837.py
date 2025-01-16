import unittest

# Import the convert837 module
from healthcare_edi_converter.convert837 import HealthClaimConverter



class TestHealthClaimConverter(unittest.TestCase):

    def setUp(self):
        with open("tests/sample837Claim.txt", "r") as f:
            self.edi_content = f.read() 

    def test_parse(self):
        
        converter = HealthClaimConverter(self.edi_content)
        result = converter.parse()
        self.assertIn("Claim", result)
      


    def test_to_json(self):
        converter = HealthClaimConverter(self.edi_content)
        json_result = converter.to_json()
        self.assertTrue(json_result.startswith("{"))
        

if __name__ == "__main__":
    unittest.main()
