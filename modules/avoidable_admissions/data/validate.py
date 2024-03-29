import warnings
from datetime import date, datetime
from typing import Tuple

import pandas as pd
import pandera as pa
from pandera.typing import Series

from avoidable_admissions.data import nhsdd
from avoidable_admissions.features import feature_maps


class AdmittedCareEpisodeSchema(pa.SchemaModel):
    """Rules for validating the Admitted Care Episodes Data before feature engineering.

    The dataset should be validated successfully against this schema before submitting to the
    rest of the pipeline.
    """

    # visit_id is not part of the data spec but is used here as a unique row identifier
    # Use `df["visit_id"] = df.reset_index(drop=True).index`

    visit_id: Series[int] = pa.Field(nullable=False, unique=True)

    # Ensure this has been pseudonymised appropriately.
    patient_id: Series[int] = pa.Field(nullable=False)

    gender: Series[str] = pa.Field(
        description=nhsdd.gender["url"],
        isin=list(feature_maps.gender),
        nullable=False,
    )

    ethnos: Series[str] = pa.Field(
        description=nhsdd.ethnos["url"],
        isin=list(feature_maps.ethnos),
        nullable=False,
    )

    procodet: Series[str] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/organisation_code__code_of_provider_.html",
        nullable=False,
    )

    sitetret: Series[str] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/site_code__of_treatment_.html",
        nullable=False,
    )

    townsend_score_decile: Series[int] = pa.Field(
        description="https://statistics.ukdataservice.ac.uk/dataset/2011-uk-townsend-deprivation-scores",
        ge=0,  # fill missing values with 0 to pass validation.
        le=10,
        nullable=True,
    )

    admimeth: Series[str] = pa.Field(
        description=nhsdd.admimeth["url"],
        isin=list(nhsdd.admimeth["mapping"].keys()),
        nullable=True,
    )

    admisorc: Series[str] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/admission_source__hospital_provider_spell_.html",
        isin=list(feature_maps.admisorc),
        nullable=True,
    )

    admidate: Series[date] = pa.Field(
        ge=date(year=2021, month=10, day=1),
        le=date(year=2022, month=9, day=30),
        nullable=False,
    )

    admitime: Series[str] = pa.Field(
        nullable=True, str_matches="2[0-3]|[01]?[0-9]:[0-5][0-9]", coerce=True
    )

    disdest: Series[str] = pa.Field(
        description=nhsdd.disdest["url"],
        isin=list(feature_maps.disdest),
        nullable=True,
    )

    dismeth: Series[str] = pa.Field(
        description=nhsdd.dismeth["url"],
        isin=list(feature_maps.dismeth),
        nullable=True,
    )

    length_of_stay: Series[float] = pa.Field(nullable=True, ge=0)

    epiorder: Series[int] = pa.Field(nullable=True, ge=0)

    admiage: Series[float] = pa.Field(
        ge=18,
        le=130,
        nullable=True,
    )

    class Config:
        coerce = True


AdmittedCareEpisodeSchema = AdmittedCareEpisodeSchema.to_schema().add_columns(
    {
        "diag_[0-9]{2}": pa.Column(
            str,
            nullable=True,
            regex=True,
        ),
        "opertn_[0-9]{2}": pa.Column(
            str,
            nullable=True,
            regex=True,
        ),
        "opdate_[0-9]{2}": pa.Column(
            datetime,
            nullable=True,
            regex=True,
        ),
    }
)


