import tkinter as tk
from tkinter import filedialog
import pandas as pd
import string
import re
from PIL import ImageTk, Image

#Type
tissue_dict = {
    "Heart": ["Heart", "Heart1", "Heart2", "Heart3"],
    "Harderian gland": ["HGland", "HGlandMass"],
    "Liver": ["Liver", "Liver1", "Liver2", "Liver3", "LiverMass", "LiverCystMass", "Liver4"],
    "Brain": ["Brain", "Hippocampus", "Cerebellum", "BrainCortex", "BrainFLobe"],
    "Kidney": ["Kidney", "KidneyMass", "KidneyMass2"],
    "Lung": ["Lung", "LungMass", "LungMassR", "LungMassL", "LungLobeMass"],
    "Spleen": ["Spleen", "SpleenMass", "SpleenHalf", "Spleen2"],
    "Bone marrow": ["BoneMarrow", "0BoneMarrow", "BoneMarrow2"],
    "Pancreas": ["Pancreas", "PancreasMass"],
    "Reproductive tract": ["OvarianCystMass", "UterineCystMass", "MammaryMass", "UterineHornMass", "OvaryMass", "UterusMass", "Ovary", "OvarianMassR", "VaginalMass", "UterineMass", "OvarianMass", "UterineThickEndMass", "OvaryCystMass", "UterineHornMass", "UterineHorn", "OvarianCystMass", "CysticOvaryMass"],
    "Blood" : ["Plasma3", "Plasma4" , "Cell Pellets", "Plasma", "Plasma1", "Plasma2", "RBCpellet", "RBCpellet1", "RBCpellet2"],
    "Gastrointestinal tract": ["AbdominalCavityMass", "AbdominalMass", "AbdominalCavity"],
    "Lymph node": ["GeneralLymphNodeMass", "MesentaryLNMass", "PoplitealLNMass", "MandLNMass", "AxillaryLymphNodeMass", "MediasternalLNMass", "MesentaryLN", "MesentericLNMass"],
    "Adrenal gland": ["AdrenalMass"],
    "Duodenum": ["DuodenamMass"],
    "Muscle": ["SkeletalMuscleMass"],
    "Eye": ["Eye"],
    "Mammary gland": ["MammaryGland"],
    "Tail": ["Tail"],
    "Skin": ["Skin", "Skin2"],
    "Mesentery": ["MesentericMass"],
    "Pituitary": ["PituitaryGlandMass", "PituitaryMass"],
    "Mandible": ["MandibularMass"],
    "Ileum": ["IleumMass", "Ileum", "Ileum2"],
    "Jejunum": ["JejunumMass"]
    
}

#Sample name
sample_dict = {
    "Heart": ["Heart", "Heart1", "Heart2", "Heart3"],
    "HarderianR": ["HGlandR", "HGlandR2"],
    "HarderianL": ["HGlandL", "HGlandL2"],
    "Liver": ["Liver", "Liver1", "Liver2", "Liver3", "Liver4"],
    "Brain": ["BrainR", "Hippocampus", "Cerebellum", "BrainCortex", "BrainFLobe", "HippocampusR", "HippocampusL", "CerebellumR", "BrainCortexR", "BrainFLobeR"],
    "BrainR": ["HippocampusR", "CerebellumR", "BrainCortexR", "BrainFLobeR"],
    "Kidney": ["Kidney", "KidneyR", "KidneyL"],
    "Lung": ["Lung", "LungL", "LungR", "LungR2"],
    "Spleen": ["Spleen", "SpleenHalf", "Spleen2"],
    "BoneMarrow": ["BoneMarrow", "0BoneMarrow", "BoneMarrow2"],
    "Pancreas": ["Pancreas"],
    "LungMass": ["LungMassR", "LungMassL"],
    "OvarianMass": ["OvarianMass", "OvarianMassR", "OvarianMassL"],
    "RBCpellet": ["RBCpellet", "RBCpellet1", "RBCpellet2"],
    "Plasma": ["Plasma3", "Plasma", "Plasma1", "Plasma2", "Plasma4" ],
    "UterineThickEndMass": ["UterineThickEndMass"],
    "LiverMass": ["LiverMass"],
    "LiverCystMass": ["LiverCystMass"],
    "OvaryCystMass": ["OvaryCystMass"],
    "UterineHornMass": ["UterineHornMassR", "UterineHornMassL"],
    "UterineHorn": ["UterineHornL"],
    "AxillaryLymphNodeMass": ["AxillaryLymphNodeMass"],
    "MediasternalLNMass": ["MediasternalLNMassL"],
    "OvarianCystMass": ["OvarianCystMassL"],
    "AdrenalMass": ["AdrenalMass"],
    "PancreasMass": ["PancreasMass"],
    "SpleenMass": ["SpleenMass"],
    "DuodenumMass": ["DuodenamMass"],
    "AbdominalMass": ["AbdominalMass"],
    "SkeletalMuscleMass": ["SkeletalMuscleMass"],
    "MesentaryLN": ["MesentaryLN"],
    "CysticOvaryMass": ["CysticOvaryMassL"],
    "MesentaryLNMass": ["MesentericLNMass"],
    "Eye": ["EyeR", "EyeR2"],
    "Ovary": ["OvaryR", "Ovary"],
    "Skin": ["Skin", "Skin2"],
    "MammaryGland": ["MammaryGlandR"],
    "Tail": ["Tail"],
    "AbdominalCavity": ["AbdominalCavity"],
    "UterusMass": ["UterusMassR", "UterusMass"],
    "MandLNMass": ["MandLNMass"],
    "PoplitealLNMass": ["PoplitealLNMass"],
    "InguinalMass": ["InguinalMass"],
    "HarderianMass": ["HGlandMass"],
    "MesentericMass": ["MesentericMass"],
    "AbdominalCavityMass": ["AbdominalCavityMass"],
    "PituitaryMass": ["PituitaryMass"],
    "KidneyMass": ["KidneyMass", "KidneyMass2"],
    "MesentaryLNMass": ["MesentaryLNMass"],
    "GeneralLymphNodeMass": ["GeneralLymphNodeMass"],
    "MandibularMass": ["MandibularMass"],
    "PituitaryGlandMass": ["PituitaryGlandMass"],
    "LungLobeMass": ["LungLobeMassR"],
    "Ileum": ["Ileum", "Ileum2"],
    "IleumMass": ["IleumMass"],
    "OvaryMassL": ["OvaryMassL"],
    "MammaryMass": ["MammaryMass"],
    "UterineCystMass": ["UterineCystMass"],
    "JejunumMass": ["JejunumMass"]
    
    
}

