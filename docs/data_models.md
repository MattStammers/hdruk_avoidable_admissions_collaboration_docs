## Data Models

This area contains the key documentation pertaining to the desired data models for the project. There are now two different datasets as part of the spec:

1. Admitted Patient Care
2. Emergency Care

### Admitted Patient Care Spec

#### Overview
Patient records for all acute emergency admissions for adults (18 years + on day of admission) that had an admission date within the specified study period (see above).

Please check the coding of the variables against those linked to in the ‘Coding/Classification system’ column, this is to ensure data (and therefore analysis) standardisation across sites.

#### Required variables for analyses

|Variable name|Description|Reasoning / Filtering (see Coding / Classification system)|Format / Coding / Classification system|
|:----|:----|:----|:----|
|patient_id|Pseudo individual patient identifier|To be able to identify different/the same patient across the dataset, and to identify re-admissions. Likely derived from NHS Number / CHI.|
|No filtering|A unique identifier for each individual patient across the dataset|
|procodet|NHS Digital ODS code defining the organisation providing treatment.|To be able to identify the trust of the admission|[NHS Data Model ORGANISATION CODE (CODE OF PROVIDER)](https://www.datadictionary.nhs.uk/data_elements/organisation_code__code_of_provider_.html)|
|sitetret|NHS Digital ODS code defining the site on which the patient was treated within an organisation. Contains the first 3 digits of the provider code of treatment (procodet) with the last two digits being the site identifier.|To be able to identify the site of the admission|[NHS Data Model SITE CODE (OF TREATMENT)](https://www.datadictionary.nhs.uk/data_elements/site_code__of_treatment_.html)|
|townsend_score_decile|Deprivation measure that covers both England and Scotland. To be derived from patient postcode|To report on patient demographics.|
|No filtering|(https://statistics.ukdataservice.ac.uk/dataset/2011-uk-townsend-deprivation-scores)|
|[Derived from NHS Data Model POSTCODE OF USUAL ADDRESS](https://www.datadictionary.nhs.uk/data_elements/postcode_of_usual_address.html)|
|gender|Defines the sex of the patient|To report on patient demographics.|
|No filtering|[NHS Data Model PERSON GENDER CODE](https://www.datadictionary.nhs.uk/data_elements/person_gender_code_current.html)|
|ethnos|The ethnicity of the patient, as specified by the patient. Groups as defined in the 2001 census.|To report on patient demographics.|
|No filtering|[NHS Data Model ETHNIC CATEGORY](https://www.datadictionary.nhs.uk/data_elements/ethnic_category.html)|
|admimeth|Identifies how the patient was admitted to hospital|Used to select only acute (emergency) admissions.|
|admimeth in (21, 22,  23,  24,  25,  2A,  2B,  2C,  2D,  28)|[NHS Data Model ADMISSION METHOD CODE (HOSPITAL PROVIDER SPELL)](https://www.datadictionary.nhs.uk/data_elements/admission_method_code__hospital_provider_spell_.html)|
|admisorc|Identifies where the patient was immediately prior to admission|Used to identify possible care home admissions.|
|No filtering|[NHS Data Model SOURCE OF ADMISSION CODE (HOSPITAL PROVIDER SPELL)](https://www.datadictionary.nhs.uk/data_elements/admission_method_code__hospital_provider_spell_.html)|
|admidate|The date the patient was admitted to hospital at the start of a hospital spell. |Start date of hospital spell, to limit the time period of interest.|
|admidate on or after 2021-10-01 and also|
|on or before 2022-09-30|[NHS Data Model START DATE (HOSPITAL PROVIDER SPELL)](https://www.datadictionary.nhs.uk/data_elements/source_of_admission_code__hospital_provider_spell_.html)|
|admitime|The time the patient was admitted to hospital at the start of a hospital spell. hh:mm:ss format|Start time of hospital spell.|
|No filtering|[NHS Data Model START TIME (HOSPITAL PROVIDER SPELL)](https://www.datadictionary.nhs.uk/data_elements/start_date__hospital_provider_spell_.html)|
|disdest|Identifies where the patient was due to go on leaving hospital|Can be used to identify discharge to care homes.|
|No filtering|[NHS Data Model DISCHARGE DESTINATION CODE (HOSPITAL PROVIDER SPELL](https://www.datadictionary.nhs.uk/data_elements/discharge_destination_code__hospital_provider_spell_.html)|
|dismeth|Indicates the circumstances under which a patient left hospital|Used to identify deaths.|
|No filtering|[NHS Data Model DISCHARGE METHOD CODE (HOSPITAL PROVIDER SPELL)](https://www.datadictionary.nhs.uk/data_elements/discharge_date__hospital_provider_spell_.html)|
|length_of_stay|The length of stay of the patient admission. Calculated as the time between a patient's spell start date and spell end date.|No filtering|Derived from|
|[NHS Data Model START DATE (HOSPITAL PROVIDER SPELL)(https://www.datadictionary.nhs.uk/data_elements/start_date__hospital_provider_spell_.html)|
|and|
|[NHS Data Model DISCHARGE DATE (HOSPITAL PROVIDER SPELL)](https://www.datadictionary.nhs.uk/data_elements/discharge_date__hospital_provider_spell_.html)|
|epiorder|The order of the episode within the current hospital provider spell. 1 indicates the first episode in the hospital provider spell, 2 the second, etc.|We wish diagnosis and procedure data from only the first episode of a spell (epiorder = 1). |[NHS Data Model EPISODE NUMBER](https://www.datadictionary.nhs.uk/data_elements/episode_number.html)|
|admiage|Age on admission|To report on patient demographics and to limit to desired cohort.|
|admiage equals or is greater than 18 years old|[NHS Data Model AGE ON ADMISSION](https://www.datadictionary.nhs.uk/data_elements/age_on_admission.html)|
|diag_01|The primary diagnosis code recorded for the episode. The classification system in use is ICD-10.|Used to identify ambulatory care sensitive conditions. See epiorder.|
|No filtering|[NHS Data Model PRIMARY DIAGNOSIS (ICD)](https://www.datadictionary.nhs.uk/data_elements/primary_diagnosis__icd_.html)|
|Code required to be in contemporary ICD-10 coding standard.|
|diag_NN|The secondary diagnosis codes recorded for the episode. The classification system in use is ICD-10.|Used to identify ambulatory care sensitive conditions.  See epiorder.|
|May include up to 19 secondary diagnosis fields, from 02-20.|[NHS Data Model SECONDARY DIAGNOSIS (ICD)](https://www.datadictionary.nhs.uk/data_elements/secondary_diagnosis__icd_.html)|
|Code required to be in contemporary ICD-10 coding standard.|
|opertn_01|The main operative procedure code recorded for the episode. The classification system in use is OPCS-4.| See epiorder. No filtering|[NHS Data Model PRIMARY PROCEDURE (OPCS)](https://www.datadictionary.nhs.uk/data_elements/primary_procedure__opcs_.html)|
|Codes required to be in contemporary OPCS-4 coding standard|
|opdate_01|The date the primary operative procedure took place.| See epiorder. No filtering|[NHS Data Model PROCEDURE DATE](https://www.datadictionary.nhs.uk/data_elements/procedure_date.html)|
|opertn_NN|Secondary procedure code| See epiorder. No filtering|
|May include up to 23 secondary procedure fields, from 02-24.|[NHS Data Model PROCEDURE (OPCS)](https://www.datadictionary.nhs.uk/data_elements/procedure__opcs_.html)|
|Codes required to be in contemporary OPCS-4 coding standard|
|opdate_NN|Secondary procedure date| See epiorder. No filtering|[NHS Data Model PROCEDURE DATE](https://www.datadictionary.nhs.uk/data_elements/procedure_date.html)|


Note: We are aware that the CDS allows for unlimited secondary diagnoses and procedures to be recorded. The first recorded 19 such secondary diagnoses and first 23 such secondary procedures are sufficient for our purposes.

### Emergency Care

#### Overview
Patient records for all emergency care attendances for adults (18 years + on day of admission) that had an admission date within the specified study period (see above).

Please check the coding of the variables against those linked to in the ‘Coding/Classification system’ column, this is to ensure data (and therefore analysis) standardisation across sites.

#### Required variables for analyses

|Variable name|Description|Reasoning / Filtering (see Coding / Classification system)|Format / Coding / Classification system|
|:----|:----|:----|:----|
|patient_id|Pseudo individual patient identifier|To be able to identify different/the same patient across the dataset, and to identify re-admissions. Likely derived from NHS Number / CHI.|
|No filtering|A unique identifier for each individual patient across the dataset|
|townsend_score_decile|Deprivation measure that covers both England and Scotland. To be derived from patient postcode|To report on patient demographics.|
|No filtering|(https://statistics.ukdataservice.ac.uk/dataset/2011-uk-townsend-deprivation-scores)|
|Derived from [NHS Data Model POSTCODE OF USUAL ADDRESS](https://www.datadictionary.nhs.uk/data_elements/postcode_of_usual_address.html)|
|gender|Defines the sex of the patient|To report on patient demographics.|
|No filtering|[NHS Data Model PERSON STATED GENDER CODE](https://www.datadictionary.nhs.uk/data_elements/person_stated_gender_code.html)|
|ethnos|The ethnicity of the patient, as specified by the patient. Groups as defined in the 2001 census.|To report on patient demographics.|
|No filtering|[NHS Data Model ETHNIC CATEGORY](https://www.datadictionary.nhs.uk/data_elements/ethnic_category.html)|
|AccommodationStatus_SnomedCt|Accommodation Status.|
|SNOMED code|Can be used to identify patient who live in residential or nursing homes|
|No filtering|[NHS Data Model ACCOMMODATION STATUS (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/accommodation_status__snomed_ct_.html)|
|procodet|NHS Digital ODS code defining the organisation providing treatment.|To be able to identify the trust of the admission|[NHS Data Model ORGANISATION IDENTIFIER (CODE OF PROVIDER)](https://www.datadictionary.nhs.uk/data_elements/organisation_identifier__code_of_provider_.html)|
|edsitecode|Site code for each Type 1 Emergency Department at the Trust. To be derived from Organisation Site Identifier of Treatment and to include the first 3 digits of the provider code of treatment (procodet)|To be able to identify the site of the admission|[Derived from NHS Data Model ORGANISATION SITE IDENTIFIER (OF TREATMENT)](https://www.datadictionary.nhs.uk/data_elements/organisation_site_identifier__of_treatment_.html)|
|eddepttype|The type of Emergency Department|Used to select attendances at type 1 EDs.|
|(eddepttype = 01)|[NHS Data Model EMERGENCY CARE DEPARTMENT TYPE](https://www.datadictionary.nhs.uk/data_elements/emergency_care_department_type.html)|
|edarrivalmode|Transport mode by which the patient arrived at the Emergency Department.|
|SNOMED code.|Used to identify arrival by ambulance, etc|
|No filtering|[NHS Data Model EMERGENCY CARE ARRIVAL MODE (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_arrival_mode__snomed_ct_.html)|
|edattendcat|The category of emergency care attendance|Used to identify unplanned first emergency care attendance for a new clinical condition (or deterioration of a chronic condition).|
|(edattendcat = 1)|[NHS Data Model EMERGENCY CARE ATTENDANCE CATEGORY](https://www.datadictionary.nhs.uk/data_elements/emergency_care_attendance_category.html)|
|edattendsource|The source of an Emergency Care Attendance|Used to identify the source of an attendance (e.g. via a GP)|
|No filtering|[NHS Data Model EMERGENCY CARE ATTENDANCE SOURCE (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_attendance_source__snomed_ct_.html)|
|edarrivaldatetime|Emergency Care Arrival DateTime|
|Format YYYY/MM/DD hh:mm:ss TMZ|Arrival datetime at the emergency department|
|EmergencyCareArrivalDate on or after 2021-10-01 00:00:00 and also|
|on or before 2022-1009-3101 00:00:00|
|Timezone will be required to derive time in ED correctly.|[Derived from NHS Data Model EMERGENCY CARE ARRIVAL DATE](https://www.datadictionary.nhs.uk/data_elements/emergency_care_arrival_date.html)|
|and|
|[NHS Data Model EMERGENCY CARE ARRIVAL TIME](https://www.datadictionary.nhs.uk/data_elements/emergency_care_arrival_time.html)|
|activage|
| |Age at time of activity|To report on patient demographics and to limit to desired cohort.|
|admiage equals or is greater than 18 years old|[NHS Data Model AGE AT CDS ACTIVITY DATE](https://www.datadictionary.nhs.uk/data_elements/age_at_cds_activity_date.html)|
|edacuity|Acuity of patient’s condition at time of initial assessment.|
|SNOMED code.|To report on patient demographics.|
|No filtering|[NHS Data Model EMERGENCY CARE ACUITY (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_acuity__snomed_ct_.html)|
|edcheifcomplaint|Chief complaint as assessed by the care professional first assessing the patient.|
|SNOMED code.|To report on patient demographics.|
|No filtering|[NHS Data Model EMERGENCY CARE CHIEF COMPLAINT (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_chief_complaint__snomed_ct_.html)|
|edcomorb_NN|Comorbidities identified for the patient.|
|SNOMED code.|Used to identify comorbid conditions|
|May include up to 10 fields, from 01-10|[NHS Data Model COMORBIDITY (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/comorbidity__snomed_ct_.html)|
|eddiag_NNEmergencyCareDiagnosis_SnomedCt|Diagnosis codes recorded for the attendance|Used to identify Ambulatory Care Sensitive Conditions|
|May include up to 12 fields, from 01-12|[NHS Data Model EMERGENCY CARE DIAGNOSIS (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_diagnosis__snomed_ct_.html)|
|edentryseq_NNCodedClinicalEntrySequenceNumber|Sequence number associated with the diagnosis, giving the position it was recorded by the clinician|Used to tie diagnosis to the position they were recorded.|
|May include up to 2 fields, from 01-12|[NHS Data Model CODED CLINICAL ENTRY SEQUENCE NUMBER](https://www.datadictionary.nhs.uk/data_elements/coded_clinical_entry_sequence_number.html)|
|eddiagqual_NNEmergencyCareDiagnosisQualifier_SnomedCt|Level of certainty of a patient diagnosis.|
|SNOMED code.|Used to identify the level of certainty of a diagnosis|
|May include up to 12 fields, from 01-12|[NHS Data Model EMERGENCY CARE DIAGNOSIS QUALIFIER (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_diagnosis_qualifier__snomed_ct_.html)|
|edinvest_NN|Clinical investigations performed while a patient is under the care of an Emergency Department.|
|SNOMED code.|Identify investigations|
|May include up to 12 fields, from 01-12|[NHS Data Model EMERGENCY CARE CLINICAL INVESTIGATION (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_clinical_investigation__snomed_ct_.html)|
|edtreat_NN|Treatments performed while the person is under the care of the emergency department.|
|SNOMED code.|Identify treatments/procedures|
|May include up to 12 fields, from 01-12|[NHS Data Model EMERGENCY CARE PROCEDURE (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_procedure__snomed_ct_.html)|
|timeined|The time a patient spent in ED (in minutes)|Used to report on time in ED|
|See edarrivaldatetime for filtering.|
|Also, timezone will need to be considered to correctly derive field around daylight saving transition (BST/GMT)|Derived from [NHS Data Model EMERGENCY CARE DEPARTURE DATE](https://www.datadictionary.nhs.uk/data_elements/emergency_care_departure_date.html)|
|and [NHS Data Model EMERGENCY CARE DEPARTURE TIME](https://www.datadictionary.nhs.uk/data_elements/emergency_care_departure_time.html)|
|and|
|edarrivaldatetime|
|edattenddispatch|Intended destination of patient following discharge from the emergency department.|
|SNOMED code.|Used to identify patients who are discharged, admitted, died, etc.|
|No filtering|[NHS Data Model EMERGENCY CARE DISCHARGE DESTINATION (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/emergency_care_discharge_destination__snomed_ct_.html)|
|edrefservice|Inpatient service to which the patient was referred for admission or opinion by treating clinician.|
|SNOMED code.|To describe where admitted patients are referred|
|No filtering|[NHS Data Model REFERRED TO SERVICE (SNOMED CT)](https://www.datadictionary.nhs.uk/data_elements/referred_to_service__snomed_ct_.html)|


Note: We are aware that the CDS allows for unlimited diagnoses, comorbidities, procedures, and treatments to be recorded. The first recorded 12 such diagnoses, procedures, and treatments,  and first 10 such comorbidities are sufficient for our purposes.