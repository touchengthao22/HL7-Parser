# parser/segments/msh.py

def parse(segment: str) -> dict:
    fields = segment.split("|")

    return {
        "field_separator": fields[1] if len(fields) > 1 else None,
        "encoding_characters": fields[2] if len(fields) > 2 else None,
        "sending_application": fields[3] if len(fields) > 3 else None,
        "sending_facility": fields[4] if len(fields) > 4 else None,
        "receiving_application": fields[5] if len(fields) > 5 else None,
        "receiving_facility": fields[6] if len(fields) > 6 else None,
        "datetime": fields[7] if len(fields) > 7 else None,
        "message_type": fields[8] if len(fields) > 8 else None,
        "message_control_id": fields[9] if len(fields) > 9 else None,
        "processing_id": fields[10] if len(fields) > 10 else None,
        "version": fields[11] if len(fields) > 11 else None
    }