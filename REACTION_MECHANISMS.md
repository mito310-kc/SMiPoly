# SMiPoly Reaction Mechanism Categorization

Complete guide to polymerization reaction mechanisms in SMiPoly.

## Overview

This document describes the categorization of all polymerization reactions in SMiPoly into four main mechanism types:

1. **Step-Growth** - Polycondensation and polyaddition reactions
2. **Chain-Growth** - Addition polymerization reactions
3. **Chain-Growth Ring-Opening** - Ring-opening polymerization
4. **Metathesis** - Ring-opening metathesis polymerization (ROMP)

Additionally, there are **Special** mechanisms (e.g., COC) and **Post-Polymerization** reactions (200-210).

## Files

- `smipoly_reaction_mechanisms.py` - Complete reaction mechanism definitions
- `monomer_structure_dict.py` - SMARTS patterns for all 340 monomer variations
- `monomer_structure_dict.json` - JSON version of SMARTS patterns
- `REACTION_MECHANISMS.md` - This documentation file

## Usage

### Basic Usage

```python
from smipoly_reaction_mechanisms import predefined_mechanism

# Access mechanism categories
step_growth_reactions = predefined_mechanism["step_growth"]
chain_growth_reactions = predefined_mechanism["chain_growth"]

# Example: Find polyamide synthesis
for monomers in step_growth_reactions:
    if "di_amine" in monomers and "di_carboxylic_acid" in monomers:
        print(f"Polyamide: {' + '.join(monomers)}")
```

### Using SMiPoly Prefixed Names

```python
from smipoly_reaction_mechanisms import smipoly_predefined_mechanism

# More specific SMiPoly monomer names
step_growth = smipoly_predefined_mechanism["step_growth"]
# Contains entries like: ["smipoly_diamin", "smipoly_diCOOH"]
```

### Helper Functions

```python
from smipoly_reaction_mechanisms import get_mechanism_for_monomers, get_reaction_info

# Get mechanism for specific monomers
mechanisms = get_mechanism_for_monomers(["vinyl", "vinyl"])
print(mechanisms)  # ['chain_growth']

# Get information about a reaction number
info = get_reaction_info(104)
print(info)
# {'reaction_number': 104, 'type': 'primary_polymerization', 'mechanism': 'step_growth'}
```

## Mechanism Categories

### 1. Step-Growth Polymerization

Reactions where monomers react through functional groups, typically with loss of small molecules (H₂O, HCl, etc.).

**Examples:**
- Polyester: `di_carboxylic_acid + di_ol → Polyester + H₂O`
- Polyamide: `di_amine + di_carboxylic_acid → Polyamide + H₂O`
- Polyimide: `di_cyclic_anhydride + primary_di_amine → Polyimide`
- Polyurethane: `di_isocyanate + di_ol → Polyurethane`

**SMiPoly Reactions:** 6, 7, 8, 104-111, 113-115

**Total combinations:** 15 (with smipoly_ prefix), 13 (without prefix)

### 2. Chain-Growth Polymerization

Addition polymerization where monomers add to active chain ends without loss of atoms.

**Examples:**
- Polyethylene: `vinyl → Polyethylene`
- Polystyrene: `styrenic → Polystyrene`
- PMMA: `acrylic → Poly(methyl methacrylate)`
- Polybutadiene: `conjugated_diene → Polybutadiene`

**Detailed Olefinic Classifications:**
- `acryl` (39 SMARTS patterns)
- `bEWole` (156 patterns) - electron-withdrawing olefins
- `styryl` (43 patterns) - styrenic monomers
- `allyl` (6 patterns)
- `haloCH` (10 patterns) - halogenated olefins
- `vinylester` (6 patterns)
- `malei` (2 patterns) - maleimide-based
- `conjdiene` (6 patterns) - conjugated dienes
- `vinylether` (9 patterns)
- `tertcatCH` (2 patterns) - tertiary carbocation forming
- `aliphCH` (2 patterns) - aliphatic olefins

**SMiPoly Reactions:** 1, 3, 101-103, 1001-1007, 1020, 1030-1031, 1052

**Total combinations:** 17 (with smipoly_ prefix), 14 (without prefix)

### 3. Chain-Growth Ring-Opening

Polymerization through ring-opening of cyclic monomers.

**Examples:**
- Polycaprolactone: `lactone → PCL`
- Nylon 6: `lactam → Polyamide`
- Polyethylene oxide: `epoxide → PEO`
- Cyclic anhydride copolymer: `cyclic_anhydride + epoxide → Copolymer`

**SMiPoly Reactions:** 2, 4, 5, 112

