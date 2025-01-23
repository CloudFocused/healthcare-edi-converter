def generate_iea_segment(number_of_included_functional_groups: int, interchange_control_number: str) -> str:
    return f"IEA*{number_of_included_functional_groups}*{interchange_control_number}~"

def generate_hl_segment(hierarchical_id: int, parent_id: int, level_code: str, child_code: str) -> str:
    return f"HL*{hierarchical_id}*{parent_id}*{level_code}*{child_code}~"

def generate_sbr_segment(payer_responsibility: str, individual_relationship: str, insured_group_number: str, 
                         other_insured_group_name: str, insurance_type_code: str) -> str:
    return f"SBR*{payer_responsibility}*{individual_relationship}*{insured_group_number}*{other_insured_group_name}***{insurance_type_code}~"

def generate_dtp_segment(date_time_qualifier: str, date_time_period_format: str, date_time_period: str) -> str:
    return f"DTP*{date_time_qualifier}*{date_time_period_format}*{date_time_period}~"

def generate_nm1_segment(entity_type: str, first_name: str, last_name: str, id_type: str, entity_id: str) -> str:
    return f"NM1*{entity_type}*1*{last_name}*{first_name}****{id_type}*{entity_id}~"

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
    return f"CLM*{claim_id}*{claim_amount:.2f}***11:B:1*Y*A*Y*I~"