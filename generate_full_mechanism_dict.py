#!/usr/bin/env python3
"""
Generate complete smipoly_predefined_mechanism with all pattern variations.
Reads monomer_structure_dict.json and expands all patterns.
"""

import json
from pathlib import Path
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def get_base_name(full_name):
    """
    Extract base name from numbered pattern.
    e.g., 'smipoly_vinyl_1' -> 'smipoly_vinyl'
    """
    if full_name.startswith('smipoly_'):
        parts = full_name.rsplit('_', 1)
        if len(parts) == 2 and parts[1].isdigit():
            return parts[0]
    return full_name

def categorize_monomer(base_name):
    """Categorize a monomer base name into mechanism type"""

    # Step-growth monomers
    step_growth_bases = [
        'smipoly_aminCOOH', 'smipoly_hydCOOH', 'smipoly_diCOOH', 'smipoly_diol',
        'smipoly_diol_b', 'smipoly_diamin', 'smipoly_pridiamin', 'smipoly_diNCO',
        'smipoly_dicAnhyd', 'smipoly_diepo', 'smipoly_hindPhenol',
        'smipoly_sfonediX', 'smipoly_BzodiF', 'smipoly_CO', 'smipoly_HCHO'
    ]

    # Chain-growth monomers
    chain_growth_bases = [
        'smipoly_vinyl', 'smipoly_acryl', 'smipoly_bEWole', 'smipoly_styryl',
        'smipoly_allyl', 'smipoly_haloCH', 'smipoly_vinylester', 'smipoly_malei',
        'smipoly_conjdiene', 'smipoly_vinylether', 'smipoly_tertcatCH',
        'smipoly_aliphCH', 'smipoly_cOle'
    ]

    # Ring-opening chain polymerization
    ring_opening_bases = [
        'smipoly_lactone', 'smipoly_lactam', 'smipoly_epo', 'smipoly_cAnhyd'
    ]

    # Metathesis
    metathesis_bases = [
        'smipoly_cycCH'
    ]

    if base_name in step_growth_bases:
        return 'step_growth'
    elif base_name in chain_growth_bases:
        return 'chain_growth'
    elif base_name in ring_opening_bases:
        return 'chain_growth_ring_opening'
    elif base_name in metathesis_bases:
        return 'metathesis'
    else:
        return None

