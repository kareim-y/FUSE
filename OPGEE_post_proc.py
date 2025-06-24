import pandas as pd

def post_proc(opgee_results_dir, postproc_export_dir):

    # # 1) File paths
    # opgee_results_dir  = 'C:\\Users\KareemYoussef\OneDrive - University of Calgary\\Documents\\Research\\LCA\\OPGEEv4\\opgee\output\\carbon_intensity.csv'
    # postproc_export_dir = 'C:\\Users\\KareemYoussef\\OneDrive - University of Calgary\\Documents\\Research\\LCA\\FUSE\\FUSE_py3\\OPGEE post processing\\output.csv'
    
    # Load the long-form data
    df = pd.read_csv(opgee_results_dir)  
    # expects columns: analysis, field, units, CI, node

    # Get the list of all fields (Field 1, Field 2, …) in their original order
    fields = df['field'].drop_duplicates().tolist()

    # Pivot to wide form: one row per node, one col per field
    df_wide = df.pivot(index='node', columns='field', values='CI')

    # Pull in the unit (assumed identical across all rows)
    unit_value = df['units'].iat[0]
    df_wide.insert(0, 'unit', unit_value)

    # Reset index into a CI column
    df_wide = df_wide.reset_index().rename(columns={'node': 'CI'})

    # Build the “analysis” row: for each field, grab its analysis name
    analysis_row = {
        'CI': 'analysis',
        'unit': unit_value,
    }
    for f in fields:
        # each field has a single analysis value (e.g. “FUSE_run”)
        analysis_row[f] = df.loc[df['field'] == f, 'analysis'].iat[0]

    # Prepend the analysis row
    df_final = pd.concat(
        [pd.DataFrame([analysis_row]), df_wide],
        ignore_index=True,
        sort=False
    )

    # reorder columns explicitly as ['CI','unit', *fields]
    df_final = df_final[['CI', 'unit'] + fields]

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