# Schema for validating Admitted Care Data Set after feature engineering
AdmittedCareFeatureSchema: pa.DataFrameSchema = AdmittedCareEpisodeSchema.add_columns(
    {
        "admiage_cat": pa.Column(
            str, nullable=False, checks=[pa.Check.isin(feature_maps.age_labels)]
        ),
        "gender_cat": pa.Column(
            str, nullable=False, checks=pa.Check.isin(set(feature_maps.gender.values()))
        ),
        "ethnos_cat": pa.Column(
            str,
            nullable=True,
            checks=[pa.Check.isin(set(feature_maps.ethnos.values()))],
        ),
        "townsend_score_quintile": pa.Column(
            nullable=True, checks=[pa.Check.in_range(min_value=1, max_value=5)]
        ),
        "admisorc_cat": pa.Column(
            nullable=True, checks=[pa.Check.isin(set(feature_maps.admisorc.values()))]
        ),
        "admidayofweek": pa.Column(
            nullable=True,
            checks=[
                pa.Check.isin(
                    [
                        "Monday",
                        "Tuesday",
                        "Wednesday",
                        "Thursday",
                        "Friday",
                        "Saturday",
                        "Sunday",
                    ]
                )
            ],
        ),
        "diag_seasonal_cat": pa.Column(
            nullable=True,
            checks=[
                pa.Check.isin(
                    [
                        "Respiratory infection",
                        "Chronic disease exacerbation",
                    ]
                )
            ],
        ),
        "length_of_stay_cat": pa.Column(
            nullable=True, checks=[pa.Check.isin(["<2 days", ">=2 days"])]
        ),
        "disdest_cat": pa.Column(
            nullable=True, checks=[pa.Check.isin(set(feature_maps.disdest.values()))]
        ),
        "dismeth_cat": pa.Column(
            nullable=True, checks=[pa.Check.isin(set(feature_maps.dismeth.values()))]
        ),
        "diag_01_acsc": pa.Column(
            nullable=True,
            checks=[pa.Check.isin(set(feature_maps.load_apc_acsc_mapping().values()))],
        ),
        "opertn_count": pa.Column(int, nullable=False, checks=pa.Check.ge(0)),
    }
)


class EmergencyCareEpisodeSchema(pa.SchemaModel):

    visit_id: Series[int] = pa.Field(nullable=False)

    patient_id: Series[int] = pa.Field(nullable=False)

    gender: Series[str] = pa.Field(
        description=nhsdd.gender["url"],
        isin=list(nhsdd.gender["mapping"].keys()),
        nullable=False,
    )

    ethnos: Series[str] = pa.Field(
        description=nhsdd.ethnos["url"],
        isin=list(nhsdd.ethnos["mapping"].keys()),
        nullable=False,
    )

    townsend_score_decile: Series[int] = pa.Field(
        description="https://statistics.ukdataservice.ac.uk/dataset/2011-uk-townsend-deprivation-scores",
        ge=0,  # fill missing values with 0 to pass validation.
        le=10,
        nullable=True,
    )

    accommodationstatus: Series[int] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/accommodation_status__snomed_ct_.html",
        nullable=True,
    )

    procodet: Series[str] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/organisation_code__code_of_provider_.html",
        nullable=False,
    )

    edsitecode: Series[str] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/organisation_site_identifier__of_treatment_.html",
        nullable=False,
    )

    eddepttype: Series[str] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_department_type.html",
        isin=list(nhsdd.eddepttype["mapping"].keys()),
        nullable=False,
    )

    edarrivalmode: Series[int] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_arrival_mode__snomed_ct_.html",
        nullable=False,
    )

    edattendcat: Series[str] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_attendance_category.html",
        isin=list(nhsdd.edattendcat["mapping"].keys()),
        nullable=True,
    )
    edattendsource: Series[int] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_attendance_source__snomed_ct_.html",
        nullable=True,
    )
    edarrivaldatetime: Series[datetime] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_arrival_date.html",
        ge=datetime(year=2021, month=10, day=1),
        le=datetime(year=2022, month=9, day=30),
        nullable=True,
    )
    activage: Series[int] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/age_at_cds_activity_date.html",
        ge=18,
        le=130,
        nullable=True,
    )
    edacuity: Series[int] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_acuity__snomed_ct_.html",
        nullable=True,
    )
    edchiefcomplaint: Series[int] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_chief_complaint__snomed_ct_.html",
        nullable=True,
    )

    timeined: Series[str] = pa.Field(
        description="Derived from Departure Date and Departure Time",
        nullable=True,
    )
    edattenddispatch: Series[int] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_discharge_destination__snomed_ct_.html",
        nullable=True,
    )
    edrefservice: Series[int] = pa.Field(
        description="https://www.datadictionary.nhs.uk/data_elements/referred_to_service__snomed_ct_.html",
        nullable=True,
    )

    class Config:
        coerce = True


