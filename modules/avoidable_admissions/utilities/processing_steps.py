from pandas import DataFrame, concat, Series
from urllib.request import urlopen
from json import loads, dumps
from params import credentials
from requests import request
from chardet import detect
from numpy import float64

def query_snomed(concept: str) -> DataFrame():

  """
  Function to scrape Snomed UK Browser and obtain relevant attributes associated to a concept. 
  
  Args: 
    concept: Medical concept that is searched at SnomedBrowser 

  Returns:
    A pandas Dataframe

  Example:
    df_1 = query_snomed("angina")

  """
  concept = str(concept).lower()
  concept_arr = concept.split(' ')
  concept = '%20'.join(concept_arr)

  url = 'https://termbrowser.nhs.uk/sct-browser-api/snomed/uk-edition/v20221123/descriptions?query=' + concept + '&limit=50&searchMode=partialMatching&lang=english&statusFilter=activeOnly&skipTo=0&returnLimit=50&normalize=true'
  url = url.encode('ascii', 'ignore').decode('ascii')
  response = urlopen(url)
  
  # storing the JSON response 
  # from url in data
  data_json = loads(response.read())

  # convert to df
  df = DataFrame(data_json["matches"])
  return (df)

def query_snomed_ICD10_mapping(concept_id: int) -> str:

  """
  Function to determine if a conceptId from SNOMED maps to a ICD10 diagnostic, and obtain the mapping code

  Args: 
    concept_id: conceptId Snomed Code

  Returns:
    A pandas Dataframe

  Example:
    df_1 = query_snomed_ICD10_mapping(194828000)
  

  """
  url = 'https://termbrowser.nhs.uk/sct-browser-api/snomed/uk-edition/v20221123map/complexmap/' + str(concept_id)
  response = urlopen(url)
  
  # storing the JSON response 
  # from url in data
  data_json = loads(response.read())

  # convert to df
  if(len(data_json)):
    if(data_json[0]["projectName"] == "ICD10"):
      return (data_json[0]["mapEntry"])
    else:
      return False

def split_array(df: DataFrame) -> DataFrame:
  """
  Function to format dataframe 

  Args: 
    df: DataFrame

  Returns:
    A pandas Dataframe

  Example:
    df_1 = split_array(df)
  """
  if(df.has_ICD10):
    aux = DataFrame(df.has_ICD10)
  else:
    aux = DataFrame([""]*10)
    aux = aux.T
  aux.columns = ["id","targetId","targetName","rule","mapPriority","mapRelation","mapGroup","ukTcMapBlock", "objectId", "mapAdvice"]
  aux["term"] = df.term
  aux["conceptId"] = df.conceptId
  aux["active"] = df.active
  aux["conceptActive"] = df.conceptActive
  aux["fsn"] = df.fsn
  aux["module"] = df.module
  aux["definitionStatus"] = df.definitionStatus
  aux["concept"] = df.concept

  return aux

aux = DataFrame()

def ts_req(row) -> Series:
    

    """
    Function to query nhs mapper API returning dataframe with icd10 code and  map to SNOMED

    Args: 
      row: row

    Returns:
      A pandas Dataframe

  """

    url = "https://ontology.nhs.uk/production1/fhir/ConceptMap/$translate?_format=json"
    description_code = row.source_description
    payload = dumps({
    "resourceType": "Parameters",
    "parameter": [
        {
        "name": "codeableConcept",
        "valueCodeableConcept": {
            "coding": [],
            "text": description_code
        }
        },
        {
        "name": "target",
        "valueUri": "http://snomed.info/sct?fhir_vs=isa/138875005"
        },
        {
        "name": "url",
        "valueUri": "http://ontoserver.csiro.au/fhir/ConceptMap/automapstrategy-default"
        }
    ]
    })
    headers = {
    'Content-Type': 'application/fhir+json',
    'Authorization': 'Bearer ' + credentials["bearer_token"]
    }

    response = request("POST", url, headers=headers, data=payload)
    concept = row.concept

    try:
        target_system = response.json()["parameter"][2]["part"][2]["valueCoding"]["system"]
        target_version = response.json()["parameter"][2]["part"][2]["valueCoding"]["version"]
        target_code = response.json()["parameter"][2]["part"][2]["valueCoding"]["code"]
        target_description = response.json()["parameter"][2]["part"][2]["valueCoding"]["display"]
        
    except:
        target_system = ""
        target_version = ""
        target_code = ""
        target_description = ""

    source_code = row.source_code
    return Series([target_system, target_version, target_code, target_description, concept,source_code,description_code], index=["target_system", "target_version", "target_code", "target_description", "concept","source_code", "source_description"])


