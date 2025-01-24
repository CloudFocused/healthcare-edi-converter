import unittest
import pandas as pd

# Import the Converter module
from healthcare_edi_converter.converter import generate_edi
from healthcare_edi_converter.models.claim_dto import ClaimData, ClaimLine, Payer,RenderingProvider



class TestHealthClaim837_Generate(unittest.TestCase):
    # ARRANGE
    def setUp(self):

        payer = Payer('Payer Name', '12345', '123 Sesame Street','555-1212')
        rendering_provider = RenderingProvider('Provider Name','1003002510',None,'123 Sesame Street')


        claimlines =[]
        claimlines.append(ClaimLine('11111111', '19110', 'Claim Line 1',0.00,2,None,['N61']))
        claimlines.append(ClaimLine('11111111', '19110', 'Claim Line 2',0.00,2,None,['N61']))
        claimlines.append(ClaimLine('11111111', '19110', 'Claim Line 3',0.00,2,None,['N61']))

        self.claim = ClaimData('11111111','2025-01-22','Jane','Doe','1973-10-08','F','12345678',payer,rendering_provider,0.00,['A31','B25'],'TESTCASE','A34512355',claimlines)



    def test_generate(self):
        #ACT
        gen = generate_edi('Big Sender', 'Sad Reciever', self.claim)        
        
        #ASSERT
        self.assertIsInstance(gen, str)

        pass


    



if __name__ == "__main__":
    unittest.main()