#Section name
section_dict = {
    "Half": ["OvarianCystMass", "JejunumMass", "MammaryMass", "UterineHornMassL", "OvaryMassL", "IleumMass", "KidneyMass2", "PituitaryGlandMass", "MandibularMass", "GeneralLymphNodeMass", "KidneyMass", "PituitaryMass", "AbdominalCavityMass", "MesentaryLNMass", "MesentericMass", "HGlandMass", "PoplitealLNMass", "MandLNMass", "UterusMass", "AbdominalCavity", "SpleenHalf", "MesentericLNMass", "CysticOvaryMassL", "MesentaryLN", "SkeletalMuscleMass", "DuodenamMass", "PancreasMass", "Spleen", "Spleen2", "VaginalMass", "LungMass", "UterineMass", "AbdominalMass", "OvarianMass", "UterineThickEndMass", "LiverMass", "SpleenMass", "LiverCystMass", "OvaryCystMass", "AxillaryLymphNodeMass", "MediasternalLNMassL", "OvarianCystMass", "AdrenalMass"],
    "Whole": ["Ileum", "Ileum2"],
    "Partial": ["Skin2", "Tail", "Heart", "Skin", "Liver", "Liver4", "Heart1", "Heart2", "Heart3", "Liver1", "Liver2", "Liver3"],
    "Hippocampus": ["Hippocampus", "HippocampusR", "HippocampusL"],
    "Cerebellum": ["Cerebellum", "CerebellumR"],
    "Cortex": ["BrainCortex", "BrainCortexR"],
    "Frontal lobe": ["BrainFLobe", "BrainFLobeR"],
    "Right": ["Kidney", "HGlandR2", "EyeR2", "LungR2", "UterusMassR", "BrainR", "EyeR", "OvaryR", "MammaryGlandR", "LungR", "HGlandR", "KidneyR", "LungMassR", "OvarianMassR", "UterineHornMassR"],
    "Left": ["HGlandL", "LungMassL", "OvarianMassL", "Lung_L", "UterineHornL", "HGlandL2", "KidneyL"],
    "Red blood cells": ["RBCpellet", "RBCpellet1", "RBCpellet2"],
    "Plasma": ["Plasma3", "Plasma", "Plasma1", "Plasma2", "Plasma4" ],
    "SpleenMass": ["SpleenMass"],
    "Inguinal": ["InguinalMass"],
    "Right lobe": ["LungLobeMassR"]
}

