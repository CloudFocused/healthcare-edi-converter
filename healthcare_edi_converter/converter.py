
from healthcare_edi_converter.convert_base import Converter_Base
from healthcare_edi_converter.convert837 import Convert837
from healthcare_edi_converter.generate_837 import segments
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



def generate_edi(sender: str, receiver: str, claim: ClaimData) -> str:
    # Implementation to generate EDI from claim and claimlines

    edi_segments = []

    # **********************************
    #          HEADER INFO
    # **********************************
    # Add ISA segment (Interchange Control Header)
    isa_segment = f"ISA*00*          *00*          *ZZ*{sender}*ZZ*{receiver}*210101*1253*^*00501*000000905*0*T*:~"
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
    submitter_segment = segments.generate_nm1_segment('41',2,None,sender,'46','1111111')
    edi_segments.append(submitter_segment)
    


    reciever_segment = segments.generate_nm1_segment('46',2,None,receiver,'46','2222222')
    edi_segments.append(reciever_segment)




    # 2000 Loops BILLING PROVIDER
    hl_segment = segments.generate_hl_segment(1, None, '20', '1')
    edi_segments.append(hl_segment)

    bill_provider_segment = segments.generate_nm1_segment('85',2,'',claim.rendering_provider.name,'XX',claim.rendering_provider.npi)   
    edi_segments.append(bill_provider_segment)




    # 2300 Loops CLAIM INFO
    clm_segment = segments.generate_claim_segment(claim.subscriber, claim.claim_amount)
    edi_segments.append(clm_segment)

    dt_segment = segments.generate_dtp_segment('435','D8',claim.claim_date)     
    edi_segments.append(dt_segment)


    hi_segment = segments.generate_hi_segment('ABK','E119',None)
    edi_segments.append(hi_segment)



    increment = 1
    # 2400 Loops SERVICE LINE INFO
    for claimline in claim.claim_lines:
        lx_segment = segments.generate_lx_segment(increment)
        edi_segments.append(lx_segment)

        sv_segment = segments.generate_sv1_segment(claimline.service_id, claimline.amount, claimline.units)
        edi_segments.append(sv_segment)

        ref_segment = segments.generate_ref_segment('6R',claimline.description)
        edi_segments.append(ref_segment)

        increment += 1






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




