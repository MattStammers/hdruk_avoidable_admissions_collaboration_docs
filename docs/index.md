# Welcome to the HDRUK Avoidable Admissions Collaboration Docs

This is a collection of the docs for the project and code snippets to help us all collaborate and share tools. 

## Site Main Sections

* `index`          - This navigation page
* `documentation`  - Documentation for the project which can be published open source to encourage sharing
* `data_models`    - Contains the Details of the Data Models for the project
* `code`           - Share repository for code snippets and explanation of how various parts of the code work
* `guides`         - Guides for how to set things up for the project

### Aim

To understand variation across the country in acute hospital admissions and explore methods for identifying an avoidable acute admission

### Objectives

1.       Take a multi-regional approach to linking routine data to describe patterns of acute admission and regional variation in admissions over a defined period of time
2.       Analyse admission variation by factors including deprivation (measured by LSOA), time of day, day of week, waiting times
3.       Describe outcomes following acute admission including Length of stay, repeat hospital attendance or admission within 7 days of index attendance, death in hospital.
4.       Where possible explore linkage with primary care data to identify patients with long term conditions who have an avoidable admission
5.       Develop methods for identifying patients at high risk of an avoidable admission using 

The criteria for those at high risk of avoidable admission are considered to be:

* 36 ambulatory care sensitive conditions[^1]. Alternatively this resource can be accessed in the [Directory of Ambulatory
Emergency Care for Adults](https://www.ambulatoryemergencycare.org.uk/uploads/files/1/AEC-Directory%206th%20edition%20February%202018.pdf)
* Length of stay in hospital
* Where possible, investigation and treatment received

### Population of Interest

* Time period: 01/08/21 to 31/08/22, all patients attending the ED during the defined period of time.

## Analysis Plan

- Describe acute admissions by demographics inc deprivation, type, time of day, day of week
Describe outcomes - length of stay, death in hospital, attendance at ED and re admission within 7 and 30 days
- Establish the admission pattern using the ACSC codes
- Where possible identify what investigations and treatments were administered in hospital - consider whether hospital admission was necessary for these
- Where possible link to primary care records TBC and discussed added value
- Model which factors have a higher likelihood of avoidable admission - possible algorithm development for a predictive tool

### Reporting and Outputs
Outputs will be in many formats including:
1. peer reviewed publication, 
2. using social media e.g. blog posts, 
3. conference presentations and through workshops. 4. In addition, we anticipate providing bespoke reports for each region that reflects their acute admissions profile.


## Reference Website layout

    mkdocs.yml               # The configuration file.
    docs/
        index.md             # The index page
        documentation.md     # An explanation of the project documentation
        data_models.md       # The data model specs for the project
        code.md              # Codeshares and docstrings
        guides.md            # Guides
    modules/
        {to be added}

[^1]: 
    Purdy S, Griffin T, Salisbury C, Sharp D. Ambulatory care sensitive conditions: terminology and disease coding need to be more specific to aid policy makers and clinicians. Public health. 2009 Feb 1;123(2):169-73. [DOI](https://doi.org/10.1016/j.puhe.2008.11.001)