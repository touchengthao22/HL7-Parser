# parser/segments/pv1.py

def parse(segment: str) -> dict:
    fields = segment.split("|")

    return {
        "patient_class": fields[2] if len(fields) > 2 else None,   # inpatient/outpatient
        "assigned_location": fields[3] if len(fields) > 3 else None,
        "admission_type": fields[4] if len(fields) > 4 else None,
        "preadmit_number": fields[5] if len(fields) > 5 else None,
        "attending_doctor": fields[7] if len(fields) > 7 else None,
        "visit_number": fields[19] if len(fields) > 19 else None,
        "admit_datetime": fields[44] if len(fields) > 44 else None
    }