import pandas as pd

def post_proc(opgee_results_dir, postproc_export_dir):
    print('OPGEEv4 post processing started')
    # # 1) File paths
    # opgee_results_dir  = 'C:\\Users\KareemYoussef\OneDrive - University of Calgary\\Documents\\Research\\LCA\\OPGEEv4\\opgee\output\\carbon_intensity.csv'
    # postproc_export_dir = 'C:\\Users\\KareemYoussef\\OneDrive - University of Calgary\\Documents\\Research\\LCA\\FUSE\\FUSE_py3\\OPGEE post processing\\output.csv'
    
    # Load the long-form data
    df = pd.read_csv(opgee_results_dir)  
    # expects columns: analysis, field, units, CI, node

    # Get the list of all fields (Field 1, Field 2, …) in their original order
    fields = df['field'].drop_duplicates().tolist()
    print("OPGEEv4 output file imported")

    # Pivot to wide form: one row per node, one col per field
    df_wide = df.pivot(index='node', columns='field', values='CI')
    print("CSV pivoted to wide form")

    # Pull in the unit (assumed identical across all rows)
    unit_value = df['units'].iat[0]
    df_wide.insert(0, 'unit', unit_value)
    print('Units extracted')

    # Reset index into a CI column
    df_wide = df_wide.reset_index().rename(columns={'node': 'CI'})
    print('index reset to CI column')

    # extract numeric IDs from existing field names
    ids = sorted(int(f.split()[1]) for f in fields)
    # build full list from smallest to largest
    full_fields = [f"Field {i}" for i in range(ids[0], ids[-1] + 1)]
    
    i = 0 # Missing field counter
    # insert any missing columns as empty strings
    for f in full_fields:
        if f not in df_wide.columns:
            i += 1
            df_wide[f] = ''   # blank cells

    print(f"Filled missing fields: {[f for f in full_fields if f not in fields]}\nTotal number of missing fields: {i}")
    # overwrite fields list so we order by the full range
    fields = full_fields
    print('Missing fields added as blank columns')

    # Build the “analysis” row: for each field, grab its analysis name
    analysis_row = {
        'CI': 'analysis',
        'unit': unit_value,
    }

    for f in fields:
        # each field has a single analysis value (e.g. “FUSE_run”)
        matches = df.loc[df['field'] == f, 'analysis']                 # Grab the series of any matching rows
        analysis_row[f] = matches.iat[0] if not matches.empty else ''  # If there's at least one, take [0], otherwise blank
        
        if (fields.index(f) % 100 == 0):
            print(f"print field {fields.index(f)} completed")

    # Prepend the analysis row
    df_final = pd.concat(
        [pd.DataFrame([analysis_row]), df_wide],
        ignore_index=True,
        sort=False
    )

    # reorder columns explicitly as ['CI','unit', *fields]
    df_final = df_final[['CI', 'unit'] + fields]
    print('columns re-ordered')

    # Export
    csv_name = "\\OPGEE_postproc_results.csv"
    df_final.to_csv(postproc_export_dir + csv_name, index=False)
    print(f"Written restructured CSV → {postproc_export_dir}")

def main():
    pass

if __name__ == "__main__": 
    main()
#     opgee_results_dir  = 'C:\\Users\KareemYoussef\\OneDrive - University of Calgary\\Documents\\Research\\LCA\\OPGEEv4\\opgee\\output\\carbon_intensity.csv'
#     postproc_export_dir = 'C:\\Users\\KareemYoussef\\OneDrive - University of Calgary\\Documents\\Research\\LCA\\FUSE\\FUSE_py3\\OPGEE post processing\\output.csv'