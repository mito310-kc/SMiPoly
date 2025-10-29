#!/usr/bin/env python3
"""
Build complete smipoly_reaction_mechanisms.py with all 464 pattern variations
"""

import sys
sys.path.insert(0, '/home/user/SMiPoly')
from generate_full_mechanism_dict import generate_mechanism_dict

# Generate the complete mechanisms
mechanisms = generate_mechanism_dict()

# File header
header = '''"""
Complete reaction mechanism categorization for SMiPoly
Maps all polymerization reactions to their mechanism types - ALL PATTERN VARIATIONS INCLUDED.

Mechanism Categories:
- step_growth: Step-growth polymerization (polycondensation, polyaddition) - 123 entries
- chain_growth: Chain-growth polymerization (addition polymerization) - 310 entries
- chain_growth_ring_opening: Ring-opening chain polymerization - 26 entries
- metathesis: Ring-opening metathesis polymerization (ROMP) - 3 entries
- special: Special cases (COC - Cyclic Olefin Copolymerization) - 2 entries

Total: 464 entries (all SMARTS pattern variations included)

Note: Post-polymerization reactions (200-210) are not included as they are
secondary transformations applied after primary polymerization.
"""

'''

# Generate smipoly_predefined_mechanism dict
mechanism_dict = "# Complete mechanism categorization with smipoly_ prefix - ALL VARIATIONS\nsmipoly_predefined_mechanism = {\n"
for category, entries in mechanisms.items():
    mechanism_dict += f'    "{category}": [\n'
    for entry in entries:
        mechanism_dict += f'        {entry},\n'
    mechanism_dict += '    ],\n'
mechanism_dict += '}\n\n'