**Total combinations:** 7 (with smipoly_ prefix), 8 (without prefix)

### 4. Metathesis Polymerization

Ring-opening metathesis polymerization (ROMP) using transition metal catalysts.

**Examples:**
- Polynorbornene: `cyclic_olefin (ROMP) → Polynorbornene`
- Polyoctenamer: `cyclic_olefin (ROMP) → Polyoctenamer`

**SMiPoly Reactions:** 1050

**Total combinations:** 3

### 5. Special Mechanisms

**COC (Cyclic Olefin Copolymerization):**
- Reaction 1051: `cyclic_olefin + aliphatic_olefin → COC polymer`
- Used for optical materials (TOPAS, ARTON)

## Monomer Name Mapping

### User-Friendly Names ↔ SMiPoly Names

| User-Friendly Name | SMiPoly Name | Description |
|-------------------|--------------|-------------|
| `amino_acid` | `smipoly_aminCOOH` | Amino acid monomers |
| `hydroxy_carboxylic_acid` | `smipoly_hydCOOH` | Hydroxy carboxylic acids |
| `di_carboxylic_acid` | `smipoly_diCOOH` | Dicarboxylic acids |
| `di_ol` | `smipoly_diol` | Diols |
| `di_amine` | `smipoly_diamin` | Diamines |
| `di_isocyanate` | `smipoly_diNCO` | Diisocyanates |
| `vinyl` | `smipoly_vinyl` | Vinyl monomers |
| `acrylic` | `smipoly_acryl` | Acrylic/methacrylic monomers |
| `styrenic` | `smipoly_styryl` | Styrene-based monomers |
| `lactone` | `smipoly_lactone` | Cyclic esters |
| `lactam` | `smipoly_lactam` | Cyclic amides |
| `epoxide` | `smipoly_epo` | Epoxide/oxirane |
| `cyclic_olefin` | `smipoly_cOle` or `smipoly_cycCH` | Cyclic olefins (context-dependent) |

Full mapping available in `smipoly_reaction_mechanisms.py` → `name_mapping` dictionary.

## Reaction Numbers

### Primary Polymerization Reactions

| Reaction # | Monomers | Mechanism | Product |
|-----------|----------|-----------|---------|
| 1 | vinyl | chain_growth | Polyolefin |
| 2 | epoxide | chain_growth_ring_opening | Polyether |
| 3 | cyclic olefin | chain_growth | Polyolefin |
| 4 | lactone | chain_growth_ring_opening | Polyester |
| 5 | lactam | chain_growth_ring_opening | Polyamide |
| 6 | hydroxy carboxylic acid | step_growth | Polyester |
| 7 | amino acid | step_growth | Polyamide |
| 8 | hindered phenol | step_growth | Polyphenol |
| 101-103 | vinyl/cyclic olefin combinations | chain_growth | Copolymers |
| 104 | diCOOH + diol | step_growth | Polyester |
| 105 | hydCOOH + hydCOOH | step_growth | Polyester |
| 106 | diol + CO | step_growth | Polycarbonate |
| 108 | diCOOH + diamin | step_growth | Polyamide |
| 109 | aminCOOH + aminCOOH | step_growth | Polyamide |
| 110 | dicAnhyd + pridiamin | step_growth | Polyimide |
| 111 | diNCO + diol | step_growth | Polyurethane |
| 112 | cAnhyd + epo | chain_growth_ring_opening | Copolymer |
| 113 | diepo + diNCO | step_growth | Polyoxazolidone |
| 114 | sfonediX + diol_b | step_growth | Polysulfone |
| 115 | BzodiF + diol_b | step_growth | Polyetherketone |
| 1001-1052 | Detailed olefinic classes | chain_growth | Various polyolefins |
| 1050 | cycCH (ROMP) | metathesis | Polyolefin |
| 1051 | cycCH + aliphCH (COC) | special | COC polymer |

### Post-Polymerization Reactions (200-210)

These are secondary transformations applied after primary polymerization:

| Reaction # | Description |
|-----------|-------------|
| 200 | Olefin hydrogenation |
| 201 | Epoxide ring-opening |
| 202 | Carboxylic acid/acyl halide reaction |
| 203 | Hydroxyl reaction in alcohols/phenols |
| 204 | Amine reaction |
| 205 | Isocyanate reaction |
| 206 | Carboxylic acid anhydride (polyester) |
| 207 | Carboxylic acid anhydride (polyimide) |
| 208 | Isocyanate (polyoxazolidone) |
| 209 | Diene 1,2→1,4 isomerization |
| 210 | Olefin hydrogenation on ROMPH |

