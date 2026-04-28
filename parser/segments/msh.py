# parser/segments/msh.py

def parse(segment: str) -> dict:
    fields = segment.split(segment[3])
    print(fields)

    return {
        "field_separator": segment[3],
        "encoding_characters": fields[1] if len(fields) > 1 else None,
        "sending_application": fields[2] if len(fields) > 2 else None,
        "sending_facility": fields[3] if len(fields) > 3 else None,
        "receiving_application": fields[4] if len(fields) > 4 else None,
        "receiving_facility": fields[5] if len(fields) > 5 else None,
        "datetime": fields[6] if len(fields) > 6 else None,
        "message_type": fields[7] if len(fields) > 7 else None,
        "message_control_id": fields[8] if len(fields) > 8 else None,
        "processing_id": fields[9] if len(fields) > 9 else None,
        "version": fields[11] if len(fields) > 11 else None
    }


print(parse('MSH|^~\&|HOSPITAL|LAB|APP|APPFAC|202604271200||ADT^A01|12345|P|2.3'))