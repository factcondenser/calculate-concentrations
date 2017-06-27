import sys
import csv
from natsort import natsorted

# Validate command line arguments
if len(sys.argv) < 3:
    print ("**Please make sure that you have specified an input file of type '.tsv' as well as the type of molecule that you are working with (either RNA or gDNA).") 
    quit()

molecule = sys.argv[2].lower()

if molecule != 'rna' and molecule != 'gdna':
    print("**Invalid molecule type: The molecule type must be either RNA or gDNA.")
    quit()

# Create an output file
output_file = open("%s Working Dilutions.txt" % sys.argv[1], "w")

# Use values from the input file to write to the output file
with open(sys.argv[1], "r") as tsv:
    
    # Create a sorted list of the sample concentration
    rows = [line.strip().split('\t') for line in tsv]
    conc_list = []
    for row in rows:
        conc_tuple = (row[0], row[4])    
        conc_list.append(conc_tuple)
    sorted_conc = natsorted(conc_list, key = lambda tuple: tuple[1])
    
    if molecule == 'rna':
        # Create a sorted list of rounded volumes to add to each sample
        conc_two = sorted_conc[0][1] # ng/uL
        VOL_TWO = 4 # uL
        volumes_to_add = []
        for i in range(0, len(sorted_conc) - 2):
            conc_one = sorted_conc[i][1]
            vol_one = float(conc_two) * VOL_TWO / float(conc_one)
            vol_water = VOL_TWO - vol_one
            volume_tuple = (sorted_conc[i][0], round(vol_one, 1), round(vol_water, 1))
            volumes_to_add.append(volume_tuple)
        sorted_volumes = natsorted(volumes_to_add, key = lambda tuple: tuple[1])

        # Adjust for volumes of less than 0.5uL (get rid of outliers)    
        
        # Write working dilutions table to *.txt file
        output_file.write("Sample | Sample uL | H2O uL\n")
        output_file.write("___________________________\n")
        for row in sorted_volumes:
            output_file.write(str(row[0]).center(6) + " | " + str(row[1]).center(9) + " | " + str(row[2]).center(6) + "\n")
            output_file.write("___________________________\n")
    
    # NOT QUITE DONE YET
    if molecule == 'gdna':
         # Create a sorted list of rounded volumes to add to each sample
        conc_two = 8 # ng/uL
        VOL_TWO = 100 # uL
        volumes_to_add = []
        for i in range(0, len(sorted_conc) - 2):
            conc_one = sorted_conc[i][1]
            vol_one = float(conc_two) * VOL_TWO / float(conc_one)
            vol_water = VOL_TWO - vol_one
            volume_tuple = (sorted_conc[i][0], round(vol_one, 1), round(vol_water, 1))
            volumes_to_add.append(volume_tuple)
        sorted_volumes = natsorted(volumes_to_add, key = lambda tuple: tuple[1])

        # Adjust for volumes of less than 0.5uL (get rid of outliers)    
    
        # Write working dilutions table to *.txt file
        output_file.write("Sample | Sample uL | H2O uL\n")
        output_file.write("___________________________\n")
        for row in sorted_volumes:
            output_file.write(str(row[0]).center(6) + " | " + str(row[1]).center(9) + " | " + str(row[2]).center(6) + "\n")
            output_file.write("___________________________\n")
        
    output_file.close()


    
        