
def format_name(raw_name: str) -> str:
    if not raw_name:
        return ""

    parts = raw_name.split("^")

    last = parts[0].title() if len(parts) > 0 else ""
    first = parts[1].title() if len(parts) > 1 else ""
    middle = parts[2].title() if len(parts) > 2 else ""

    if middle:
        return f"{first} {middle} {last}".strip()

    return f"{first} {last}".strip()

def format_address(raw: str) -> str:
    if not raw:
        return ""

    parts = raw.split("^")

    # safely extract with fallback ""
    street = parts[0].title() if len(parts) > 0 and parts[0] else ""
    unit   = parts[1].title() if len(parts) > 1 and parts[1] else ""
    city   = parts[2].title() if len(parts) > 2 and parts[2] else ""
    state  = parts[3].upper() if len(parts) > 3 and parts[3] else ""
    zip_code = parts[4] if len(parts) > 4 and parts[4] else ""

    # build line 1 (street + unit)
    line1 = " ".join([x for x in [street, unit] if x])

    # build line 2 (city, state zip)
    line2_parts = []

    if city:
        line2_parts.append(city)

    if state:
        if city:
            line2_parts.append(f", {state}")
        else:
            line2_parts.append(state)

    if zip_code:
        line2_parts.append(f" {zip_code}")

    line2 = "".join(line2_parts).strip()

    # combine final address
    if line1 and line2:
        return f"{line1} {line2}"
    elif line1:
        return line1
    elif line2:
        return line2
    else:
        return ""
    