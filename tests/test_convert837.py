import unittest

# Import the convert837 module
from healthcare_edi_converter.convert837 import HealthClaimConverter



class TestHealthClaimConverter(unittest.TestCase):
    # ARRANGE
    def setUp(self):
        with open("tests/sample837Claim.txt", "r") as f:
            self.edi_content = f.read() 

    def test_parse(self):
        #ACT        
        converter = HealthClaimConverter(self.edi_content)
        result = converter.parse()
        #ASSERT
        self.assertIn("Claim", result)

    def test_to_json(self):
        #ACT
        converter = HealthClaimConverter(self.edi_content)
        json_result = converter.to_json()
        #ASSERT
        self.assertTrue(json_result.startswith("{"))
        

if __name__ == "__main__":
    unittest.main()