## Monomers Not in SMiPoly Core

These monomers appear in the user's `predefined_mechanism` but are not explicitly defined in SMiPoly's `mon_dic.json`:

| Monomer | Status |
|---------|--------|
| `di_acid_chloride` | Included in `smipoly_diCOOH` SMARTS patterns (acyl halide) |
| `cyclic_ether` | Not explicitly defined (epoxide is closest match) |
| `cyclic_carbonate` | Not found in mon_dic |
| `cyclic_sulfide` | Not found in mon_dic |
| `acetylene` | Not found in mon_dic |
| `terminal_diene` | Not found in mon_dic (conjugated_diene exists) |
| `conjugated_di_bromide` | Not found in mon_dic |

**Recommendation:** These can be added as custom monomers or integrated into SMiPoly if needed.

## Statistics

- **Total SMiPoly reaction numbers mapped:** 35
- **Total monomer classes mapped:** 32
- **Post-polymerization reactions:** 11
- **Total SMARTS patterns:** 340
- **Mechanism categories:** 4 (+ 1 special)

## Common Polymer Examples

### Step-Growth Polymers
- **PET (Polyethylene terephthalate):** `diCOOH (terephthalic acid) + diol (ethylene glycol)`
- **Nylon 6,6:** `diamin (hexamethylenediamine) + diCOOH (adipic acid)`
- **Polyurethane (PU):** `diNCO (MDI/TDI) + diol (polyol)`
- **Kapton (Polyimide):** `dicAnhyd (PMDA) + pridiamin (ODA)`
- **PEEK:** `BzodiF (difluorobenzophenone) + diol_b (hydroquinone)`

### Chain-Growth Polymers
- **Polyethylene (PE):** `vinyl (ethylene)`
- **Polypropylene (PP):** `vinyl (propylene)`
- **Polystyrene (PS):** `styryl (styrene)`
- **PMMA:** `acryl (methyl methacrylate)`
- **PTFE:** `haloCH (tetrafluoroethylene)`
- **Polybutadiene:** `conjdiene (butadiene)`

### Ring-Opening Polymers
- **PCL (Polycaprolactone):** `lactone (ε-caprolactone)`
- **Nylon 6:** `lactam (ε-caprolactam)`
- **PEO (Polyethylene oxide):** `epo (ethylene oxide)`
- **PLA (Polylactic acid):** `lactone (lactide)` or `hydCOOH (lactic acid)`

### Metathesis Polymers
- **Polynorbornene:** `cycCH (norbornene)` via ROMP
- **Polyoctenamer:** `cycCH (cyclooctene)` via ROMP

## References

- SMiPoly Documentation: `docs/source/42_Ps_rxnL.md`
- Monomer Dictionary: `src/smipoly/rules/mon_dic.json`
- Monomer SMARTS Patterns: `src/smipoly/rules/mon_lst.json`
- Reaction Definitions: `src/smipoly/rules/ps_rxn.pkl`

## Questions Answered

### Q: これらに属さない反応はありそうか？ (Are there reactions that don't belong to these categories?)

**A: はい、いくつかあります：**

1. **Post-polymerization reactions (200-210)** - これらは後処理反応なので、主要な重合メカニズムではありません。

2. **COC (Cyclic Olefin Copolymerization)** - "special"カテゴリに分類されています。配位重合の特殊ケースです。

3. **ユーザーが追加したい反応** - SMiPolyのコアにない以下の反応：
   - `cyclic_carbonate` - 環状カーボネートの重合
   - `cyclic_sulfide` - 環状スルフィドの重合
   - `acetylene` - アセチレン系重合
   - `terminal_diene` - 末端ジエンのメタセシス
   - `conjugated_di_bromide` - 共役ジブロミドのカップリング

4. **その他の可能性のある反応メカニズム：**
   - **Electrochemical polymerization** - 電気化学重合
   - **Photopolymerization** - 光重合（フリーラジカル、カチオン）
   - **Plasma polymerization** - プラズマ重合
   - **Enzymatic polymerization** - 酵素重合
   - **Solid-state polymerization** - 固相重合

これらの特殊な反応を追加する場合は、新しいカテゴリ（例：`"electrochemical"`, `"photo"`, `"enzymatic"`）を作成することをお勧めします。

## Contributing

To add new reactions or monomers:

1. Add SMARTS pattern to `monomer_structure_dict.json`
2. Update `smipoly_reaction_mechanisms.py` with new monomer class
3. Categorize into appropriate mechanism type
4. Update this documentation

---

**Generated with Claude Code**
