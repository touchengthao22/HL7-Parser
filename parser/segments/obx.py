# parser/segments/obx.py

def parse(segment: str) -> dict:
    fields = segment.split("|")

    return {
        "set_id": fields[1] if len(fields) > 1 else None,
        "value_type": fields[2] if len(fields) > 2 else None,
        "observation_identifier": fields[3] if len(fields) > 3 else None,
        "observation_sub_id": fields[4] if len(fields) > 4 else None,
        "observation_value": fields[5] if len(fields) > 5 else None,
        "units": fields[6] if len(fields) > 6 else None,
        "reference_range": fields[7] if len(fields) > 7 else None,
        "abnormal_flags": fields[8] if len(fields) > 8 else None,
        "result_status": fields[11] if len(fields) > 11 else None,
        "observation_datetime": fields[14] if len(fields) > 14 else None
    }