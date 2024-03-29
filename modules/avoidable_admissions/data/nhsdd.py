gender = {
    "url": "https://www.datadictionary.nhs.uk/data_elements/person_stated_gender_code.html",
    "mapping": {"X": "Not Known", "1": "Male", "2": "Female", "9": "Not Specified"},
}

ethnos = {
    "url": "https://www.datadictionary.nhs.uk/data_elements/ethnic_category.html",
    "mapping": {
        "A": "White - British",
        "B": "White - Irish",
        "C": "White - Any other White background",
        "D": "Mixed - White and Black Caribbean",
        "E": "Mixed - White and Black African",
        "F": "Mixed - White and Asian",
        "G": "Mixed - Any other mixed background",
        "H": "Asian or Asian British - Indian",
        "J": "Asian or Asian British - Pakistani",
        "K": "Asian or Asian British - Bangladeshi",
        "L": "Asian or Asian British - Any other Asian background",
        "M": "Black or Black British - Caribbean",
        "N": "Black or Black British - African",
        "P": "Black or Black British - Any other Black background",
        "R": "Other Ethnic Groups - Chinese",
        "S": "Other Ethnic Groups - Any other ethnic group",
        "Z": "Not stated",
        "99": "Not known",
    },
}

admisorc = {
    "url": "https://www.datadictionary.nhs.uk/data_elements/admission_source__hospital_provider_spell_.html",
    "mapping": {
        "19": "Usual place of residence unless listed below, for example, a private dwelling whether owner occupied or owned by Local Authority, housing association or other landlord. This includes wardened accommodation but not residential accommodation where health care is provided. It also includes PATIENTS  with no fixed abode.",
        "29": "Temporary place of residence when usually resident elsewhere (e.g. hotels, residential Educational Establishments)",
        "37": "Court",
        "40": "Penal establishment",
        "42": "Police Station / Police Custody Suite",
        "49": "NHS other Hospital Provider  - high security psychiatric accommodation in an NHS Hospital Provider (NHS Trust or NHS Foundation Trust)",
        "51": "NHS other Hospital Provider  - WARD  for general PATIENTS  or the younger physically disabled or Emergency Care Department",
        "52": "NHS other Hospital Provider  - WARD  for maternity PATIENTS  or Neonates",
        "53": "NHS other Hospital Provider  - WARD  for PATIENTS  who are mentally ill or have Learning Disabilities",
        "55": "Care Home With Nursing",
        "56": "Care Home Without Nursing",
        "66": "Local Authority  foster care",
        "79": "Babies born in or on the way to hospital",
        "87": "Independent Sector Healthcare Provider run hospital",
        "88": "Hospice",
        "98": "Not applicable",
        "99": "ADMISSION SOURCE not known",
    },
}

admimeth = {
    "url": "https://www.datadictionary.nhs.uk/data_elements/admission_method_code__hospital_provider_spell_.html",
    "mapping": {
        "11": "Elective Admission:Waiting list",
        "12": "Elective Admission: Booked",
        "13": "Elective Admission:Planned",
        "21": "Emergency Admission: Emergency Care Department  or dental casualty department of the Health Care Provider",
        "22": "Emergency Admission: GENERAL PRACTITIONER: after a request for immediate admission has been made direct to a Hospital Provider, i.e. not through a Bed bureau, by a GENERAL PRACTITIONER  or deputy",
        "23": "Emergency Admission: Bed bureau",
        "24": "Emergency Admission: Consultant Clinic, of this or another Health Care Provider",
        "25": "Emergency Admission: Admission via Mental Health Crisis Resolution Team",
        "2A": "Emergency Admission: Emergency Care Department  of another provider where the PATIENT had not been admitted",
        "2B": "Emergency Admission: Transfer of an admitted PATIENT  from another Hospital Provider  in an emergency",
        "2C": "Emergency Admission: Baby born at home as intended",
        "2D": "Emergency Admission: Other emergency admission",
        "28": "Emergency Admission: Other means, examples are:  - admitted from the Emergency Care Department  of another provider where they had not been admitted  - transfer of an admitted PATIENT  from another Hospital Provider  in an emergency  - baby born at home as intended",
        "31": "Maternity Admission: Admitted ante partum",
        "32": "Maternity Admission: Admitted post partum",
        "82": "Other Admission: The birth of a baby in this Health Care Provider",
        "83": "Other Admission: Baby born outside the Health Care Provider  except when born at home as intended",
        "81": "Other Admission: Transfer of any admitted PATIENT  from other Hospital Provider  other than in an emergency",
        "98": "Not applicable",
        "99": "ADMISSION METHOD not known",
    },
}