def generate_mechanism_dict():
    """Generate complete smipoly_predefined_mechanism with all variations"""

    # Load monomer structure dict
    monomer_dict = load_json('monomer_structure_dict.json')

    # Group patterns by base name
    patterns_by_base = defaultdict(list)
    for key in monomer_dict.keys():
        base = get_base_name(key)
        patterns_by_base[base].append(key)

    # Sort each group by number
    for base in patterns_by_base:
        patterns_by_base[base].sort(key=lambda x: int(x.rsplit('_', 1)[1]) if x.rsplit('_', 1)[1].isdigit() else 0)

    # Categorize into mechanisms
    mechanisms = {
        'step_growth': [],
        'chain_growth': [],
        'chain_growth_ring_opening': [],
        'metathesis': [],
        'special': []
    }

    # Add all patterns to appropriate categories
    for base, patterns in sorted(patterns_by_base.items()):
        category = categorize_monomer(base)
        if category:
            for pattern in patterns:
                mechanisms[category].append([pattern])

    # Add user-added non-SMiPoly monomers
    mechanisms['step_growth'].extend([
        ["di_acid_chloride", "di_amine"],
        ["di_acid_chloride", "di_ol"],
    ])

    mechanisms['chain_growth'].append(["acetylene"])

    mechanisms['chain_growth_ring_opening'].extend([
        ["cyclic_ether"],
        ["cyclic_carbonate"],
        ["cyclic_sulfide"],
    ])

    mechanisms['metathesis'].extend([
        ["terminal_diene"],
        ["conjugated_di_bromide"],
    ])

    # Add special COC combination
    if 'smipoly_cycCH' in patterns_by_base and 'smipoly_aliphCH' in patterns_by_base:
        # Add all combinations of cycCH and aliphCH
        for cycch in patterns_by_base['smipoly_cycCH']:
            for aliphch in patterns_by_base['smipoly_aliphCH']:
                mechanisms['special'].append([cycch, aliphch])

    # Add binary combinations for step_growth
    # These are important specific combinations
    if 'smipoly_aminCOOH' in patterns_by_base:
        for p in patterns_by_base['smipoly_aminCOOH']:
            mechanisms['step_growth'].append([p, p])  # Alternating copolymer

    if 'smipoly_hydCOOH' in patterns_by_base:
        for p in patterns_by_base['smipoly_hydCOOH']:
            mechanisms['step_growth'].append([p, p])  # Alternating copolymer

    # diCOOH + diol (Polyester)
    if 'smipoly_diCOOH' in patterns_by_base and 'smipoly_diol' in patterns_by_base:
        for dicooh in patterns_by_base['smipoly_diCOOH']:
            for diol in patterns_by_base['smipoly_diol']:
                mechanisms['step_growth'].append([dicooh, diol])

    # diCOOH + diamin (Polyamide)
    if 'smipoly_diCOOH' in patterns_by_base and 'smipoly_diamin' in patterns_by_base:
        for dicooh in patterns_by_base['smipoly_diCOOH']:
            for diamin in patterns_by_base['smipoly_diamin']:
                mechanisms['step_growth'].append([dicooh, diamin])

    # dicAnhyd + pridiamin (Polyimide)
    if 'smipoly_dicAnhyd' in patterns_by_base and 'smipoly_pridiamin' in patterns_by_base:
        for dicanhyd in patterns_by_base['smipoly_dicAnhyd']:
            for pridiamin in patterns_by_base['smipoly_pridiamin']:
                mechanisms['step_growth'].append([dicanhyd, pridiamin])

    # diNCO + diol (Polyurethane)
    if 'smipoly_diNCO' in patterns_by_base and 'smipoly_diol' in patterns_by_base:
        for dinco in patterns_by_base['smipoly_diNCO']:
            for diol in patterns_by_base['smipoly_diol']:
                mechanisms['step_growth'].append([dinco, diol])

    # diepo + diNCO (Polyoxazolidone)
    if 'smipoly_diepo' in patterns_by_base and 'smipoly_diNCO' in patterns_by_base:
        for diepo in patterns_by_base['smipoly_diepo']:
            for dinco in patterns_by_base['smipoly_diNCO']:
                mechanisms['step_growth'].append([diepo, dinco])

    # diol + CO (Polycarbonate)
    if 'smipoly_diol' in patterns_by_base and 'smipoly_CO' in patterns_by_base:
        for diol in patterns_by_base['smipoly_diol']:
            for co in patterns_by_base['smipoly_CO']:
                mechanisms['step_growth'].append([diol, co])

    # sfonediX + diol_b
    if 'smipoly_sfonediX' in patterns_by_base and 'smipoly_diol_b' in patterns_by_base:
        for sfone in patterns_by_base['smipoly_sfonediX']:
            for diol_b in patterns_by_base['smipoly_diol_b']:
                mechanisms['step_growth'].append([sfone, diol_b])

    # BzodiF + diol_b
    if 'smipoly_BzodiF' in patterns_by_base and 'smipoly_diol_b' in patterns_by_base:
        for bzo in patterns_by_base['smipoly_BzodiF']:
            for diol_b in patterns_by_base['smipoly_diol_b']:
                mechanisms['step_growth'].append([bzo, diol_b])

    # Chain-growth binary combinations
    # vinyl + vinyl
    if 'smipoly_vinyl' in patterns_by_base:
        for v in patterns_by_base['smipoly_vinyl']:
            mechanisms['chain_growth'].append([v, v])

    # vinyl + cOle
    if 'smipoly_vinyl' in patterns_by_base and 'smipoly_cOle' in patterns_by_base:
        for vinyl in patterns_by_base['smipoly_vinyl']:
            for cole in patterns_by_base['smipoly_cOle']:
                mechanisms['chain_growth'].append([vinyl, cole])

    # cOle + cOle
    if 'smipoly_cOle' in patterns_by_base:
        for c in patterns_by_base['smipoly_cOle']:
            mechanisms['chain_growth'].append([c, c])

    # Ring-opening: cAnhyd + epo
    if 'smipoly_cAnhyd' in patterns_by_base and 'smipoly_epo' in patterns_by_base:
        for canhyd in patterns_by_base['smipoly_cAnhyd']:
            for epo in patterns_by_base['smipoly_epo']:
                mechanisms['chain_growth_ring_opening'].append([canhyd, epo])

    return mechanisms

if __name__ == '__main__':
    mechanisms = generate_mechanism_dict()

    print("Generated smipoly_predefined_mechanism statistics:")
    print("="*60)
    for category, entries in mechanisms.items():
        print(f"{category}: {len(entries)} entries")

    total = sum(len(entries) for entries in mechanisms.values())
    print(f"\nTotal entries: {total}")

    # Show sample entries
    print("\n" + "="*60)
    print("Sample entries (first 5 per category):")
    for category, entries in mechanisms.items():
        print(f"\n{category}:")
        for entry in entries[:5]:
            print(f"  {entry}")
        if len(entries) > 5:
            print(f"  ... and {len(entries) - 5} more")
