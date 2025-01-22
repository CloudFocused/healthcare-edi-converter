from typing import Tuple, Iterator, Optional, List
from warnings import warn

from ..segments.service import Service as ServiceSegment
from ..segments.claim import Claim as ClaimSegment
from ..segments.date import Date as DateSegment
from ..segments.reference import Reference as ReferenceSegment
from ..segments.amount import Amount as AmountSegment
from ..segments.service_adjustment import ServiceAdjustment as ServiceAdjustmentSegment
from ..segments.service_line_adjudication import Service_Line_Adjudication as Service_Line_AdjudicationSegment
from ..segments.serviceline import Serviceline_Institutional as ServicelineInstitutionalSegment
from ..segments.serviceline import Serviceline_Professional as ServicelineSegmentProfessionalSegment
from ..segments.drug_identification import Drug_Identification as Drug_IdentificationSegment
from ..segments.drug_quantity import Drug_Quantity as Drug_QuantitySegment
from ..segments.note import Note as NoteSegment

from ..segments.utilities import find_identifier


class ServiceInstitutional:
	initiating_identifier = ServiceSegment.identification
	terminating_identifiers = [
		ServiceSegment.identification,
		ClaimSegment.identification,
		'HL',
		'SE'
	]

	def __init__(
			self,
			service: ServiceSegment = None,
			dates: List[DateSegment] = None,
			references: List[ReferenceSegment] = None,
			serviceline: List[ServicelineInstitutionalSegment] = None,
			amount: AmountSegment = None,
			adjustments: List[ServiceAdjustmentSegment] = None,
			service_line_adjudication: Service_Line_AdjudicationSegment = None,
			drug_identification:Drug_IdentificationSegment=None,
			drug_quantity:Drug_QuantitySegment=None,
			notes: List[NoteSegment] = None,

	):
		self.service = service
		self.dates = dates if dates else []
		self.references = references if references else []
		self.serviceline = serviceline if serviceline else []
		self.amount = amount
		self.adjustments = adjustments if adjustments else []
		self.service_line_adjudication = service_line_adjudication 
		self.drug_identification=drug_identification
		self.drug_quantity=drug_quantity
		self.notes = notes if notes else []

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())

	@classmethod
	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['ServiceInstitutional', Optional[str], Optional[Iterator[str]]]:
		service = ServiceInstitutional()
		service.service = ServiceSegment(segment)

		while True:
			try:
				segment = segments.__next__()
				identifier = find_identifier(segment)

				match identifier:
					case DateSegment.identification:
						date = DateSegment(segment)
						service.dates.append(date)

					case ServicelineInstitutionalSegment.identification:
						serviceline = ServicelineInstitutionalSegment(segment)
						service.serviceline.append(serviceline)

					case ServicelineSegmentProfessionalSegment.identification:
						serviceline = ServicelineSegmentProfessionalSegment(segment)
						service.serviceline.append(serviceline)

					case Service_Line_AdjudicationSegment.identification:
						service.service_line_adjudication = Service_Line_AdjudicationSegment(segment)

					case Drug_IdentificationSegment.identification:
						di = Drug_IdentificationSegment(segment)
						service.drug_identification = di

					case Drug_QuantitySegment.identification:
						dq = Drug_QuantitySegment(segment)
						service.drug_quantity = dq

					case ReferenceSegment.identification:
						reference = ReferenceSegment(segment)
						service.references.append(reference)
					
					case NoteSegment.identification:
						service.notes.append(NoteSegment(segment))
					
					case ServiceAdjustmentSegment.identification:
						service.adjustments.append(ServiceAdjustmentSegment(segment))

					case _ if identifier in cls.terminating_identifiers:
						return service, segment, segments

					case _:
						message = f'Identifier: {identifier} not handled in service loop.'
						warn(message)

			except StopIteration:
				return service, None, None


if __name__ == '__main__':
	pass