disdest = {
    "url": "https://www.datadictionary.nhs.uk/data_elements/discharge_destination_code__hospital_provider_spell_.html",
    "mapping": {
        "19": "Usual place of residence unless listed below, for example, a private dwelling whether owner occupied or owned by Local Authority, housing association or other landlord. This includes wardened accommodation but not residential accommodation where health care is provided. It also includes PATIENTS  with no fixed abode.",
        "29": "Temporary place of residence when usually resident elsewhere (includes hotel, residential Educational Establishment)",
        "30": "Repatriation from high security psychiatric accommodation in an NHS Hospital Provider  (NHS Trust or NHS Foundation Trust)",
        "37": "Court",
        "38": "Penal establishment or police station",
        "48": "High Security Psychiatric Hospital, Scotland",
        "49": "NHS other Hospital Provider  - high security psychiatric accommodation",
        "50": "NHS other Hospital Provider  - medium secure unit",
        "51": "NHS other Hospital Provider  - WARD  for general PATIENTS  or the younger physically disabled",
        "52": "NHS other Hospital Provider  - WARD  for maternity PATIENTS  or Neonates",
        "53": "NHS other Hospital Provider  - WARD  for PATIENTS  who are mentally ill or have Learning Disabilities",
        "54": "NHS run Care Home",
        "65": "Local Authority  residential accommodation i.e. where care is provided",
        "66": "Local Authority  foster care",
        "79": "Not applicable - PATIENT  died or stillbirth",
        "84": "Non-NHS run hospital - medium secure unit",
        "85": "Non-NHS (other than Local Authority) run Care Home",
        "87": "Non-NHS run hospital",
        "88": "Non-NHS (other than Local Authority) run Hospice",
        "98": "Not applicable - Hospital Provider Spell  not finished at episode end (i.e. not discharged) or current episode unfinished",
        "99": "Not known",
    },
}

dismeth = {
    "url": "https://www.datadictionary.nhs.uk/data_elements/discharge_method_code__hospital_provider_spell_.html",
    "mapping": {
        "1": "PATIENT  discharged on clinical advice or with clinical consent",
        "2": "PATIENT  discharged him/herself or was discharged by a relative or advocate",
        "3": "PATIENT  discharged by mental health review tribunal, Home Secretary or Court",
        "4": "PATIENT  died",
        "5": "Stillbirth",
        "8": "Not applicable (Hospital Provider Spell not finished at episode end (i.e. not discharged) or current episode unfinished)",
        "9": "DISCHARGE METHOD not known",
    },
}

edattendcat = {
    "url": "https://www.datadictionary.nhs.uk/data_elements/emergency_care_attendance_category.html",
    "mapping": {
        "1": "Unplanned First Emergency Care Attendance  for a new clinical condition (or deterioration of a chronic condition).",
        "2": "Unplanned Follow-up Emergency Care Attendance  for the same or a related clinical condition and within 7 days ofthe First Emergency Care Attendance at THIS  Emergency Care Department",
        "3": "Unplanned Follow-up Emergency Care Attendance  for the same or a related clinical condition and within 7 days ofthe First Emergency Care Attendance at ANOTHER  Emergency Care Department",
        "4": "Planned Follow-up Emergency Care Attendance within 7 days of the First Emergency Care Attendance  at THIS  Emergency Care Department",
        "X": "Not Applicable (PATIENT dead on arrival in Emergency Care Department)",
    },
}

eddepttype = {
    "url": "https://www.datadictionary.nhs.uk/data_elements/emergency_care_department_type.html",
    "mapping": {
        "1": "Emergency departments are a CONSULTANT  led 24 hour service with full resuscitation facilities and designated accommodation for the reception of emergency care PATIENTS",
        "2": "CONSULTANT  led mono specialtyemergency careservice (e.g. ophthalmology, dental) with designated accommodation for the reception of PATIENTS",
        "3": "Other type of A&E/minor injury ACTIVITY  with designated accommodation for the reception of emergency care PATIENTS. The department may be doctor led, GENERAL PRACTITIONER ledor NURSE  led and treats at least minor injuries and illnesses and can be routinely accessed without APPOINTMENT. A SERVICE  mainly or entirely APPOINTMENT  based (for example a GP Practice  or Out-Patient Clinic) is excluded even though it may treat a number of PATIENTS  with minor illness or injury. Includes Urgent Treatment Centres.Excludes NHS walk-in centres",
        "4": "NHS walk in centres",
        "5": "Ambulatory Emergency Care Service. Note this is only  valid for piloting purposes in the CDS V6-2-2 Type 011 - Emergency Care Commissioning Data Set/ CDS V6-2-3 Type 011 - Emergency Care Commissioning Data Set and must not be submitted in the Patient Level Information Costing System Integrated Data Set - Emergency Care (Acute).",
    },
}
