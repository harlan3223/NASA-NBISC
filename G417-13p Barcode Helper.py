import tkinter as tk
from tkinter import filedialog
import pandas as pd
import string
import re
from PIL import ImageTk, Image

filename = ''

def select_file():
    global filename
    filename = filedialog.askopenfilename()

def run_script():
    global filename
    tissue_dict = {
        "Lung_R": ["Lung-R", "lungs-r", "lung"],
        "Kidney_R": ["Kidney-R"],
        "Kidney_L": ["Kidney-L"],
        "Eye_R": ["Eye-R"],
        "Ovary_R": ["Ovary-R"],
        "MammaryGland_R": ["Mammary Gland-R"],
        "MammaryMass": ["gross lesions mammary mass"],
        "Kidney": ["Kidney"],
        "Ileum": ["Ileum"],
        "Spleen": ["Spleen"],
        "Liver": ["Liver"],
        "HGland_R": ["H. Gland-R", "gland-r", "H. Glands-R", "h. glandr"],
        "HGland_L": ["h. glands l", "H. Gland-L", "gland-l", "H. Glands-L", "h, glands-l"],
        "Plasma": ["Plasma"],
        "RBCpellet": ["Cell Pellet"],
        "Brain_R": ["Brain-R"],
        "SpleenHalf": ["Spleen-Half"],
        "BoneMarrow": ["Bone Marrow"],
        "Heart": ["Heart"],
        "LungMass_L": ["Lung-L", "Gross Lesions Lung-L", "gross lesions lung mass-l", "gross lesions lung-l", "Gross Lesions Lung-L Mass"],
        "AbdominalCavity": ["gross lesions-abdominal cavity", "gross lesions abdominal cavity"],
        "AbdominalMass": ["gross lesions-abdominal mass", "gross lesions abdominal mass", "Abdominal Mass", "Gross lesions: Abdominal mass"],
        "UterusMass_R": ["gross lesions uterus-r"],
        "LungMass": ["gross lesions lung mass", "gross lesions lung"],
        "KidneyMass": ["gross lesions kidney"],
        "HGlandMass": ["Gross Lesions H. Gland Mass"],
        "MesentericMass": ["gross lesions mesenteric mass"],
        "AbdominalCavityMass": ["Gross Lesions Abdominal Cavity"],
        "OvarianMass": ["Gross Lesions Ovarian Mass", "Ovarian Mass", "Gross lesions ovarian mass", "ovarian mass"],
        "LiverMass": ["Gross Lesion Liver Lesion", "Gross Lesions Liver"],
        "UterineThickEndMass": ["Gross Lesion Uterus Thick End"],
        "PancreasMass": ["Gross Lesions Pancreas Mass", "Gross Lesions Pancreas"],
        "OvarianMass_R": ["Gross Lesions Ovarian Mass-R", "Gross Lesions Ovarian-R Mass", "Gross lesion Ovarian-R Mass"],
        "SpleenMass": ["gross lesions-spleen", "Gross Lesions Spleen", "Gross Lesions Spleen Mass", "Spleen Mass"],
        "LiverCystMass": ["Gross Lesions Liver Cyst"],
        "OvaryCystMass_L": ["Gross Lesions Ovary-L Cyst"],
        "OvarianCystMass_L": ["Gross Lesions Ovarian-l cyst", "gross lesions ovarian cyst-l"],
        "OvarianCystMass": ["gross lesions ovarian cyst"],
        "UterineHornMass_R": ["Gross Lesions Uterine-R Horn"],
        "UterineHornMass_L": ["Gross Lesions Uterine-l Horn", "gross lesions uterine horn-l"],
        "AxillaryLymphNodeMass": ["Gross lesions Axillary Lymph Node (LN)"],
        "UterineHorn_L": ["Left Uterine Horn"],
        "MediasternalLNMass": ["Gross Lesion Mediasternal LN"],
        "AdrenalMass": ["Gross Lesions: Adrenal Mass"],
        "DuodenamMass": ["Gross Lesions Duodenam Mass", "Gross Lesions Duodenum"],
        "SkeletalMuscleMass": ["Gross Lesions Skeletal Muscle Mass"],
        "InguinalMass": ["Inguinal Mass", "InguinalMass", " Inguinal Mass", "Inguinal mass"],
        "LungMass_R": ["Gross Lesions Lung-R", "LungMass r"],
        "Hippocampus_R": ["HPC-R"],
        "Hippocampus_L": ["HPC-L"],
        "Cerebellum_R": ["CERE-R"],
        "BrainCortex_R": ["Cortex-R"],
        "BrainFLobe_R": ["F. Lobe-R", "f. lobe"],
        "UterusMass": ["Gross Lesions Uterus"],
        "MesentaryLNMass": ["Gross Lesions Mesentary L.N."],
        "KidneyMass_R": ["Gross Lesions Kidney-R"],
        "KidneyMass_L": ["Gross Lesions Kidney-L"],
        "SkinMass": ["Gross Lesions Skin Mass"],
        "GeneralLymphNodeMass": ["gross lesions general l.n.", "gross lesions lymph nodes"],
        "PituitaryGlandMass": ["gross lesions pituitary", "gross lesion pituitary gland", "gross lesions pituitary gland"],
        "MandibularMass": ["gross lesions mandibular mass"],
        "LungLobeMass_R": ["gross lesions lung lobe-r"],
        "IleumMass": ["gross lesions ileum"],
        "OvaryMass_L": ["ovary-l"],
        "OvaryMass_R": ["ovary-r"],
        "TailMass": ["gross lesions tail"],
        "MesentericLNMass": ["gross lesions mesenteric l.n.", "gross lesions mesenteric ln", "gross lesions mesenteric lymph node"],
        "UterineHornMass_R": ["gross lesions uterine horn-r"],
        "MediastinalMass": ["gross lesions mediastinal"],
        "UterineCystMass": ["gross lesions uterine cyst"],
        "JejunumMass": ["gross lesions jejunum"]
        

    }
    # Convert the dictionary values to lowercase
    tissue_dict = {k: [i.lower() for i in v] for k, v in tissue_dict.items()}
    
    # Read the CSV file
    df = pd.read_csv(filename)
    box_title = df.columns[0]
    box_title_without_spaces = box_title.replace(" ", "")

    # Define the pattern for box titles to exclude
    pattern = r'R\d+C\d+ Box \d+'

    # Find columns that match the pattern
    matching_columns = [col for col in df.columns if re.match(pattern, col)]

    # Exclude matching columns from the DataFrame
    df = df.drop(columns=matching_columns)

    # Create a dictionary to hold cell labels and corresponding values
    cell_dict = {}

    # Iterate over the DataFrame, storing the cell label and value in the dictionary
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            cell_label = f"{string.ascii_uppercase[i]}{j+1}"
            cell_value = df.iloc[i, j]
            if isinstance(cell_value, str) and cell_value.startswith('Row'):
                continue
            cell_dict[cell_label] = cell_value

    # Convert the dictionary to a DataFrame
    output_df = pd.DataFrame(list(cell_dict.items()), columns=['Cell', 'Value'])

    # Replace NaN or empty cells with 'NO TUBE'
    output_df['Value'] = output_df['Value'].fillna('NO TUBE')
    output_df['rack'] = 'rack_2d_rackid_180ori'
    output_df['box_title'] = 'G417-13p_NBISC-BTSC_' + box_title_without_spaces
    # Split the cell value on the date and use the second part for comparison
    def process_value(value):
        if re.search(' \d{1,2}/\d{1,2}/\d{2,4} ', value):
            # Split the string into words
            words = value.split()
            # Return a string that consists of the tube number and the last two words (assumed to be the tissue type)
            return ' '.join([words[0], words[-2], words[-1]])
        else:
            # If the conditions are not met, return the original value
            return value
    output_df['Value'] = output_df['Value'].apply(process_value)
    # Convert the 'Value' column in your dataframe to lowercase
    output_df['Value'] = output_df['Value'].str.lower()

    # Then in your for loop...
    for key, values in tissue_dict.items():
        for value in values:
            # Use regular expressions to capture the tube number and use it in the replacement string
            pattern = r'(\w+)\s*' + re.escape(value)
            replacement = "G417-13p_" + key + "_LN2_LBNL_" + r'\1'
            output_df['Value'] = output_df['Value'].replace(to_replace=pattern, value=replacement, regex=True)
    
    # After all replacements...
    output_df['Value'] = output_df['Value'].replace('no tube', 'NO TUBE')
     # Extract sample number from "Value" column
    output_df['sample_number'] = output_df['Value'].str.extract(r'G417-13p_\w+_\w+_(\w+)')
    
    # Set "experiment" column based on sample number
    output_df.loc[output_df['sample_number'].notnull(), 'experiment'] = 'Chang_G417-13p_' + output_df['sample_number'].str.upper()

    # Set empty "experiment" column for "NO TUBE" entries
    output_df.loc[output_df['Value'] == 'NO TUBE', 'experiment'] = ''
    #This dictionary will keep track of the counts of each barcode
    barcode_counts = {}

    for i in range(output_df.shape[0]):
        barcode = output_df.at[i, 'Value']
        # Check if the barcode follows the expected format
        if barcode == 'NO TUBE':
            continue
        match = re.search(r"G417-13p_(\w+)_LN2_LBNL_(\w+)", barcode)
        if match:
            tissue_type = match.group(1)
            subject_number = match.group(2).upper()
            base_barcode = f"G417-13p_{tissue_type}_LN2_LBNL_{subject_number}"
            new_barcode = f"G417-13p_{tissue_type}_LN2_LBNL_{subject_number}"

            barcode_counts[base_barcode] = barcode_counts.get(new_barcode, 0) + 1
            if barcode_counts[new_barcode] > 1:
                new_barcode = new_barcode.replace(tissue_type, tissue_type + str(barcode_counts[new_barcode]))

            output_df.at[i, 'Value'] = new_barcode
            
            #if new_barcode in barcode_counts:
                #barcode_counts[new_barcode] += 1
                #new_barcode = new_barcode.replace(tissue_type, tissue_type + str(barcode_counts[new_barcode]))
                #output_df.at[i, 'Value'] = new_barcode
            #else:
                #barcode_counts[new_barcode] = 0
        else:
            print(f"Barcode format did not match for entry: {barcode}")
    # Remove temporary "sample_number" column
    output_df = output_df.drop(columns=['sample_number'])


    # Write the output DataFrame to a CSV file
    output_df.to_csv(box_title_without_spaces + 'RegistrationTemplate.csv', index=False, header=False)

    




root = tk.Tk()
#root.geometry('600x400+50+50')
root.title('Barcode Registration Helper')
#root.iconbitmap('/Desktop/TISSUEHELP/NBISC-logo.ico')
root.iconphoto(False, tk.PhotoImage(file='NBISC-logo.png'))
image = Image.open("OIP.jpg")
image = image.resize((300, 400), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack()

select_button = tk.Button(root, text="Select file", command=select_file)
select_button.pack()

run_button = tk.Button(root, text="Run script", command=run_script)
run_button.pack()

root.mainloop()
