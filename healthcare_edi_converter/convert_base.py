from abc import ABC, abstractmethod

class Converter_Base(ABC):

    segments=[]

    def __init__(self, edi_content):
        self.edi_content = edi_content


    def parse_x12(self):
        """
            Parse the X12 file content into segments.
            Args:
                self
            Returns:
                True if parsing was successful, False otherwise.
        """
        if self.edi_content is None:
            return False
        self.segments = self.edi_content.split('~')
        self.segments = [segment.strip() for segment in self.segments]
        return True
    



    @abstractmethod
    def parse_edi(self, edi_content):
        pass
    
    @abstractmethod
    def generate_edi(self, data):
        pass


