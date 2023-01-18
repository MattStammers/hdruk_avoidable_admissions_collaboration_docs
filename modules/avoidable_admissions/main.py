
from pandas import read_csv, concat
from utilities.processing_steps import ts_req, obtain_snomed_concepts, obtain_previous_snomed_codes, merge_data_sets, obtain_ECDS_snomed_members
from chardet import detect

def main():
   
    with open('hdruk_avoidable_admissions_collaboration_docs/datafiles/codes_to_map.csv', 'rb') as f:
          enc = detect(f.read()) 
 
    df = read_csv("hdruk_avoidable_admissions_collaboration_docs/datafiles/codes_to_map.csv", encoding = enc['encoding'])
    df_4 = read_csv("hdruk_avoidable_admissions_collaboration_docs/datafiles/codes_to_map_v2.csv")
    df_out = concat([df,df_4]).drop_duplicates()
    out_df = df_out.apply(ts_req, axis=1)
    out_df.to_csv('hdruk_avoidable_admissions_collaboration_docs/datafiles/out_df_snapper.csv')

    concepts_protocol = out_df.concept.str.replace ('"',"").str.replace (';',"").drop_duplicates().values
    obtain_snomed_concepts(concepts_protocol, 'out_df_snomed_browser')

    with open('hdruk_avoidable_admissions_collaboration_docs/datafiles/out_df_snomed_browser.csv', 'rb') as f:
        enc = detect(f.read())


    codes_to_map = read_csv('hdruk_avoidable_admissions_collaboration_docs/datafiles/out_df_snomed_browser.csv', encoding = enc['encoding'])
    codes_to_map["source_description"] = codes_to_map.source_description.str.replace ('"',"").str.replace (';',"")
    concepts = codes_to_map.source_description.drop_duplicates().values
    obtain_snomed_concepts(concepts, '"hdruk_avoidable_admissions_collaboration_docs/datafiles/out_df_snapper_snomed_browser.csv"')
    obtain_ECDS_snomed_members("hdruk_avoidable_admissions_collaboration_docs/datafiles/ECDS_codes.csv")
    concepts = read_csv('hdruk_avoidable_admissions_collaboration_docs/datafiles/out_df_snomed_browser.csv', index_col=0)
    with open('hdruk_avoidable_admissions_collaboration_docs/datafiles/out_df_snapper.csv', 'rb') as f:
        enc = detect(f.read()) 
    snapper = read_csv('hdruk_avoidable_admissions_collaboration_docs/datafiles/out_df_snapper.csv', encoding = enc['encoding'], index_col=0)
    concepts_snapper = read_csv('hdruk_avoidable_admissions_collaboration_docs/datafiles/out_df_snapper_snomed_browser.csv', index_col = 0)
    ecds = read_csv('hdruk_avoidable_admissions_collaboration_docs/datafiles/ECDS_codes.csv', index_col = 0)
    df_2 = merge_data_sets([snapper,concepts_snapper,concepts],ecds)
    obtain_previous_snomed_codes(df_2, "hdruk_avoidable_admissions_collaboration_docs/datafiles/ECDS_codes_mapping.csv")

if __name__ == "__main__":
    main()
    
