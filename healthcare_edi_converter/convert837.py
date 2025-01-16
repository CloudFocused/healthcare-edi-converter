import json

class HealthClaimConverter:
    def __init__(self, edi_content: str):
        self.edi_content = edi_content

    def parse(self) -> dict:
        # This method will parse the EDI file and return a dictionary representation
        # For now, we'll just return a placeholder
        parsed_data = {
            "Claim": {
                "ClaimID": "12345",
                "Patient": {
                    "FirstName": "John",
                    "LastName": "Doe",
                },
                "Provider": {
                    "Name": "Sample Provider",
                    "NPI": "1234567890"
                },
                "ClaimLines": [
                    {"Service": "Consultation", "Amount": 100.00},
                    {"Service": "X-Ray", "Amount": 200.00},
                ]
            }
        }
        return parsed_data

    def to_json(self) -> str:
        return json.dumps(self.parse(), indent=4)