#!/usr/bin/env python3
"""
Convert mon_dic.json and mon_lst.json into a simple dictionary format
where each monomer class name maps to a representative SMARTS pattern.
"""

import json
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def get_representative_pattern(patterns):
    """
    Get the most representative SMARTS pattern from a list.
    If patterns is a string, return it directly.
    If it's a list, return the first (usually simplest) pattern.
    """
    if isinstance(patterns, str):
        return patterns
    elif isinstance(patterns, list):
        if len(patterns) == 0:
            return None
        # Return the first pattern (usually the most basic/representative)
        return patterns[0]
    return None

def create_simple_mapping():
    """Create a simple monomer name -> SMARTS pattern mapping"""

    # Load the dictionaries
    rules_dir = Path('/home/user/SMiPoly/src/smipoly/rules')
    mon_dic = load_json(rules_dir / 'mon_dic.json')
    mon_lst = load_json(rules_dir / 'mon_lst.json')

    # Create the simplified mapping
    simple_mapping = {}

    for monomer_name, monomer_id in mon_dic.items():
        # Get the pattern list for this monomer ID
        patterns = mon_lst.get(str(monomer_id))

        if patterns is not None:
            representative = get_representative_pattern(patterns)
            if representative:
                simple_mapping[monomer_name] = representative

    return simple_mapping

def print_as_python_dict(mapping):
    """Print the mapping as a formatted Python dictionary"""
    print("monomer_structure_dict = {")

    # Sort by key for better readability
    for key in sorted(mapping.keys()):
        value = mapping[key]
        # Escape single quotes in the SMARTS pattern
        value_escaped = value.replace("'", "\\'")
        print(f"    '{key}': '{value_escaped}',")

    print("}")

def save_as_python_file(mapping, output_path):
    """Save the mapping as a Python file"""
    with open(output_path, 'w') as f:
        f.write('"""Simple monomer structure mapping\n')
        f.write('Generated from mon_dic.json and mon_lst.json\n')
        f.write('Each monomer class maps to its representative SMARTS pattern.\n')
        f.write('"""\n\n')

        f.write('monomer_structure_dict = {\n')

        # Sort by key for better readability
        for key in sorted(mapping.keys()):
            value = mapping[key]
            # Escape single quotes in the SMARTS pattern
            value_escaped = value.replace("'", "\\'")
            f.write(f"    '{key}': '{value_escaped}',\n")

        f.write('}\n')

def save_as_json(mapping, output_path):
    """Save the mapping as a JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Create the mapping
    mapping = create_simple_mapping()

    print(f"Created mapping for {len(mapping)} monomer classes\n")
    print("="*60)

    # Print as Python dict
    print_as_python_dict(mapping)
    print("\n" + "="*60 + "\n")

    # Save as Python file
    output_py = Path('/home/user/SMiPoly/monomer_structure_dict.py')
    save_as_python_file(mapping, output_py)
    print(f"Saved Python dictionary to: {output_py}")

    # Save as JSON
    output_json = Path('/home/user/SMiPoly/monomer_structure_dict.json')
    save_as_json(mapping, output_json)
    print(f"Saved JSON mapping to: {output_json}")
