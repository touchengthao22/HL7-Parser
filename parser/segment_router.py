
from parser.segments import msh, pid, pv1, obx

def route(segment, message):
    seg_type = segment.split("|")[0]

    if seg_type == "MSH":
        message.msh = msh.parse(segment)

    elif seg_type == "PID":
        message.pid = pid.parse(segment)

    elif seg_type == "PV1":
        message.pv1 = pv1.parse(segment)

    elif seg_type == "OBX":
        message.obx.append(obx.parse(segment))