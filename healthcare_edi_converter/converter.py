
from healthcare_edi_converter.convert_base import Converter_Base
from healthcare_edi_converter.convert837 import Convert837
from healthcare_edi_converter.models.claim_dto import ClaimData, ClaimLine, ClaimData_Flat

from abc import ABC, abstractmethod

def process_file(file_type: str, file_content: str):
    """
    Process the file based on its type and content.
    Args:
        file_type (str): The type of the file (e.g., '837').
        file_content (str): The content of the file.
    Returns:
        dict: A dictionary containing the processed data.
    """
    if file_type == "837":
        from healthcare_edi_converter.convert837 import Convert837
        factory = FileParserFactory837(file_content)
        parser = factory.create_converter()
        parse = parser.parse_edi()
    return parse



def generate_edi(sender: str, reciever: str, claim: ClaimData) -> str:
    # Implementation to generate EDI from claim and claimlines

    edi_segments = []

    # **********************************
    #          HEADER INFO
    # **********************************
    # Add ISA segment (Interchange Control Header)
    isa_segment = f"ISA*00*          *00*          *ZZ*{sender}*ZZ*{reciever}*210101*1253*^*00501*000000905*0*T*:~"
    edi_segments.append(isa_segment)

    # Add GS segment (Functional Group Header)
    gs_segment = "GS*HC*ABCDEFGHIJKLMNO*1234567890*20210101*1253*1*X*005010X222A1~"
    edi_segments.append(gs_segment)

    # Add ST segment (Transaction Set Header)
    st_segment = "ST*837*0001*005010X222A1~"
    edi_segments.append(st_segment)

    # Add BHT segment (Beginning of Hierarchical Transaction)
    bht_segment = "BHT*0019*00*0123*20210101*1253*CH~"
    edi_segments.append(bht_segment)


    # **********************************
    #       CLAIM CONTENT INFO
    # **********************************

    # 1000 Loops SUBMITTER / RECIEVER


    # 2000 Loops BILLING PROVIDER


    # 2300 Loops CLAIM INFO


    # 2400 Loops SERVICE LINE INFO


    # Add other segments based on claim data
    # for claim_line in claim.claim_lines:
    #     clm_segment = f"CLM*{claim_line.claim_id}*{claim_line.amount}***{claim_line.place_of_service}*{claim_line.facility_code}*{claim_line.frequency_code}~"
    #     edi_segments.append(clm_segment)















    # **********************************
    #          TRAILER INFO
    # **********************************

    # Add SE segment
    se_segment = f"SE*{len(edi_segments) + 1}*0001~"
    edi_segments.append(se_segment)

    # Add GE segment
    ge_segment = "GE*1*1~"
    edi_segments.append(ge_segment)

    # Add IEA segment
    iea_segment = "IEA*1*000000905~"
    edi_segments.append(iea_segment)

    # Join all segments into a single EDI string
    edi_content = "\n".join(edi_segments)


    return edi_content




  # Abstract Factory
class EdiConverterFactory(ABC):
    @abstractmethod

    def create_converter(self) -> Converter_Base:
        pass  





# Concrete Factory for 837 files
class FileParserFactory837(EdiConverterFactory):
    def __init__(self, edi_content: str):
        self.edi_content = edi_content

    def create_converter(self) -> Converter_Base:
        return Convert837(self.edi_content)
    





    pass




