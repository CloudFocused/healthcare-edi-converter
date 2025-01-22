from typing import Iterator, Tuple, Optional, List
from warnings import warn
from ..segments.claim import Claim as ClaimSegment
from ..segments.subscriber import Subscriber as SubscriberSegment
from ..segments.entity import Entity as EntitySegment
from ..segments.amount import Amount as AmountSegmant
from ..segments.service_adjustment import ServiceAdjustment as ServiceAdjustmentSegment
from ..loops.payer import Payer as PayerLoop
from ..segments.utilities import find_identifier


class Subscriber:
	initiating_identifier = SubscriberSegment.identification
	terminating_identifiers = [
		ClaimSegment.identification,
		SubscriberSegment.identification,
		'LX',
		'HL',
		'SE'
	]

	def __init__(
			self,
			subscriber: SubscriberSegment = None,
			amount:List[AmountSegmant]=None,
			payer: List[PayerLoop] = None,
			adjustments: List[ServiceAdjustmentSegment] = None,

	):
		self.subscriber = subscriber
		self.amount = amount if amount else []
		self.payer = self.payer = payer if payer else []
		self.adjustments = adjustments if adjustments else []



		

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())



	@classmethod
	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Subscriber', Optional[Iterator[str]], Optional[str]]:
		subscriber = Subscriber()
		subscriber.subscriber = SubscriberSegment(segment)

		segment = segments.__next__()
		while True:
			try:
				if segment is None:
					segment = segments.__next__()
		
				identifier = find_identifier(segment)

				if identifier == EntitySegment.identification:
					payer, segments, segment = PayerLoop.build(segment, segments)
					subscriber.payer.append(payer)
				
				elif identifier == ServiceAdjustmentSegment.identification:
					subscriber.adjustments.append(ServiceAdjustmentSegment(segment))
					segment = None

				elif identifier == AmountSegmant.identification:
					subscriber.amount.append(AmountSegmant(segment))
					segment = None



				elif identifier in cls.terminating_identifiers:
					return subscriber, segments, segment

				else:
					segment = None
					message = f'Identifier: {identifier} not handled in subscriber loop.'
					warn(message)

			except StopIteration:
				return subscriber, None, None
