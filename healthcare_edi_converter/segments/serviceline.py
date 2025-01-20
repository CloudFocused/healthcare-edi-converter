from typing import Optional
from ..elements.identifier import Identifier
from ..segments.utilities import split_segment


class ServiceLine:
	"""
		Service Line Base Class
	"""
	identification = ''
	identifier = Identifier()
	procedurecode:str = Optional[str]
	revenuecode:str = Optional[str]
	chargeamount:str = Optional[str]
	measurementcode:str = Optional[str]
	units:str = Optional[str]

	
	def __repr__(self) -> str:
		return '\n'.join(str(item) for item in self.__dict__.items())
	



class Serviceline_Professional(ServiceLine):
	"""
		SV1: Service Line Information for Professional Claims
	"""
	identification = 'SV1'
	identifier = Identifier()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)
		self.identifier = segment[0]
		self.procedurecode = segment[1]
		self.chargeamount = segment[2]
		self.measurementcode = segment[3]
		self.units = segment[4]




class Serviceline_Institutional(ServiceLine):
	"""
		SV2: Service Line Information for Institutional Claims
	"""
	identification = 'SV2'
	identifier = Identifier()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)
		self.identifier = segment[0]
		self.revenuecode=segment[1]
		self.procedurecode = segment[2]
		self.chargeamount = segment[3]
		self.measurementcode = segment[4]
		self.unitdays = segment[5]


if __name__ == '__main__':
	pass
