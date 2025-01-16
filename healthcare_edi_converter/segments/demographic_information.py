from ..elements.identifier import Identifier
from ..elements.date import Date as DateElement
from ..elements.date_qualifier import DateQualifier
from ..segments.utilities import split_segment


class Demographic_information:
	identification = 'DMG'

	identifier = Identifier()
	date = DateElement()
	qualifier = DateQualifier()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.qualifier = segment[1]
		self.date = segment[2]
		self.gender_code=segment[3]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
