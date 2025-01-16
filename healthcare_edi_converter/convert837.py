import json
from typing import List, Iterator, Optional
from collections import namedtuple
import pandas as pd
from .loops.claim import Claim as ClaimLoop
from .loops.service import Service as ServiceLoop
from .segments.utilities import find_identifier,split_segment
from .loops.patient import Patient as PatientLoop
from .loops.billingprovider import Billingprovider as BillingproviderLoop
from .loops.subscriber import Subscriber as SubscriberLoop
from .loops.payer import Payer as PayerLoop

BuildAttributeResponse = namedtuple('BuildAttributeResponse', 'key value segment segments')

class HealthClaimConverter:
    def __init__(self, edi_content: str):
        self.edi_content = edi_content

    def parse(self) -> dict:


        segments = self.edi_content.split('~')
        segments = [segment.strip() for segment in segments]

        claims = []
        organizations = []
        patient=[]
        billingprovider=[]
        subscriber=[]

        segments = iter(segments)
        segment = None
        pat=PatientLoop()
        bp=BillingproviderLoop()
        sub=SubscriberLoop()
        submit=PayerLoop()
        receive=PayerLoop()


        while True:
            response = self.build_attribute(segment, segments)

            segment = response.segment
            segments = response.segments

            # no more segments to parse
            if response.segments is None:
                break

            if response.key == 'interchange':
                interchange = response.value

            if response.key == 'financial information':
                financial_information = response.value

            if response.key == 'organization':
                organizations.append(response.value)

            if response.key == 'claim':

                response.value.patient=pat
                response.value.billingprovider=bp
                response.value.subscriber=sub
                response.value.submitter=submit
                response.value.receiver=receive

                claims.append(response.value)

            if response.key == 'patient':
                patient.append(response.value)
                pat=response.value

            if response.key == 'billingprovider':

                billingprovider.append(response.value)
                bp=response.value
                
            if response.key == 'subscriber':

                subscriber.append(response.value)
                sub=response.value

            if response.key == 'submitter':
                submit=response.value

            if response.key == 'receiver':
                receive=response.value
        print(organizations)



        #return parsed_segments
    
      
        
        return claims


    def build_attribute(cls, segment: Optional[str], segments: Iterator[str]) -> BuildAttributeResponse:
        if segment is None:
            try:
                segment = segments.__next__()
            except StopIteration:
                return BuildAttributeResponse(None, None, None, None)
        
        identifier = find_identifier(segment)
        identifier2=split_segment(segment)
        
        if identifier == PatientLoop.initiating_identifier:
            patient, segments, segment = PatientLoop.build(segment, segments)

            
            return BuildAttributeResponse('patient', patient, segment, segments)
        
        elif identifier == ClaimLoop.initiating_identifier:

            claim, segments, segment = ClaimLoop.build(segment, segments)
            
            return BuildAttributeResponse('claim', claim, segment, segments)
        
        elif identifier == SubscriberLoop.initiating_identifier:
            subscriber, segments, segment = SubscriberLoop.build(segment, segments)
            
            return BuildAttributeResponse('subscriber', subscriber, segment, segments)
        
        elif (identifier2[0]== BillingproviderLoop.initiating_identifier and identifier2[1] == 'BI' ):
            billingprovider, segments, segment = BillingproviderLoop.build(segment, segments)
            
            return BuildAttributeResponse('billingprovider', billingprovider, segment, segments)
        elif (identifier2[0]== PayerLoop.initiating_identifier and identifier2[1] == '41' ):
            submitter, segments, segment = PayerLoop.build(segment, segments)
            
            return BuildAttributeResponse('submitter', submitter, segment, segments)
        
        elif (identifier2[0]== PayerLoop.initiating_identifier and identifier2[1] == '40' ):
            receiver, segments, segment = PayerLoop.build(segment, segments)
            
            return BuildAttributeResponse('receiver', receiver, segment, segments)

        else:
            return BuildAttributeResponse(None, None, None, segments)




    def to_json(self) -> str:
        return json.dumps(self.parse(), indent=4)