#Biospecimen category
biospec_dict = {
    "Circulatory": ["Plasma4" ,"Plasma3", "SpleenHalf", "Heart", "Heart1", "Heart2", "Heart3", "Spleen", "Spleen2", "Plasma", "RBCpellet", "SpleenMass", "Plasma1", "Plasma2", "RBCpellet1", "RBCpellet2"], 
    "Neurosensory": ["Brain", "Eye", "Hippocampus", "Cerebellum", "BrainFLobe", "BrainCortex"],
    "Digestive": ["Ileum2", "JejunumMass", "Ileum", "IleumMass", "AbdominalCavityMass", "MesentericMass", "Liver4", "Liver", "DuodenamMass", "PancreasMass", "Liver1", "Liver2", "Liver3", "Pancreas", "InguinalMass", "AbdominalMass", "LiverMass", "LiverCystMass", "AbdominalCavity"],
    "Respiratory": ["Lung", "LungMass", "LungLobeMass"],
    "Excretory": ["KidneyMass2", "KidneyMass", "HGlandMass", "HGland", "Kidney"],
    "Reproductive": ["MammaryMass", "OvaryMass", "UterusMass", "MammaryGland", "Ovary", "OvarianMassR", "CysticOvaryMass", "VaginalMass", "UterineMass", "OvarianMass", "UterineThickEndMass", "UterineCystMass", "OvaryCystMass", "UterineHornMass", "UterineHorn", "OvarianCystMass"],
    "Skeletal": ["MandibularMass", "Tail", "BoneMarrow", "0BoneMarrow", "BoneMarrow2"],
    "Other": ["GeneralLymphNodeMass", "MesentaryLNMass", "PoplitealLNMass", "MandLNMass", "AxillaryLymphNodeMass", "MediasternalLNMass", "MesentaryLN", "MesentericLNMass"],
    "Endocrine": ["PituitaryGlandMass", "AdrenalMass", "PituitaryMass"],
    "Muscular": ["SkeletalMuscleMass"],
    "Integumentary": ["Skin", "Skin2"]
    
    
}

def get_tissue_name(barcode):
    split_barcode = barcode.split('_')
    if len(split_barcode) > 1:
        tissue_term = split_barcode[1]
        tissue_type = get_tissue_type(tissue_term)
        if tissue_type:
            return tissue_type
    return None

def get_tissue_type(term):
    for tissue, tissue_types in tissue_dict.items():
        if term in tissue_types:
            return tissue
    return None

def get_tissue_section(term):
    for tissue, tissue_section in section_dict.items():
        if term in tissue_section:
            return tissue
    return None

def get_tissue_biospec(term):
    for tissue, tissue_biospec in biospec_dict.items():
        if term in tissue_biospec:
            return tissue
    return None

def get_sampname(term):
    for tissue, tissue_samp in sample_dict.items():
        if term in tissue_samp:
            return tissue
    return None

def get_section(barcode):
    split_barcode = barcode.split('_')
    if len(split_barcode) > 1:
        tissue_term = split_barcode[1]
        if split_barcode[2] == "R" or split_barcode[2] == "L":
            tissue_term = split_barcode[1] + split_barcode[2]
        tissue_section = get_tissue_section(tissue_term)
        if tissue_section:
            return tissue_section
    return None

def get_biospec(barcode):
    split_barcode = barcode.split('_')
    if len(split_barcode) > 1:
        tissue_term = split_barcode[1]
        tissue_biospec = get_tissue_biospec(tissue_term)
        if tissue_biospec:
            return tissue_biospec
    return None

def replace_tissue_name(row):
    # Split barcode and sample name
    split_barcode = row['Barcode'].split('_')
    split_sample_name = row['Sample name'].split('_')

    # If barcode and sample name are properly formed
    if len(split_barcode) > 1 and len(split_sample_name) > 1:
        tissue_term = split_barcode[1]
        if split_barcode[2] == "R" or split_barcode[2] == "L":
            tissue_term = split_barcode[1] + split_barcode[2]
        tissue_sample = get_sampname(tissue_term)
        if tissue_sample:
            split_sample_name[-1] = tissue_sample # Replace 'Heart' with the tissue term
            return '_'.join(split_sample_name)  # Join the elements back into a string

    return row['Sample name']  # If barcode or sample name is not properly formed, return the original sample name


def open_file():
    global filename
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    
    
# Apply the function to the DataFrame
def run_script():
    df = pd.read_excel(filename)
    df['Sample name'] = df.apply(replace_tissue_name, axis=1)
    df['Type (cntp_name)'] = df['Barcode'].apply(get_tissue_name)
    df['Section'] = df['Barcode'].apply(get_section)
    df['Biospecimen category'] = df['Barcode'].apply(get_biospec)
    df['Sample preservation method'] = 'LN2'
    df['Sample storage temperature'] = '-80C'
    df.to_excel('output.xlsx', index=False)

# Create the Tkinter window
root = tk.Tk()
root.iconphoto(False, tk.PhotoImage(file='NBISC-logo.png'))
image = Image.open("nasa.png")
image = image.resize((300, 250), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack()
# Create the "Open" button and the "Run" button
open_button = tk.Button(root, text="Open File", command=open_file)
run_button = tk.Button(root, text="Run Script", command=run_script)

# Add the buttons to the window
open_button.pack()
run_button.pack()

# Run the Tkinter event loop
root.mainloop()