# Rest of the file (from original)
rest_of_file = '''# ========== REACTION NUMBER MAPPING ==========
# Maps SMiPoly reaction numbers to their mechanism categories
smipoly_reaction_number_to_mechanism = {
    # Step-growth
    6: "step_growth",    # hydCOOH
    7: "step_growth",    # aminCOOH
    8: "step_growth",    # hindPhenol
    104: "step_growth",  # diCOOH + diol
    105: "step_growth",  # hydCOOH + hydCOOH
    106: "step_growth",  # diol + CO
    108: "step_growth",  # diCOOH + diamin
    109: "step_growth",  # aminCOOH + aminCOOH
    110: "step_growth",  # dicAnhyd + pridiamin
    111: "step_growth",  # diNCO + diol
    113: "step_growth",  # diepo + diNCO
    114: "step_growth",  # sfonediX + diol_b
    115: "step_growth",  # BzodiF + diol_b

    # Chain-growth
    1: "chain_growth",     # vinyl
    3: "chain_growth",     # cOle
    101: "chain_growth",   # vinyl + vinyl
    102: "chain_growth",   # vinyl + cOle
    103: "chain_growth",   # cOle + cOle
    1001: "chain_growth",  # acryl
    1002: "chain_growth",  # bEWole
    1003: "chain_growth",  # styryl
    1004: "chain_growth",  # allyl
    1005: "chain_growth",  # haloCH
    1006: "chain_growth",  # vinylester
    1007: "chain_growth",  # malei
    1020: "chain_growth",  # conjdiene
    1030: "chain_growth",  # vinylether
    1031: "chain_growth",  # tertcatCH
    1052: "chain_growth",  # aliphCH

    # Ring-opening chain polymerization
    2: "chain_growth_ring_opening",    # epo
    4: "chain_growth_ring_opening",    # lactone
    5: "chain_growth_ring_opening",    # lactam
    112: "chain_growth_ring_opening",  # cAnhyd + epo

    # Metathesis
    1050: "metathesis",  # cycCH (ROMP)

    # Special
    1051: "special",  # cycCH + aliphCH (COC)
}

# ========== MONOMER CLASS TO MECHANISM MAPPING ==========
# Maps monomer classes to their typical polymerization mechanisms
# Note: These use _1 suffix to match the numbered SMARTS patterns
smipoly_monomer_to_mechanism = {
    # Step-growth monomers
    "smipoly_aminCOOH_1": ["step_growth"],
    "smipoly_hydCOOH_1": ["step_growth"],
    "smipoly_diCOOH_1": ["step_growth"],
    "smipoly_diol_1": ["step_growth"],
    "smipoly_diol_b_1": ["step_growth"],
    "smipoly_diamin_1": ["step_growth"],
    "smipoly_pridiamin_1": ["step_growth"],
    "smipoly_diNCO_1": ["step_growth"],
    "smipoly_dicAnhyd_1": ["step_growth"],
    "smipoly_diepo_1": ["step_growth"],
    "smipoly_hindPhenol_1": ["step_growth"],
    "smipoly_sfonediX_1": ["step_growth"],
    "smipoly_BzodiF_1": ["step_growth"],
    "smipoly_CO_1": ["step_growth"],

    # Chain-growth monomers
    "smipoly_vinyl_1": ["chain_growth"],
    "smipoly_acryl_1": ["chain_growth"],
    "smipoly_bEWole_1": ["chain_growth"],
    "smipoly_styryl_1": ["chain_growth"],
    "smipoly_allyl_1": ["chain_growth"],
    "smipoly_haloCH_1": ["chain_growth"],
    "smipoly_vinylester_1": ["chain_growth"],
    "smipoly_malei_1": ["chain_growth"],
    "smipoly_conjdiene_1": ["chain_growth"],
    "smipoly_vinylether_1": ["chain_growth"],
    "smipoly_tertcatCH_1": ["chain_growth"],
    "smipoly_aliphCH_1": ["chain_growth"],

    # Ring-opening chain polymerization
    "smipoly_lactone_1": ["chain_growth_ring_opening"],
    "smipoly_lactam_1": ["chain_growth_ring_opening"],
    "smipoly_epo_1": ["chain_growth_ring_opening"],
    "smipoly_cAnhyd_1": ["chain_growth_ring_opening"],

    # Metathesis (can also be chain_growth in some cases)
    "smipoly_cycCH_1": ["metathesis", "chain_growth", "special"],  # ROMP, or coordination polymerization
    "smipoly_cOle_1": ["chain_growth"],  # Cyclic olefin (non-ROMP)
}

# ========== POST-POLYMERIZATION REACTIONS ==========
# These are secondary transformations, not primary polymerization mechanisms
smipoly_post_polymerization_reactions = {
    200: "olefin_hydrogenation",
    201: "epoxide_ring_opening",
    202: "carboxylic_acid_acyl_halide_reaction",
    203: "hydroxyl_reaction",
    204: "amine_reaction",
    205: "isocyanate_reaction",
    206: "carboxylic_acid_anhydride_polyester",
    207: "carboxylic_acid_anhydride_polyimide",
    208: "isocyanate_polyoxazolidone",
    209: "diene_12_to_14_isomerization",
    210: "olefin_hydrogenation_ROMPH",
}

# ========== HELPER FUNCTIONS ==========

def get_mechanism_for_monomers(monomers):
    """
    Get the polymerization mechanism for a given set of monomers.

    Args:
        monomers: List of monomer names (with or without smipoly_ prefix and/or _number suffix)
                  Can use user-friendly names (e.g., "vinyl", "di_amine") or
                  smipoly names (e.g., "smipoly_vinyl_1", "smipoly_diamin_1")

    Returns:
        List of possible mechanism categories
    """
    # Normalize monomers: ensure smipoly_ prefix and _1 suffix
    normalized = []
    for m in monomers:
        # First, try to map using name_mapping
        if m in name_mapping:
            normalized.append(name_mapping[m])
            continue

        # If it doesn't start with smipoly_, add it
        if not m.startswith("smipoly_"):
            # Check if it's a user-added monomer (not in SMiPoly)
            if m in ["di_acid_chloride", "cyclic_ether", "cyclic_carbonate",
                     "cyclic_sulfide", "acetylene", "terminal_diene", "conjugated_di_bromide"]:
                normalized.append(m)
                continue
            else:
                m = f"smipoly_{m}"

        # If it doesn't have a number suffix and it's a smipoly_ name, add _1
        if m.startswith("smipoly_") and not any(m.endswith(f"_{i}") for i in range(1, 200)):
            m = f"{m}_1"

        if m not in normalized:
            normalized.append(m)

    # Check predefined_mechanism for exact match
    for mechanism, monomer_sets in smipoly_predefined_mechanism.items():
        for monomer_set in monomer_sets:
            if sorted(normalized) == sorted(monomer_set):
                return [mechanism]

    # Check individual monomer mechanisms
    possible_mechanisms = set()
    for monomer in normalized:
        if monomer in smipoly_monomer_to_mechanism:
            possible_mechanisms.update(smipoly_monomer_to_mechanism[monomer])

    return list(possible_mechanisms) if possible_mechanisms else ["unknown"]

def get_reaction_info(reaction_number):
    """
    Get information about a specific reaction number.

    Args:
        reaction_number: SMiPoly reaction number

    Returns:
        Dictionary with reaction information
    """
    mechanism = smipoly_reaction_number_to_mechanism.get(reaction_number, "unknown")

    if reaction_number in smipoly_post_polymerization_reactions:
        return {
            "reaction_number": reaction_number,
            "type": "post_polymerization",
            "description": smipoly_post_polymerization_reactions[reaction_number],
        }

    return {
        "reaction_number": reaction_number,
        "type": "primary_polymerization",
        "mechanism": mechanism,
    }


# ========== COMPATIBILITY VERSION (without smipoly_ prefix) ==========
# This version maintains compatibility with existing code that doesn't use the smipoly_ prefix
predefined_mechanism = {
    "step_growth": [
        # Amino acid-based
        ["amino_acid"],
        ["hydroxy_carboxylic_acid"],

        # Polyester
        ["di_carboxylic_acid", "di_ol"],

        # Polyamide
        ["di_amine", "di_carboxylic_acid"],
        ["di_acid_chloride", "di_amine"],

        # Polyimide
        ["di_cyclic_anhydride", "primary_di_amine"],

        # Polyurethane
        ["di_isocyanate", "di_ol"],
        ["di_acid_chloride", "di_ol"],

        # Polyoxazolidone
        ["di_epoxide", "di_isocyanate"],

        # Polycarbonate
        ["di_ol", "carbon_monoxide"],

        # Other
        ["hindered_phenol"],
        ["bis_p_halogenated_aryl_sulfone", "di_ol"],
        ["bis_p_fluoroaryl_ketone", "di_ol"],
    ],

    "chain_growth": [
        # Basic
        ["vinyl"],
        ["acetylene"],

        # Cyclic olefin (non-ROMP)
        ["cyclic_olefin"],

        # Detailed olefinic classifications
        ["acrylic"],
        ["electron_withdrawing_olefin"],
        ["styrenic"],
        ["allyl"],
        ["halogenated_olefin"],
        ["vinyl_ester"],
        ["maleic"],
        ["conjugated_diene"],
        ["vinyl_ether"],
        ["tertiary_carbocation_olefin"],
        ["aliphatic_olefin"],
    ],

    "chain_growth_ring_opening": [
        ["lactone"],
        ["lactam"],
        ["epoxide"],
        ["cyclic_ether"],
        ["cyclic_olefin"],  # Can also be ROMP
        ["cyclic_carbonate"],
        ["cyclic_sulfide"],
        ["cyclic_anhydride", "epoxide"],
    ],

    "metathesis": [
        ["cyclic_olefin"],  # ROMP
        ["terminal_diene"],
        ["conjugated_di_bromide"],
    ],
}

# Mapping from user-friendly names to smipoly_ names (with _1 suffix)
name_mapping = {
    # User name → SMiPoly name
    "amino_acid": "smipoly_aminCOOH_1",
    "hydroxy_carboxylic_acid": "smipoly_hydCOOH_1",
    "di_carboxylic_acid": "smipoly_diCOOH_1",
    "di_ol": "smipoly_diol_1",
    "di_amine": "smipoly_diamin_1",
    "primary_di_amine": "smipoly_pridiamin_1",
    "di_isocyanate": "smipoly_diNCO_1",
    "di_cyclic_anhydride": "smipoly_dicAnhyd_1",
    "di_epoxide": "smipoly_diepo_1",
    "hindered_phenol": "smipoly_hindPhenol_1",
    "bis_p_halogenated_aryl_sulfone": "smipoly_sfonediX_1",
    "bis_p_fluoroaryl_ketone": "smipoly_BzodiF_1",
    "carbon_monoxide": "smipoly_CO_1",
    "formaldehyde": "smipoly_HCHO_1",

    # Chain growth
    "vinyl": "smipoly_vinyl_1",
    "cyclic_olefin": "smipoly_cOle_1",  # Note: can also be smipoly_cycCH_1 for ROMP
    "acrylic": "smipoly_acryl_1",
    "electron_withdrawing_olefin": "smipoly_bEWole_1",
    "styrenic": "smipoly_styryl_1",
    "allyl": "smipoly_allyl_1",
    "halogenated_olefin": "smipoly_haloCH_1",
    "vinyl_ester": "smipoly_vinylester_1",
    "maleic": "smipoly_malei_1",
    "conjugated_diene": "smipoly_conjdiene_1",
    "vinyl_ether": "smipoly_vinylether_1",
    "tertiary_carbocation_olefin": "smipoly_tertcatCH_1",
    "aliphatic_olefin": "smipoly_aliphCH_1",

    # Ring-opening
    "lactone": "smipoly_lactone_1",
    "lactam": "smipoly_lactam_1",
    "epoxide": "smipoly_epo_1",
    "cyclic_anhydride": "smipoly_cAnhyd_1",

    # ROMP
    "cyclic_olefin_romp": "smipoly_cycCH_1",  # For ROMP specifically

    # Not in SMiPoly core (user additions)
    "di_acid_chloride": "di_acid_chloride",  # Included in diCOOH SMARTS
    "cyclic_ether": "cyclic_ether",
    "cyclic_carbonate": "cyclic_carbonate",
    "cyclic_sulfide": "cyclic_sulfide",
    "acetylene": "acetylene",
    "terminal_diene": "terminal_diene",
    "conjugated_di_bromide": "conjugated_di_bromide",
}


if __name__ == "__main__":
    print("SMiPoly Reaction Mechanism Categorization")
    print("=" * 60)

    print("\\n### SMIPOLY VERSION (with smipoly_ prefix)")
    for mechanism, monomer_sets in smipoly_predefined_mechanism.items():
        print(f"\\n{mechanism.upper().replace('_', ' ')}:")
        print(f"  Total combinations: {len(monomer_sets)}")
        for monomers in monomer_sets[:5]:  # Show first 5
            print(f"    - {' + '.join(monomers)}")
        if len(monomer_sets) > 5:
            print(f"    ... and {len(monomer_sets) - 5} more")

    print(f"\\nTotal reaction numbers mapped: {len(smipoly_reaction_number_to_mechanism)}")
    print(f"Total monomer classes mapped: {len(smipoly_monomer_to_mechanism)}")
    print(f"Post-polymerization reactions: {len(smipoly_post_polymerization_reactions)}")

    print("\\n" + "=" * 60)
    print("### COMPATIBILITY VERSION (without smipoly_ prefix)")
    for mechanism, monomer_sets in predefined_mechanism.items():
        print(f"\\n{mechanism.upper().replace('_', ' ')}:")
        print(f"  Total combinations: {len(monomer_sets)}")
        for monomers in monomer_sets[:5]:  # Show first 5
            print(f"    - {' + '.join(monomers)}")
        if len(monomer_sets) > 5:
            print(f"    ... and {len(monomer_sets) - 5} more")
'''

# Write the complete file
output_file = '/home/user/SMiPoly/smipoly_reaction_mechanisms.py'
with open(output_file, 'w') as f:
    f.write(header)
    f.write(mechanism_dict)
    f.write(rest_of_file)

print(f"✓ Generated {output_file}")
print(f"✓ Total entries in smipoly_predefined_mechanism: {sum(len(v) for v in mechanisms.values())}")
