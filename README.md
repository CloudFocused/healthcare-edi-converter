# Healthcare Edi Converter
A Python library that can be used to convert EDI file content strings into objects. 
Initially it supports just the EDI x12 837p (Claims submitted to payor requesting payment)



## Installation
```bash
pip install healthcare-edi-converter
```

## Basic Use
```py

pip install healthcare-edi-converter

```


## 837P File Overall Structure

The 837P consists of envelopes, headers, loops, and segments:

1. Interchange Control Header (ISA) -  The outermost wrapper for the EDI file. Contains metadata for sender/receiver identification, control numbers, date/time, and separators.

2. Functional Group Header (GS) - Groups related transaction sets together (e.g., all claims for one sender).
Identifies the sender, receiver, version, and date/time of the transaction group.

3. Transaction Set Header (ST) - Marks the beginning of an individual claim transaction. Contains the transaction set identifier and control numbers.

### Loops and Segments

#### Loop 1000: Submitter and Receiver Information Identifies the sender (submitter) and the recipient (receiver) of the claim.

1000A – Submitter Name
NM1: Submitter's name and ID.
PER: Submitter's contact information.

1000B – Receiver Name
NM1: Receiver's name and ID.

#### Loop 2000: Billing/Subscriber/Patient Information
This loop contains hierarchical levels (HL) to organize the billing provider, subscriber, and patient data.

2000A: Billing Provider
HL: Hierarchical structure (billing provider).
PRV: Billing provider taxonomy (e.g., specialty).
NM1: Billing provider’s name and ID.

2000B: Subscriber
HL: Hierarchical structure (subscriber).
SBR: Subscriber relationship to the insured (e.g., self, spouse).
NM1: Subscriber’s name and ID.
DMG: Subscriber’s demographic information (e.g., date of birth, gender).

2000C: Patient (if different from the subscriber)
HL: Hierarchical structure (patient).
PAT: Patient relationship to subscriber (e.g., child).
NM1: Patient’s name.

#### Loop 2300: Claim Information
Details about the specific claim being submitted.

CLM: Claim information (e.g., amount, claim number).
DTP: Date(s) of service or admission.
HI: Diagnosis codes (e.g., ICD-10 codes).
CN1: Contract information (if applicable).

#### Loop 2400: Service Line Information
Details about individual services provided.

SV1: Service line details (e.g., CPT code, service amount).
DTP: Service line dates.
REF: Reference IDs (e.g., prior authorization number).

#### Loop 2420: Service Provider Information
Identifies additional providers involved in the claim.

NM1: Referring provider, rendering provider, or supervising provider.
PRV: Provider taxonomy (e.g., specialty).
REF: Provider identification numbers.

#### Control Segments
1. Transaction Set Trailer (SE) Indicates the end of a transaction set. Contains a count of all segments in the transaction.
2. Functional Group Trailer (GE) Indicates the end of a functional group. Includes control numbers.
3. Interchange Control Trailer (IEA) Indicates the end of the interchange envelope. Includes the total number of functional groups and control numbers.