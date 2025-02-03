import sys
from Bio.PDB import MMCIFParser, PDBParser, PDBIO, DSSP

def convert_mmcif_to_pdb(input_cif, output_pdb):
    """Convert an mmCIF file to PDB format."""
    mmcif_parser = MMCIFParser()
    structure = mmcif_parser.get_structure("model", input_cif)
    
    pdb_io = PDBIO()
    pdb_io.set_structure(structure)
    pdb_io.save(output_pdb)
    print(f"Converted {input_cif} to {output_pdb}")

def run_dssp(pdb_file):
    """Run DSSP on the given PDB file and print secondary structure assignments."""
    parser = PDBParser()
    structure = parser.get_structure("model", pdb_file)
    
    dssp = DSSP(structure[0], pdb_file, dssp="mkdssp")
    
    print("\nResidue Secondary Structure Assignments:")
    for key in dssp.keys():
        residue = dssp[key]
        print(f"Residue: {residue[0]}, Secondary Structure: {residue[2]}")

    # Save DSSP output to a file
    with open(pdb_file.replace(".pdb", ".dssp"), "w") as f:
        f.write(f"{'Residue':<10} {'SS':<10}\n")
        for key in dssp.keys():
            residue = dssp[key]
            f.write(f"{residue[0]:<10} {residue[2]:<10}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_mmcif_file>")
        sys.exit(1)

    input_cif = sys.argv[1]
    output_pdb = input_cif.replace(".cif", ".pdb")

    convert_mmcif_to_pdb(input_cif, output_pdb)
    run_dssp(output_pdb)
