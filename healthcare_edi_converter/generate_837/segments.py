def generate_iea_segment(number_of_included_functional_groups: int, interchange_control_number: str) -> str:
    return f"IEA*{number_of_included_functional_groups}*{interchange_control_number}~"


def generate_hl_segment(hierarchical_id: int, parent_id: int, level_code: str, child_code: str) -> str:
    return f"HL*{hierarchical_id}*{parent_id}*{level_code}*{child_code}~"

def generate_lx_segment(line_number: int) -> str:
    """
        Generates a Line Number Segment
        line_number: int - Line Number
    """
    return f"LX*{line_number}~"

def generate_sv1_segment(service_id: str, amount: float, units: int) -> str:
    """
        Generates a Service Line Segment
        service_id: str - Service ID (CPT/HCPCS)
        amount: float - Charge amount for the service
        units: int - Number of units for the service
    """    
    return f"SV1*HC:{service_id}*{amount:.2f}*UN*{units}~"

def generate_sv2_segment(revenue_code: str, service_id: str, amount: float, units: int, unit_days: int) -> str:
    """
        Generates a Service Line Segment
        revenue_code: str - Revenue Code
        service_id: str - Service ID (CPT/HCPCS)
        amount: float - Charge amount for the service
        units: int - Number of units for the service
        unit_days: int - Number of days for the service
    """    
    return f"SV2*{revenue_code}*{service_id}*{amount:.2f}:UN*{units}*{unit_days}~"







def generate_hi_segment(qualifier: str, diagnosis_code:str, admission_indicator: str) -> str:
    """
        Health Care Code Information
        qualifier - Common qualifier codes are: ABF - Principal Diagnosis, ABK - Admitting Diagnosis, ABN - External Cause of Injury, ABK - Admitting Diagnosis, ABN - External Cause of Injury, ABF - Principal Diagnosis, ABK - Admitting Diagnosis, ABN - External Cause of Injury, ABK - Admitting Diagnosis, ABN - External Cause of Injury
        diagnosis_code - Diagnosis code without the decimal point
        admission_indicator - Y for Yes, N for No, U for Unknown, W for Not Applicable
        NOTES:  Single only for now. This should be a list someday
    """
    return f"HI*{qualifier}:{diagnosis_code}*{admission_indicator}~"



def generate_sbr_segment(payer_responsibility: str, individual_relationship: str, insured_group_number: str, 
                         other_insured_group_name: str, insurance_type_code: str) -> str:
    return f"SBR*{payer_responsibility}*{individual_relationship}*{insured_group_number}*{other_insured_group_name}***{insurance_type_code}~"




def generate_dtp_segment(date_time_qualifier: str, date_time_period_format: str, date_time_period: str) -> str:
    """
        Generates a Date Segment
        date_time_qualifier: str - 291 Date of Service, 472 Service Date, 573 Initial Treatment Date, 314 Last Seen Date, 484 Prescription Date, 435 Admission Date, 472 Discharge Date, 090 Report Start Date, 091 Report End Date, 444 Statement Covers Period, 090 Report Start Date, 091 Report End Date, 444 Statement Covers Period
        date_time_period_format: str - D8 Date Expressed as CCYYMMDD, RD8 Date Expressed as YYMMDD, DTM Date Expressed as CCYYMMDDHHMM, RD8 Date Expressed as YYMMDDHHMM
        date_time_period: str - Date in the format specified in date_time_period_format
    """
    return f"DTP*{date_time_qualifier}*{date_time_period_format}*{date_time_period}~"




def generate_nm1_segment(entity_id_code: str, entity_type:str, first_name: str, last_name: str, id_type: str, entity_id: str) -> str:
    """
        entity_id_code: str  - 41 Submitter, 46 Payer, 85 Billing Provider, 87 Pay-to Provider, 88 Referring Provider, 90 Service Facility Location, 98 Rendering Provider
        entity_type: str - 1 Person, 2 Non-Person
        first_name: str - First name of the entity
        last_name: str - Last name OR Org Name the entity
        id_type: str - 24 Employer's Identification Number, 34 Social Security Number 46 Electronic Transmitter Identification Number (ETIN), 57 National Association of Insurance Commissioners Company Code (NAIC), 58 US Federal Tax Identification Number, 99 Other
        entity_id: str - ID of the entity
    """
    return f"NM1*{entity_id_code}*{entity_type}*{last_name}*{first_name}****{id_type}*{entity_id}~"





def generate_n3_segment(address_line1: str, address_line2: str = "") -> str:
    return f"N3*{address_line1}*{address_line2}~"

def generate_n4_segment(city_name: str, state_code: str, postal_code: str, country_code: str = "") -> str:
    return f"N4*{city_name}*{state_code}*{postal_code}*{country_code}~"

def generate_ref_segment(reference_id_qualifier: str, reference_id: str) -> str:
    return f"REF*{reference_id_qualifier}*{reference_id}~"

def generate_se_segment(number_of_included_segments: int, transaction_set_control_number: str) -> str:
    return f"SE*{number_of_included_segments}*{transaction_set_control_number}~"

def generate_ge_segment(number_of_transaction_sets_included: int, group_control_number: str) -> str:
    return f"GE*{number_of_transaction_sets_included}*{group_control_number}~"





def generate_claim_segment(claim_id: str, claim_amount: float) -> str:
    """
        Generates a Claim Segment
        claim_id: str - ID of the claim (Patient Account Number)
        claim_amount: float - Total amount of the claim
    """
    return f"CLM*{claim_id}*{claim_amount:.2f}***11:B:1*Y*A*Y*I~"