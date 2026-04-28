# parser/message_parser.py

from parser.segment_router import route
from models.message import HL7Message

def parse_message(text):
    message = HL7Message()

    segments = text.splitlines()

    for seg in segments:
        if seg.strip():
            route(seg, message)

    return message