#!/bin/bash
# Script to convert mmCIF files to DSSP format using mkdssp

# Define the directories containing the mmCIF files
directories=("Data/Postprocessed/TS115" "Data/Postprocessed/CB513" "Data/Postprocessed/CASP10")

# Loop through each directory
for dir in "${directories[@]}"; do
    # Check if the directory exists
    if [ -d "$dir" ]; then
        echo "Processing directory: $dir"
        # Loop through each .cif file in the directory
        for cif_file in "$dir"/*.cif; do
            # Check if the file exists
            if [ -f "$cif_file" ]; then
                # Extract the base name of the file (without extension)
                base_name=$(basename "$cif_file" .cif)
                # Define the output .dssp file path
                dssp_file="$dir/${base_name}.dssp"
                # Debugging: Print the paths being checked
                echo "Checking if DSSP file exists: $dssp_file"
                if [ -f "$dssp_file" ]; then
                    echo "DSSP file $dssp_file already exists. Skipping conversion."
                else
                    # Run the mkdssp command
                    mkdssp --write-other --output-format mmcif "$cif_file" "$dssp_file"
                    echo "Converted $cif_file to $dssp_file"
                fi
            else
                echo "No .cif files found in $dir"
            fi
        done
    else
        echo "Directory $dir does not exist."
    fi
done