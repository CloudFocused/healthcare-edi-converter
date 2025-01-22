from ..elements.identifier import Identifier
from ..elements.dollars import Dollars
from ..elements.service_code import ServiceCode
from ..elements.service_qualifier import ServiceQualifer
from ..elements.service_modifier import ServiceModifier
from ..elements.integer import Integer
from ..segments.utilities import split_segment, get_element


class Service:
	identification = 'LX'

	identifier = Identifier()
	assigned_number = Integer()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.assigned_number = segment[1]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