EmergencyCareEpisodeSchema = EmergencyCareEpisodeSchema.to_schema().add_columns(
    {
        "edcomorb_[0-9]{2}": pa.Column(
            description="https://www.datadictionary.nhs.uk/data_elements/comorbidity__snomed_ct_.html",
            dtype=int,
            nullable=True,
            regex=True,
        ),
        "eddiag_[0-9]{2}": pa.Column(
            description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_diagnosis__snomed_ct_.html",
            dtype=int,
            nullable=True,
            regex=True,
        ),
        "edentryseq_[0-9]{2}": pa.Column(
            description="https://www.datadictionary.nhs.uk/data_elements/coded_clinical_entry_sequence_number.html",
            dtype=int,
            nullable=True,
            regex=True,
        ),
        "eddiag_[0-9]{2}": pa.Column(
            description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_diagnosis_qualifier__snomed_ct_.html",
            dtype=int,
            nullable=True,
            regex=True,
        ),
        "edinvest_[0-9]{2}": pa.Column(
            description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_clinical_investigation__snomed_ct_.html",
            dtype=int,
            nullable=True,
            regex=True,
        ),
        "edtreat_[0-9]{2}": pa.Column(
            description="https://www.datadictionary.nhs.uk/data_elements/emergency_care_procedure__snomed_ct_.html",
            dtype=int,
            nullable=True,
            regex=True,
        ),
    }
)


# Schema for validating Emergency Care Data Set after feature engineering
EmergencyCareFeatureSchema: pa.DataFrameSchema = EmergencyCareEpisodeSchema.add_columns(
    {
        "activage_cat": pa.Column(),
        "gender_cat": pa.Column(),
        "ethnos_cat": pa.Column(),
        "townsend_score_quintile": pa.Column(),
        "accommodationstatus_cat": pa.Column(),
        "edarrivalmode_cat": pa.Column(),
        "edattendsource_cat": pa.Column(),
        "edacuity_cat": pa.Column(),
        "edinvest_[0-9]{2}_cat": pa.Column(
            regex=True,
        ),
        "edtreat_[0-9]{2}_cat": pa.Column(
            regex=True,
        ),
        "eddiag_seasonal_cat": pa.Column(),
        "edattenddispatch_cat": pa.Column(),
        "edrefservice_cat": pa.Column(),
    }
)


def _validate_dataframe(
    df: pd.DataFrame, schema: pa.SchemaModel
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df_errors = pd.DataFrame()

    # todo: document this behaviour to warn user that index will be dropped.
    # alternatively find a way to set a unique key for each row - important for merging errors
    df = df.copy().reset_index(drop=True)

    try:
        # Capture all errors
        # https://pandera.readthedocs.io/en/stable/lazy_validation.html
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            schema.validate(df, lazy=True)
    except pa.errors.SchemaErrors as ex:

        print(ex.args[0])

        df_errors = ex.failure_cases.copy()

        # First get the rows that are causing errors
        df_errors["index"] = df_errors["index"].fillna(df.index.max() + 1)
        df_errors = df.merge(df_errors, how="right", left_index=True, right_on="index")
        df_errors["index"] = df_errors["index"].replace(df.index.max() + 1, None)

        # Column name mismatches will have an 'index' of NaN which causes merge to fail
        # If a column name is not present, then all rows should be returned as errors

        if df_errors["index"].hasnans:  # this
            # there is a column error. drop all rows from the 'good' dataframe
            df = df.iloc[0:0]

            print("No data will pass validation due to column error. See output above.")

        else:
            df = df[~df.index.isin(df_errors["index"])]

    finally:
        return df, df_errors


def validate_admitted_care_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return _validate_dataframe(df, AdmittedCareEpisodeSchema)


def validate_emergency_care_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return _validate_dataframe(df, EmergencyCareEpisodeSchema)


def validate_admitted_care_features(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return _validate_dataframe(df, AdmittedCareFeatureSchema)


def validate_emergency_care_features(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return _validate_dataframe(df, EmergencyCareFeatureSchema)
