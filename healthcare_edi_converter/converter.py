
from healthcare_edi_converter.convert_base import Converter_Base
from healthcare_edi_converter.convert837 import Convert837
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