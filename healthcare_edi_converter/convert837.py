import json
from typing import List, Iterator, Optional
from dataclasses import dataclass, asdict
from collections import namedtuple
import pandas as pd
from .parse_837.loops.claim import Claim as ClaimLoop
from .parse_837.loops.service import ServiceInstitutional as ServiceLoop
from .parse_837.segments.utilities import find_identifier,split_segment
from .parse_837.loops.patient import Patient as PatientLoop
from .parse_837.loops.billingprovider import Billingprovider as BillingproviderLoop
from .parse_837.loops.subscriber import Subscriber as SubscriberLoop
from .parse_837.loops.payer import Payer as PayerLoop

from .models.claim_dto import ClaimData_Flat as ClaimData_Flat
from .models.claim_dto import ClaimLine as ClaimLine
from .utils import flatten_object
from healthcare_edi_converter.convert_base import Converter_Base

BuildAttributeResponse = namedtuple('BuildAttributeResponse', 'key value segment segments')


class Convert837(Converter_Base):
    """
        Convert837 class to handle the conversion of 837 files by implementing the Converter_Base interface.
        parse_edi() method to parse the 837 file content.
        generate_edi() method to generate the 837 file content from dataframes.
    """


    def __init__(self, edi_content: str):
        self.edi_content = edi_content

    def parse_edi(self) -> pd.DataFrame:

        if self.edi_content is None:
            return {}
        
        # base class has the x12 parsing logic because it's shared among all the types
        if self.parse_x12() == False:
            return {}

        claims = []
        flat_objects = []

        organizations = []
        patient=[]
        billingprovider=[]
        subscriber=[]
        
        self.segments = iter(self.segments)

        segment = None
        pat=PatientLoop()
        bp=BillingproviderLoop()
        sub=SubscriberLoop()
        submit=PayerLoop()
        receive=PayerLoop()


        while True:
            response = self.build_attribute(segment, self.segments)
            segment = response.segment
            

            # no more segments to parse
            if response.segments is None:
                break

            # based on the segment build the appropriate object
            match response.key:
                case None:
                    pass
                case 'interchange':
                    interchange = response.value

                case 'financial information':
                    financial_information = response.value

                case 'organization':
                    organizations.append(response.value)

                case 'claim':
                    response.value.patient = pat
                    response.value.billingprovider = bp
                    response.value.subscriber = sub
                    response.value.submitter = submit
                    response.value.receiver = receive
                    claims.append(response.value)

                    flat_obj = flatten_object(response.value)
                    flat_objects.append(flat_obj)

                case 'patient':
                    patient.append(response.value)
                    pat = response.value

                case 'billingprovider':
                    billingprovider.append(response.value)
                    bp = response.value

                case 'subscriber':
                    subscriber.append(response.value)
                    sub = response.value

                case 'submitter':
                    submit = response.value

                case 'receiver':
                    receive = response.value
                
                case _:
                    pass

        df = pd.DataFrame(flat_objects)
                
        return df


    def build_flat_claim(self, claim: ClaimLoop) -> ClaimData_Flat:
        """
            Build a flat claim from a claim object.
            Args:
                claim (ClaimLoop): The claim object.
            Returns:
                ClaimData_Flat: The flat claim object.
        """

        return ClaimData_Flat(  claim_id=claim.claim.marker,
                                claim_date=None,
                                subscriber_first_name = claim.subscriber.payer[0].entities.first_name,
                                subscriber_last_name =claim.subscriber.payer[0].entities.last_name,
                                subscriber_dob = None,
                                subscriber_gender = None,
                                subscriber_id = claim.subscriber.payer[0].entities.identification_code,
                                payer_name = claim.subscriber.payer[1].entities.name,
                                payer_id = claim.subscriber.payer[1].entities.identification_code,
                                provider_name = claim.rendering_provider.name,
                                provider_npi = claim.rendering_provider.identification_code,
                                provider_specialty = claim.submitter.demographic_information,
                                provider_address = claim.submitter.address,

                                patient_first_name= '',
                                patient_last_name='',
                                patient_dob='',
                                patient_gender='',

                                claim_amount = claim.claim.charge_amount,
                                diagnosis_codes = claim.diagnosis[0].identification
                              
                              )



    def build_attribute(cls, segment: Optional[str], segments: Iterator[str]) -> BuildAttributeResponse:
        """
            Build an attribute based on the segment and segments.
            Args:
                segment (Optional[str]): The current segment.
                segments (Iterator[str]): The iterator of segments.
            Returns:
                BuildAttributeResponse: A namedtuple containing the key, value, segment, and remaining segments.
        """
        if segment is None:
            try:
                segment = segments.__next__()
            except StopIteration:
                return BuildAttributeResponse(None, None, None, None)
        
        identifier = find_identifier(segment)
        identifier2= split_segment(segment)
        
        match identifier:
            case PatientLoop.initiating_identifier:
                patient, segments, segment = PatientLoop.build(segment, segments)
                return BuildAttributeResponse('patient', patient, segment, segments)
            
            case ClaimLoop.initiating_identifier:
                claim, segments, segment = ClaimLoop.build(segment, segments)
                return BuildAttributeResponse('claim', claim, segment, segments)
            
            case SubscriberLoop.initiating_identifier:
                subscriber, segments, segment = SubscriberLoop.build(segment, segments)
                return BuildAttributeResponse('subscriber', subscriber, segment, segments)
            
            case _ if identifier2[0] == BillingproviderLoop.initiating_identifier and identifier2[1] == 'BI':
                billingprovider, segments, segment = BillingproviderLoop.build(segment, segments)
                return BuildAttributeResponse('billingprovider', billingprovider, segment, segments)
                
            case _ if identifier2[0] == PayerLoop.initiating_identifier and identifier2[1] == '41':
                submitter, segments, segment = PayerLoop.build(segment, segments)
                return BuildAttributeResponse('submitter', submitter, segment, segments)
                
            case _ if identifier2[0] == PayerLoop.initiating_identifier and identifier2[1] == '40':
                receiver, segments, segment = PayerLoop.build(segment, segments)
                return BuildAttributeResponse('receiver', receiver, segment, segments)
                
            case _:
                return BuildAttributeResponse(None, None, None, segments)


    def generate_edi(self, data):
        return super().generate_edi(data)

