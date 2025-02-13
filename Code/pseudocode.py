function DSSP_8State(structure):
    atoms = parse_pdb(structure)
    hbonds = find_hydrogen_bonds(atoms)
    
    for each residue in atoms:
        structure = assign_secondary_structure_8State(residue, hbonds)
        secondary_structure_map[residue] = structure
    
    return secondary_structure_map

function find_hydrogen_bonds(atoms):
    hbonds = []
    for each donor in atoms:
        for each acceptor in atoms:
            if is_valid_hydrogen_bond(donor, acceptor):
                hbonds.append((donor, acceptor))
    return hbonds

function is_valid_hydrogen_bond(donor, acceptor):
    energy = compute_hydrogen_bond_energy(donor, acceptor)
    return energy < -0.5

function assign_secondary_structure_8State(residue, hbonds):
    if residue forms α-helix:
        return "H"
    else if residue forms 3₁₀-helix:
        return "G"
    else if residue forms π-helix:
        return "I"
    else if residue forms β-strand:
        return "E"
    else if residue forms β-bridge:
        return "B"
    else if residue forms turn:
        return "T"
    else if residue forms bend:
        return "S"
    else:
        return "C"  # Coil / Random structure
