# HDRUK Avoidable Admissions Docs and Codeshare

Repository for sharing data models and information for the national HDRUK avoidable admissions project

This is the main repo. Feel free to create code development branches and submit pull requests to update the documentation. If this works and matures we can move it to the official HDRUK repository. 

## Pipeline
This code is used for obtaining the map between the ICD10 codes presented at both the protocol (Ambulatory care sensitive conditions: terminology and disease coding need to be more specific to aid policy makers and clinicians) and the suggested alternative document (Directory of AmbulatoryEmergency Care for Adults). It first queries the ConceptMap/translate endpoint for mapping the icd10 codes to snomed and then the ValueSet/expand endpoint for obtaining previous codes. 
For considering also possible codes associated with the source concepts, it queries the snomed browser too.
