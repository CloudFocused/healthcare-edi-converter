from ..elements.identifier import Identifier
from ..elements.claim_status import ClaimStatus
from ..elements.dollars import Dollars
from ..segments.utilities import split_segment


class Diagnosis:
	identification = 'HI'

	identifier = Identifier()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.diagnosis_codes = segment[1:]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
