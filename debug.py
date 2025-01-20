import pandas as pd
import os
from healthcare_edi_converter.convert837 import HealthClaimConverter

with open("tests/sample837Claim.txt", "r") as file:
    edi_data = file.read()



converter = HealthClaimConverter(edi_data)
parsed_data = converter.parse()