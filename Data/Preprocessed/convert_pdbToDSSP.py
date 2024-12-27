from Bio.PDB import PDBParser, DSSP

# Load PDB structure
parser = PDBParser()
structure = parser.get_structure("model", "input.pdb")

# Run DSSP
dssp = DSSP(structure[0], "input.pdb")

# Access secondary structure for each residue
for key in dssp.keys():
    residue = dssp[key]
    print(f"Residue: {residue[0]}, Secondary Structure: {residue[2]}")