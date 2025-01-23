from dataclasses import dataclass, field, asdict
from typing import List, Optional

@dataclass
class Subscriber:
    first_name: str
    last_name: str
    dob: Optional[str] = None  # Date of Birth (YYYY-MM-DD)
    gender: Optional[str] = None  # Gender (M/F/U)
    subscriber_id: Optional[str] = None  # Subscriber's ID assigned by the payer
    def to_dict(self):
        """Convert the dataclass to a dictionary."""
        return asdict(self)


@dataclass
class Payer:
    name: str  # Payer (insurance company) name
    payer_id: str  # Payer ID
    address: Optional[str] = None  # Address of the payer
    contact_number: Optional[str] = None  # Payer's contact number
    
    def to_dict(self):
        """Convert the dataclass to a dictionary."""
        return asdict(self)
    
@dataclass
class RenderingProvider:
    name: str  # Name of the rendering provider
    npi: str  # National Provider Identifier
    specialty: Optional[str] = None  # Provider's specialty
    address: Optional[str] = None  # Address of the rendering provider
    def to_dict(self):
        """Convert the dataclass to a dictionary."""
        return asdict(self)
@dataclass
class ClaimData:
    """
        Represents a single claim with all its details in a nested structure. This is useful for generating JSON structures of the claim.
    """
    claim_id: str  # Unique Claim ID
    claim_date: Optional[str] = None

    patient_first_name: Optional[str] = None
    patient_last_name: Optional[str] = None
    patient_dob: Optional[str] = None  # Date of Birth (YYYY-MM-DD)
    patient_gender: Optional[str] = None  # Gender (M/F/U)
    
    # Subscriber Information
    subscriber: Optional[Subscriber] = None

    # Payer Information
    payer: Optional[Payer] = None

    # Rendering Provider Information
    rendering_provider: Optional[RenderingProvider] = None

    # Claim-Level Information
    claim_amount: float = 0.0  # Total claim amount
    diagnosis_codes: List[str] = field(default_factory=list)  # List of diagnosis codes (ICD)

    # Information used to track/trace the claim
    claim_source: Optional[str] = None
    trace_number: Optional[str] = None

    # Claim Lines
    claim_lines: List["ClaimLine"] = field(default_factory=list)  # List of line items
   
    def to_dict(self):
        """Convert the dataclass to a dictionary."""
        return asdict(self)


@dataclass
class ClaimLine:
    """
        Represents a single line item in a claim
    """
    claim_id: str
    service_id: str  # Procedure/Service Code (e.g., CPT/HCPCS code)
    description: Optional[str] = None  # Description of the service
    amount: float = 0.0  # Charge amount for the line
    units: int = 1  # Number of units for the service
    modifier: Optional[str] = None  # Service modifier (if any)
    diagnosis_pointer: List[str] = field(default_factory=list)  # Links to diagnoses
    
    def to_dict(self):
        """Convert the dataclass to a dictionary."""
        return asdict(self)


@dataclass
class ClaimData_Flat:
    """
        Represents a single claim with all its details in a flat structure. This is used to generate a flat file or pandas dataframe.
        Claim Lines are in a seperate object list claimdata_lines.
    """
     # Unique Claim ID
    claim_id: str  # Unique Claim ID
    claim_date: Optional[str] = None
    subscriber_first_name: Optional[str]=None
    subscriber_last_name: Optional[str] = None
    subscriber_dob: Optional[str] = None
    subscriber_gender: Optional[str] = None
    subscriber_id: Optional[str]    = None
    
    # Payer Information
    payer_name: Optional[str] = None
    payer_id: Optional[str] = None
    
    # Rendering Provider Information
    provider_name: Optional[str] = None
    provider_npi: Optional[str] = None
    provider_specialty: Optional[str] = None
    provider_address: Optional[str] = None
    
    # Patient Information
    patient_first_name: Optional[str] = None
    patient_last_name: Optional[str] = None
    patient_dob: Optional[str] = None  # Date of Birth (YYYY-MM-DD)
    patient_gender: Optional[str] = None  # Gender (M/F/U)
    
    claim_amount: float = 0.0  # Total claim amount
    
    diagnosis_codes: List[str] = field(default_factory=list)  # List of diagnosis codes (ICD)

    # Information used to track/trace the claim
    claim_source: Optional[str] = None
    trace_number: Optional[str] = None

    def to_dict(self):
        """Convert the dataclass to a dictionary."""
        return asdict(self)







    