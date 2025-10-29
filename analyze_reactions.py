#!/usr/bin/env python3
"""
Analyze SMiPoly reactions and categorize them by mechanism type
"""

import json
import pickle
from pathlib import Path
from collections import defaultdict

def load_pickle(filepath):
    """Load pickle file"""
    with open(filepath, 'rb') as f:
        return pickle.load(f)

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_reactions():
    """Analyze all reactions and categorize them"""

    rules_dir = Path('/home/user/SMiPoly/src/smipoly/rules')

    # Load dictionaries
    mon_dic = load_json(rules_dir / 'mon_dic.json')
    mon_dic_inv = load_json(rules_dir / 'mon_dic_inv.json')
    ps_class = load_json(Path('/home/user/SMiPoly/utilities/rules/ps_class.json'))

    # Load reaction definitions
    try:
        ps_rxn = load_pickle(rules_dir / 'ps_rxn.pkl')
        print(f"Loaded {len(ps_rxn)} reactions from ps_rxn.pkl")
        print(f"Reaction keys: {sorted(ps_rxn.keys())}\n")
    except Exception as e:
        print(f"Error loading ps_rxn.pkl: {e}")
        ps_rxn = {}

    # Load polymer generation rules
    try:
        ps_gen = load_pickle(rules_dir / 'ps_gen.pkl')
        print(f"Loaded ps_gen.pkl")
        print(f"Polymer classes: {list(ps_gen.keys())}\n")

        # Analyze each polymer class
        for poly_class, data in ps_gen.items():
            print(f"\n=== {poly_class} ===")
            if isinstance(data, dict):
                for key, value in data.items():
                    print(f"  {key}: {value}")
            else:
                print(f"  Data type: {type(data)}")
                print(f"  Data: {data}")
    except Exception as e:
        print(f"Error loading ps_gen.pkl: {e}")

    # Monomer name mapping (inverse of mon_dic)
    name_to_id = mon_dic
    id_to_name = {v: k for k, v in mon_dic.items()}

    print("\n" + "="*60)
    print("REACTION CATEGORIZATION ANALYSIS")
    print("="*60)

    # Based on documentation, categorize reactions
    reaction_categories = {
        "chain_growth": {
            1: ["vinyl"],  # Vinyl homopolymer
            3: ["cOle"],   # Cyclic olefin homopolymer
            101: ["vinyl", "vinyl"],  # Vinyl alternating copolymer
            102: ["vinyl", "cOle"],   # Vinyl + cyclic olefin
            103: ["cOle", "cOle"],    # Cyclic olefin + cyclic olefin
        },
        "chain_growth_ring_opening": {
            2: ["epo"],      # Epoxide homopolymer
            4: ["lactone"],  # Lactone homopolymer
            5: ["lactam"],   # Lactam homopolymer
            112: ["cAnhyd", "epo"],  # Cyclic anhydride + epoxide
        },
        "step_growth": {
            6: ["hydCOOH"],  # Hydroxy carboxylic acid
            7: ["aminCOOH"], # Amino acid
            8: ["hindPhenol"],  # Hindered phenol
            104: ["diCOOH", "diol"],  # Dicarboxylic acid + diol (Polyester)
            105: ["hydCOOH", "hydCOOH"],  # Hydroxy carboxylic acid alternating
            106: ["diol", "CO"],  # Diol + carbon monoxide
            108: ["diCOOH", "diamin"],  # Dicarboxylic acid + diamine (Polyamide)
            109: ["aminCOOH", "aminCOOH"],  # Amino acid alternating
            110: ["dicAnhyd", "pridiamin"],  # Dicyclic anhydride + primary diamine (Polyimide)
            111: ["diNCO", "diol"],  # Diisocyanate + diol (Polyurethane)
            113: ["diepo", "diNCO"],  # Diepoxide + diisocyanate (Polyoxazolidone)
            114: ["sfonediX", "diol_b"],  # Bis(p-halogenated aryl)sulfone + diol
            115: ["BzodiF", "diol_b"],  # Bis(p-fluoroaryl)ketone + diol
        },
        "metathesis": {
            1050: ["cycCH"],  # ROMP (Ring-Opening Metathesis Polymerization)
        },
        "special": {
            1051: ["cycCH", "aliphCH"],  # COC (Cyclic Olefin Copolymerization)
        },
        "post_polymerization": {
            200: "olefin hydrogenation",
            201: "epoxide ring-opening",
            202: "carboxylic acid/acyl halide",
            203: "hydroxyl in alcohol/phenol",
            204: "amine",
            205: "isocyanate",
            206: "carboxylic acid anhydride (polyester)",
            207: "carboxylic acid anhydride (polyimide)",
            208: "isocyanate (polyoxazolidone)",
            209: "diene 1,2→1,4 isomerization",
            210: "olefin hydrogenation on ROMPH",
        }
    }

    # Print categorization
    for category, reactions in reaction_categories.items():
        if category == "post_polymerization":
            continue
        print(f"\n{category.upper().replace('_', ' ')}:")
        for rxn_num, monomers in reactions.items():
            monomer_str = " + ".join(monomers)
            print(f"  Reaction {rxn_num}: {monomer_str}")

    print("\n" + "="*60)
    print("DETAILED OLEFINIC MONOMER CLASSIFICATIONS")
    print("="*60)

    olefinic_classes = {
        1001: "acryl",
        1002: "bEWole",
        1003: "styryl",
        1004: "allyl",
        1005: "haloCH",
        1006: "vinylester",
        1007: "malei",
        1020: "conjdiene",
        1030: "vinylether",
        1031: "tertcatCH",
        1050: "cycCH",
        1052: "aliphCH",
    }

    print("\nThese detailed olefinic monomers are typically chain_growth:")
    for rxn_num, name in olefinic_classes.items():
        print(f"  {rxn_num}: {name}")

    print("\n" + "="*60)
    print("UNCATEGORIZED OR MISSING IN SMIPOLY")
    print("="*60)

    # Check what's in user's predefined_mechanism but not in SMiPoly
    user_monomers = {
        "di_acid_chloride": "Included in diCOOH patterns (acyl halide)",
        "cyclic_ether": "Not explicitly defined (epo is closest)",
        "cyclic_carbonate": "Not found in mon_dic",
        "cyclic_sulfide": "Not found in mon_dic",
        "acetylene": "Not found in mon_dic",
        "terminal_diene": "Not found in mon_dic (conjdiene exists)",
        "conjugated_di_bromide": "Not found in mon_dic",
    }

    print("\nMonomers in user's list but not in SMiPoly mon_dic:")
    for monomer, note in user_monomers.items():
        print(f"  {monomer}: {note}")

    return reaction_categories

if __name__ == '__main__':
    analyze_reactions()