def obtain_snomed_concepts(concepts: list, path: str) -> bool:
    aux = DataFrame()

    for concept in concepts:
        df_1 = query_snomed(concept)
        df_1["concept"] = concept
        aux = concat([aux,df_1], ignore_index=True)

    aux["has_ICD10"] = aux["conceptId"].apply(lambda x: query_snomed_ICD10_mapping(x))

    out_df = DataFrame()

    for i in range(len(aux)):
        aux_df = aux[(aux.index== i)]
        df_2 = aux_df.apply(lambda x: split_array(x), axis=1)
        out_df = concat([df_2[i],out_df], ignore_index=True)

    out_df = out_df.drop(["rule", "mapRelation","mapGroup", "ukTcMapBlock","objectId", "mapAdvice"], axis = 1)
    out_df = out_df.rename(columns = {"targetId":"source_code", "targetName":"source_description", "conceptId":"target_code","fsn":"target_description"})
    out_df.to_csv(path)

    return True


def obtain_ECDS_snomed_members(path: str) -> DataFrame:

  """
  Function to obtain .csv file with  Emergency care diagnosis simple reference set (foundation metadata concept)

   Args: 
    path: string path for saving out df



  Returns:
    A pandas Dataframe with the member codes of the mentioned reference set

  Example:
    df_1 = obtain_ECDS_snomed_members()
  
  """
  url = 'https://termbrowser.nhs.uk/sct-browser-api/snomed/uk-edition/v20221123/concepts/991411000000109/members?limit=10000&skip=300&paginate=1'
  response = urlopen(url)
  
  # storing the JSON response 
  # from url in data
  data_json = loads(response.read())

  # convert to df
  codes_list = data_json["members"]
  df = DataFrame(codes_list)
  df.to_csv(path)
  return df
  
def obtain_previous_snomed_codes(df: DataFrame, path: str) -> DataFrame:

  """
  Function to obtain .csv file with  Emergency care diagnosis simple reference set (foundation metadata concept) including previous diagnosis codes

  Args: 
    dataframe with snomed target code, snomed target description and concept

  Returns:
    A pandas Dataframe with the member codes of the mentioned reference set

  Example:
    df_out = obtain_previous_snomed_codes(df):
  

  """

  aux_code = []
  aux_description = []
  aux_concept = []
  payload={}
  headers = {
      'Authorization': 'Bearer ' + credentials["bearer_token"]
    }

  for i in range(len(df.target_code.values)):
    url = "https://ontology.nhs.uk/production1/fhir/ValueSet/$expand?count=100&offset=0&url=http:%2F%2Fsnomed.info%2Fsct%3Ffhir_vs%3Decl%2F(" + str(df.target_code.astype(int).values[i]) + "%2520%257B%257B%2520%252BHISTORY-MAX%2520%257D%257D)"
    response = request("GET", url, headers=headers, data=payload)
    arr = response.json()["expansion"]["contains"]
    concept = df[df.target_code == df.target_code.values[i]].concept.values[0]

    for j in range(len(arr)):
      aux_code.append(arr[j]["code"])
      aux_description.append(arr[j]["display"])
      aux_concept.append(concept)

  df_out = DataFrame({"target_code":aux_code, "target_description":aux_description, "concept":aux_concept})
  df_out.to_csv(path)
  return df_out


def merge_data_sets(df_list, ecds = None):
  """
    Function to obtain merged df out of different sources that were analyzed to obtain the ACSCs snomed codes, and to optionally obtain subset that is present at ECDS dataset
    
  """

  df_out = []
  for i in range(len(df_list)):
    df = df_list[i]
    df_out = concat([df["target_code", "target_description", "concept","source_code","source_description"],df_out])
  df_out = df_out.drop_duplicates(
  subset = ['target_code', 'target_description'],
  keep = 'last').reset_index(drop = True)
  if(ecds):
    df_out = df_out[df_out.target_code.isin(ecds.conceptId.astype(float64).values)]
  return df_out
  



