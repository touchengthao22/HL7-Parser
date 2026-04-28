# parser/segments/pid.py
from utils.formatters import format_name, format_address

def parse(segment):
    fields = segment.split("|")

    return {
        "patient_id": fields[3] if len(fields) > 3 else None,
        "name": format_name(fields[5] if len(fields) > 5 else ""),
        "dob": fields[7] if len(fields) > 7 else None,
        "sex": fields[8] if len(fields) > 8 else None,
        "address": format_address(fields[11] if len(fields) > 11 else "")
    }