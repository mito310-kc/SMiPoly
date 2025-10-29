# SMiPoly SMARTS Pattern Design Documentation

## Overview

This document explains how SMiPoly uses SMARTS patterns and reaction rules at the implementation level.

## Key Concept: Pattern-Level Reaction Specification

SMiPoly operates at the **individual SMARTS pattern level**, not at the monomer class level.

### Example: Reaction 104 (Polyester Synthesis)

**Documentation says:**
- Reaction 104: Di/Polycarboxylic Acid [52] + Di/Polyol [53] → Polyester

**Actual implementation:**
- 6 diCOOH SMARTS patterns × 4 diol SMARTS patterns = **24 separate reaction specifications**

```python
# Each of these is a DISTINCT reaction specification in ps_gen.pkl:
['smipoly_diCOOH_1', 'smipoly_diol_1']  # Aliphatic acid + secondary alcohol
['smipoly_diCOOH_1', 'smipoly_diol_2']  # Aliphatic acid + primary alcohol
['smipoly_diCOOH_3', 'smipoly_diol_2']  # Aromatic acid + primary alcohol (PET)
# ... 21 more combinations
```

## Why Multiple Patterns Per Monomer Class?

Each pattern within a monomer class represents a **different chemical substructure**:

### diCOOH Patterns (6 total)

| Pattern | SMARTS | Chemical Meaning |
|---------|--------|------------------|
| diCOOH_1 | `[CX4H2][C](=[O])[OH1]` | Primary aliphatic carboxylic acid |
| diCOOH_2 | `[CX4H1][C](=[O])[OH1]` | Secondary aliphatic carboxylic acid |
| diCOOH_3 | `[c][C](=O)[OH1]` | Aromatic carboxylic acid (e.g., terephthalic acid) |
| diCOOH_4 | `[CX4H2][C](=[O])[Cl,Br]` | Primary aliphatic acid chloride |
| diCOOH_5 | `[CX4H1][C](=[O])[Cl,Br]` | Secondary aliphatic acid chloride |
| diCOOH_6 | `[c][C](=O)[Cl,Br]` | Aromatic acid chloride (e.g., terephthaloyl chloride) |

### diol Patterns (4 total)

| Pattern | SMARTS | Chemical Meaning |
|---------|--------|------------------|
| diol_1 | `[CX4H1][OX2,SX2;H1]` | Secondary alcohol |
| diol_2 | `[CX4H2][OX2,SX2;H1]` | Primary aliphatic alcohol (e.g., ethylene glycol) |
| diol_3 | `[c][OX2,SX2;H1]` | Phenolic alcohol |
| diol_4 | `[CX4;H2,H1,c]([OX2,SX2;H1])[OX2,SX2;H1]` | Vicinal diol |

## Real-World Examples

Each pattern combination produces a different polymer:

| Acid Pattern | Diol Pattern | Product Polymer |
|--------------|--------------|-----------------|
| diCOOH_3 (terephthalic acid) | diol_2 (ethylene glycol) | PET (polyethylene terephthalate) |
| diCOOH_3 (terephthalic acid) | diol_4 (1,4-butanediol) | PBT (polybutylene terephthalate) |
| diCOOH_1 (adipic acid) | diol_2 (ethylene glycol) | Polyethylene adipate |

## Implementation Details

### File Structure

```
/home/user/SMiPoly/
├── src/smipoly/rules/
│   ├── mon_dic.json          # Monomer class name → ID mapping
│   ├── mon_lst.json          # Monomer ID → SMARTS patterns (raw)
│   ├── ps_rxn.pkl            # Reaction ID → RDKit ChemicalReaction
│   └── ps_gen.pkl            # Polymer class → List of (mon1, mon2, rxn) tuples
├── monomer_structure_dict.py # Complete pattern dictionary (340 entries)
├── monomer_structure_dict.json
└── smipoly_reaction_mechanisms.py # Categorized mechanism dict (464 entries)
```

### Source Code Flow

