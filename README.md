# 📄 HL7 Parser (Python)

## Overview

This project is a Python-based HL7 v2 message parser designed to transform raw healthcare data into structured, readable, and analytics-ready formats.

HL7 messages are widely used in healthcare systems to transmit clinical and administrative data. This parser extracts key segments such as patient demographics, visit information, and lab results, and converts them into clean structured output for downstream use.

---

## Features

* Parses HL7 v2 messages from raw text files
* Supports core segments:

  * **MSH** (Message Header)
  * **PID** (Patient Information)
  * **PV1** (Visit Information)
  * **OBX** (Observation / Lab Results)
* Handles missing or incomplete HL7 fields safely
* Converts encoded values (e.g., names, dates, addresses) into human-readable formats
* Displays structured output using clean console formatting
* Designed for extensibility (easy to add new HL7 segments)

---

## Project Structure

```
hl7-parser/
│
├── main.py                  # Entry point / demo runner
├── parser/
│   ├── message_parser.py    # Orchestrates full HL7 parsing
│   ├── segment_router.py    # Routes segments to correct parser
│   ├── segments/
│   │   ├── msh.py
│   │   ├── pid.py
│   │   ├── pv1.py
│   │   ├── obx.py
│
├── utils/
│   ├── formatters.py        # Name, date, address formatting
│
├── messages/
│   ├── message.hl7          # Sample HL7 input file
│
└── README.md
```

---

## How It Works

1. **Read HL7 file**

   * Raw HL7 message is loaded from a `.hl7` text file

2. **Split into segments**

   * Each line is treated as a segment (MSH, PID, PV1, OBX, etc.)

3. **Route segments**

   * Each segment is sent to its respective parser

4. **Normalize data**

   * Encoded HL7 values (names, dates, etc.) are formatted into readable form

5. **Output structured data**

   * Parsed message is displayed in a clean, readable format

---
## Example Input
```
MSH|^~\&|HOSPITAL|LAB|APP|APPFAC|202604271200||ADT^A01|12345|P|2.3
PID|1||123456||DOE^JOHN||19800115|M|||123 MAIN ST^^SACRAMENTO^CA
PV1|1|I|WARD^101^A|EMERGENCY||||DR.SMITH|||||||||||VISIT123
OBX|1|NM|WBC||6.4|10^9/L|4.0-10.5|N|||F|||202604271100
OBX|2|NM|GLUCOSE||98|mg/dL|70-110|N|||F|||202604271100
```

## Example Output

```
=== PID - Patient Information ===
Patient ID: 123456
Name: John Doe
DOB: 01/15/1980
Sex: Male
Address: 123 Main St, Sacramento CA

=== PV1 - Visit Information ===
Patient Class: Inpatient
Assigned Location: WARD 101

=== OBX - Lab Results ===
WBC: 6.4 10^9/L (Normal)
Glucose: 98 mg/dL (Normal)
```

---

## Key Design Goals

* **Robustness:** Handles missing HL7 fields without crashing
* **Modularity:** Each segment is independently parsed
* **Scalability:** Easy to add new HL7 segments (e.g., OBR, ORC)
* **Readability:** Converts raw clinical encoding into human-readable format
* **Healthcare relevance:** Designed with real-world HL7 message structure in mind

---

## Skills Demonstrated

* Python data parsing & transformation
* Healthcare data (HL7 v2 standard)
* Data cleaning and normalization
* Modular software design
* Handling real-world messy data
* Basic clinical data engineering workflow

---

## Future Improvements

* Add support for additional HL7 segments (OBR, ORC, NK1)
* Store parsed data in SQLite or PostgreSQL
* Build API using FastAPI for HL7 ingestion
* Add validation rules for clinical data quality

---

## Example HL7 Input

```
MSH|^~\&|HOSPITAL|LAB|...
PID|1||123456||DOE^JOHN||19800115|M|...
PV1|1|I|WARD^101...
OBX|1|NM|WBC||6.4|...
```

---
