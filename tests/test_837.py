import unittest
import pandas as pd

# Import the convert837 module
from healthcare_edi_converter.converter import process_file


class TestHealthClaim837_Parse(unittest.TestCase):


    # ARRANGE
    def setUp(self):
        with open("tests/111111.edi", "r") as f:
            self.edi_content = f.read() 


    def test_parse(self):
        #ACT        
        converter = process_file('837', self.edi_content)
        

        #ASSERT
        self.assertIsInstance(converter, pd.DataFrame)
        self.assertGreater(len(converter), 0)
       # print(converter.columns.tolist())
        
        #converter.to_parquet('tests/sample837Claim.parquet', engine="pyarrow" ,index=False)


if __name__ == "__main__":
    unittest.main()