**1. Load Pre-computed Specifications** (`polg.py:42-45`)
```python
with open(os.path.join(db_file, 'ps_gen.pkl'), 'rb') as f:
    Ps_GenL = pickle.load(f)
# Ps_GenL['polyester'] contains 24 P_set tuples for diCOOH + diol
```

**2. Iterate Through Pattern Combinations** (`polg.py:157-185`)
```python
for P_set in Ps_GenL[str(P_class)]:
    targ_mon1 = P_set[0]  # 'smipoly_diCOOH_3'
    targ_mon2 = P_set[1]  # 'smipoly_diol_2'
    targ_rxn = P_set[2]   # Specific RDKit ChemicalReaction
```

**3. Apply Reaction to Matched Molecules** (`funclib.py:402`)
```python
def bipolymA(reactant, targ_rxn, ...):
    prods = targ_rxn.RunReactants(reactant)
```

## Pattern Statistics

### Total Patterns by Monomer Class

| Monomer Class | Pattern Count | Mechanism |
|---------------|---------------|-----------|
| vinyl | 6 | Chain growth (addition) |
| acryl | 39 | Chain growth (addition) |
| bEWole | 156 | Chain growth (addition) |
| diCOOH | 6 | Step growth (polycondensation) |
| diol | 4 | Step growth (polycondensation) |
| diNH2 | 9 | Step growth (polycondensation) |
| diNCO | 11 | Polyaddition (urethane) |
| ... | ... | ... |

**Total:** 340 individual SMARTS patterns across 32 monomer classes

### Total Reaction Combinations

| Mechanism Type | Combinations |
|----------------|--------------|
| Chain growth (homopolymerization) | 201 |
| Step growth (binary) | 234 |
| Ring-opening (chain growth) | 14 |
| Metathesis (ROMP) | 10 |
| Special (COC) | 5 |
| **TOTAL** | **464** |

## Design Rationale

### Why Not Use Class-Level Templates?

**Option A (NOT used):** One template per reaction type
```python
# Hypothetical class-level approach (NOT how SMiPoly works)
reaction_104 = {
    'reactants': ['diCOOH', 'diol'],  # Class names
    'products': ['polyester']
}
```

**Option B (ACTUAL design):** Pre-computed pattern combinations
```python
# Actual SMiPoly approach
ps_gen['polyester'] = [
    ('smipoly_diCOOH_1', 'smipoly_diol_1', rxn_obj_1),
    ('smipoly_diCOOH_1', 'smipoly_diol_2', rxn_obj_2),
    # ... 22 more entries
]
```

**Advantages of Option B:**
1. **Pre-computation:** Reaction SMARTS are validated and compiled once
2. **Specificity:** Each pattern pair has its own optimized reaction template
3. **Performance:** No runtime pattern matching - direct RDKit ChemicalReaction application
4. **Extensibility:** Easy to add new patterns without changing core logic

## Conclusion

The **464-entry expansion** in `smipoly_predefined_mechanism` accurately reflects SMiPoly's actual implementation:

- **Not over-specified:** Each entry corresponds to a real P_set tuple in ps_gen.pkl
- **Not redundant:** Each pattern combination represents a distinct chemical reaction
- **Production-ready:** Aligned with how SMiPoly generates polymers in practice

## References

### Source Files
- `/home/user/SMiPoly/src/smipoly/smip/polg.py` (polymer generation)
- `/home/user/SMiPoly/src/smipoly/smip/funclib.py` (reaction functions)
- `/home/user/SMiPoly/src/smipoly/smip/monc.py` (monomer classification)

### Documentation
- `/home/user/SMiPoly/docs/source/42_Ps_rxnL.md` (reaction list)
- `/home/user/SMiPoly/REACTION_MECHANISMS.md` (mechanism categories)

### Generated Files
- `/home/user/SMiPoly/monomer_structure_dict.py` (340 patterns)
- `/home/user/SMiPoly/smipoly_reaction_mechanisms.py` (464 combinations)
