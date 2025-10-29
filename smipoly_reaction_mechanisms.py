"""
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

# Complete mechanism categorization with smipoly_ prefix - ALL VARIATIONS
smipoly_predefined_mechanism = {
    "step_growth": [
        ['smipoly_BzodiF_1'],
        ['smipoly_CO_1'],
        ['smipoly_HCHO_1'],
        ['smipoly_aminCOOH_1'],
        ['smipoly_aminCOOH_2'],
        ['smipoly_diCOOH_1'],
        ['smipoly_diCOOH_2'],
        ['smipoly_diCOOH_3'],
        ['smipoly_diCOOH_4'],
        ['smipoly_diCOOH_5'],
        ['smipoly_diCOOH_6'],
        ['smipoly_diNCO_1'],
        ['smipoly_diNCO_2'],
        ['smipoly_diamin_1'],
        ['smipoly_diamin_2'],
        ['smipoly_diamin_3'],
        ['smipoly_diamin_4'],
        ['smipoly_dicAnhyd_1'],
        ['smipoly_dicAnhyd_2'],
        ['smipoly_diepo_1'],
        ['smipoly_diepo_2'],
        ['smipoly_diepo_3'],
        ['smipoly_diepo_4'],
        ['smipoly_diepo_5'],
        ['smipoly_diol_1'],
        ['smipoly_diol_2'],
        ['smipoly_diol_3'],
        ['smipoly_diol_4'],
        ['smipoly_diol_b_1'],
        ['smipoly_diol_b_2'],
        ['smipoly_diol_b_3'],
        ['smipoly_hindPhenol_1'],
        ['smipoly_hydCOOH_1'],
        ['smipoly_hydCOOH_2'],
        ['smipoly_pridiamin_1'],
        ['smipoly_pridiamin_2'],
        ['smipoly_sfonediX_1'],
        ['di_acid_chloride', 'di_amine'],
        ['di_acid_chloride', 'di_ol'],
        ['smipoly_aminCOOH_1', 'smipoly_aminCOOH_1'],
        ['smipoly_aminCOOH_2', 'smipoly_aminCOOH_2'],
        ['smipoly_hydCOOH_1', 'smipoly_hydCOOH_1'],
        ['smipoly_hydCOOH_2', 'smipoly_hydCOOH_2'],
        ['smipoly_diCOOH_1', 'smipoly_diol_1'],
        ['smipoly_diCOOH_1', 'smipoly_diol_2'],
        ['smipoly_diCOOH_1', 'smipoly_diol_3'],
        ['smipoly_diCOOH_1', 'smipoly_diol_4'],
        ['smipoly_diCOOH_2', 'smipoly_diol_1'],
        ['smipoly_diCOOH_2', 'smipoly_diol_2'],
        ['smipoly_diCOOH_2', 'smipoly_diol_3'],
        ['smipoly_diCOOH_2', 'smipoly_diol_4'],
        ['smipoly_diCOOH_3', 'smipoly_diol_1'],
        ['smipoly_diCOOH_3', 'smipoly_diol_2'],
        ['smipoly_diCOOH_3', 'smipoly_diol_3'],
        ['smipoly_diCOOH_3', 'smipoly_diol_4'],
        ['smipoly_diCOOH_4', 'smipoly_diol_1'],
        ['smipoly_diCOOH_4', 'smipoly_diol_2'],
        ['smipoly_diCOOH_4', 'smipoly_diol_3'],
        ['smipoly_diCOOH_4', 'smipoly_diol_4'],
        ['smipoly_diCOOH_5', 'smipoly_diol_1'],
        ['smipoly_diCOOH_5', 'smipoly_diol_2'],
        ['smipoly_diCOOH_5', 'smipoly_diol_3'],
        ['smipoly_diCOOH_5', 'smipoly_diol_4'],
        ['smipoly_diCOOH_6', 'smipoly_diol_1'],
        ['smipoly_diCOOH_6', 'smipoly_diol_2'],
        ['smipoly_diCOOH_6', 'smipoly_diol_3'],
        ['smipoly_diCOOH_6', 'smipoly_diol_4'],
        ['smipoly_diCOOH_1', 'smipoly_diamin_1'],
        ['smipoly_diCOOH_1', 'smipoly_diamin_2'],
        ['smipoly_diCOOH_1', 'smipoly_diamin_3'],
        ['smipoly_diCOOH_1', 'smipoly_diamin_4'],
        ['smipoly_diCOOH_2', 'smipoly_diamin_1'],
        ['smipoly_diCOOH_2', 'smipoly_diamin_2'],
        ['smipoly_diCOOH_2', 'smipoly_diamin_3'],
        ['smipoly_diCOOH_2', 'smipoly_diamin_4'],
        ['smipoly_diCOOH_3', 'smipoly_diamin_1'],
        ['smipoly_diCOOH_3', 'smipoly_diamin_2'],
        ['smipoly_diCOOH_3', 'smipoly_diamin_3'],
        ['smipoly_diCOOH_3', 'smipoly_diamin_4'],
        ['smipoly_diCOOH_4', 'smipoly_diamin_1'],
        ['smipoly_diCOOH_4', 'smipoly_diamin_2'],
        ['smipoly_diCOOH_4', 'smipoly_diamin_3'],
        ['smipoly_diCOOH_4', 'smipoly_diamin_4'],
        ['smipoly_diCOOH_5', 'smipoly_diamin_1'],
        ['smipoly_diCOOH_5', 'smipoly_diamin_2'],
        ['smipoly_diCOOH_5', 'smipoly_diamin_3'],
        ['smipoly_diCOOH_5', 'smipoly_diamin_4'],
        ['smipoly_diCOOH_6', 'smipoly_diamin_1'],
        ['smipoly_diCOOH_6', 'smipoly_diamin_2'],
        ['smipoly_diCOOH_6', 'smipoly_diamin_3'],
        ['smipoly_diCOOH_6', 'smipoly_diamin_4'],
        ['smipoly_dicAnhyd_1', 'smipoly_pridiamin_1'],
        ['smipoly_dicAnhyd_1', 'smipoly_pridiamin_2'],
        ['smipoly_dicAnhyd_2', 'smipoly_pridiamin_1'],
        ['smipoly_dicAnhyd_2', 'smipoly_pridiamin_2'],
        ['smipoly_diNCO_1', 'smipoly_diol_1'],
        ['smipoly_diNCO_1', 'smipoly_diol_2'],
        ['smipoly_diNCO_1', 'smipoly_diol_3'],
        ['smipoly_diNCO_1', 'smipoly_diol_4'],
        ['smipoly_diNCO_2', 'smipoly_diol_1'],
        ['smipoly_diNCO_2', 'smipoly_diol_2'],
        ['smipoly_diNCO_2', 'smipoly_diol_3'],
        ['smipoly_diNCO_2', 'smipoly_diol_4'],
        ['smipoly_diepo_1', 'smipoly_diNCO_1'],
        ['smipoly_diepo_1', 'smipoly_diNCO_2'],
        ['smipoly_diepo_2', 'smipoly_diNCO_1'],
        ['smipoly_diepo_2', 'smipoly_diNCO_2'],
        ['smipoly_diepo_3', 'smipoly_diNCO_1'],
        ['smipoly_diepo_3', 'smipoly_diNCO_2'],
        ['smipoly_diepo_4', 'smipoly_diNCO_1'],
        ['smipoly_diepo_4', 'smipoly_diNCO_2'],
        ['smipoly_diepo_5', 'smipoly_diNCO_1'],
        ['smipoly_diepo_5', 'smipoly_diNCO_2'],
        ['smipoly_diol_1', 'smipoly_CO_1'],
        ['smipoly_diol_2', 'smipoly_CO_1'],
        ['smipoly_diol_3', 'smipoly_CO_1'],
        ['smipoly_diol_4', 'smipoly_CO_1'],
        ['smipoly_sfonediX_1', 'smipoly_diol_b_1'],
        ['smipoly_sfonediX_1', 'smipoly_diol_b_2'],
        ['smipoly_sfonediX_1', 'smipoly_diol_b_3'],
        ['smipoly_BzodiF_1', 'smipoly_diol_b_1'],
        ['smipoly_BzodiF_1', 'smipoly_diol_b_2'],
        ['smipoly_BzodiF_1', 'smipoly_diol_b_3'],
    ],
    "chain_growth": [
        ['smipoly_acryl_1'],
        ['smipoly_acryl_2'],
        ['smipoly_acryl_3'],
        ['smipoly_acryl_4'],
        ['smipoly_acryl_5'],
        ['smipoly_acryl_6'],
        ['smipoly_acryl_7'],
        ['smipoly_acryl_8'],
        ['smipoly_acryl_9'],
        ['smipoly_acryl_10'],
        ['smipoly_acryl_11'],
        ['smipoly_acryl_12'],
        ['smipoly_acryl_13'],
        ['smipoly_acryl_14'],
        ['smipoly_acryl_15'],
        ['smipoly_acryl_16'],
        ['smipoly_acryl_17'],
        ['smipoly_acryl_18'],
        ['smipoly_acryl_19'],
        ['smipoly_acryl_20'],
        ['smipoly_acryl_21'],
        ['smipoly_acryl_22'],
        ['smipoly_acryl_23'],
        ['smipoly_acryl_24'],
        ['smipoly_acryl_25'],
        ['smipoly_acryl_26'],
        ['smipoly_acryl_27'],
        ['smipoly_acryl_28'],
        ['smipoly_acryl_29'],
        ['smipoly_acryl_30'],
        ['smipoly_acryl_31'],
        ['smipoly_acryl_32'],
        ['smipoly_acryl_33'],
        ['smipoly_acryl_34'],
        ['smipoly_acryl_35'],
        ['smipoly_acryl_36'],
        ['smipoly_acryl_37'],
        ['smipoly_acryl_38'],
        ['smipoly_acryl_39'],
        ['smipoly_aliphCH_1'],
        ['smipoly_aliphCH_2'],
        ['smipoly_allyl_1'],
        ['smipoly_allyl_2'],
        ['smipoly_allyl_3'],
        ['smipoly_allyl_4'],
        ['smipoly_allyl_5'],
        ['smipoly_allyl_6'],
        ['smipoly_bEWole_1'],
        ['smipoly_bEWole_2'],
        ['smipoly_bEWole_3'],
        ['smipoly_bEWole_4'],
        ['smipoly_bEWole_5'],
        ['smipoly_bEWole_6'],
        ['smipoly_bEWole_7'],
        ['smipoly_bEWole_8'],
        ['smipoly_bEWole_9'],
        ['smipoly_bEWole_10'],
        ['smipoly_bEWole_11'],
        ['smipoly_bEWole_12'],
        ['smipoly_bEWole_13'],
        ['smipoly_bEWole_14'],
        ['smipoly_bEWole_15'],
        ['smipoly_bEWole_16'],
        ['smipoly_bEWole_17'],
        ['smipoly_bEWole_18'],
        ['smipoly_bEWole_19'],
        ['smipoly_bEWole_20'],
        ['smipoly_bEWole_21'],
        ['smipoly_bEWole_22'],
        ['smipoly_bEWole_23'],
        ['smipoly_bEWole_24'],
        ['smipoly_bEWole_25'],
        ['smipoly_bEWole_26'],
        ['smipoly_bEWole_27'],
        ['smipoly_bEWole_28'],
        ['smipoly_bEWole_29'],
        ['smipoly_bEWole_30'],
        ['smipoly_bEWole_31'],
        ['smipoly_bEWole_32'],
        ['smipoly_bEWole_33'],
        ['smipoly_bEWole_34'],
        ['smipoly_bEWole_35'],
        ['smipoly_bEWole_36'],
        ['smipoly_bEWole_37'],
        ['smipoly_bEWole_38'],
        ['smipoly_bEWole_39'],
        ['smipoly_bEWole_40'],
        ['smipoly_bEWole_41'],
        ['smipoly_bEWole_42'],
        ['smipoly_bEWole_43'],
        ['smipoly_bEWole_44'],
        ['smipoly_bEWole_45'],
        ['smipoly_bEWole_46'],
        ['smipoly_bEWole_47'],
        ['smipoly_bEWole_48'],
        ['smipoly_bEWole_49'],
        ['smipoly_bEWole_50'],
        ['smipoly_bEWole_51'],
        ['smipoly_bEWole_52'],
        ['smipoly_bEWole_53'],
        ['smipoly_bEWole_54'],
        ['smipoly_bEWole_55'],
        ['smipoly_bEWole_56'],
        ['smipoly_bEWole_57'],
        ['smipoly_bEWole_58'],
        ['smipoly_bEWole_59'],
        ['smipoly_bEWole_60'],
        ['smipoly_bEWole_61'],
        ['smipoly_bEWole_62'],
        ['smipoly_bEWole_63'],
        ['smipoly_bEWole_64'],
        ['smipoly_bEWole_65'],
        ['smipoly_bEWole_66'],
        ['smipoly_bEWole_67'],
        ['smipoly_bEWole_68'],
        ['smipoly_bEWole_69'],
        ['smipoly_bEWole_70'],
        ['smipoly_bEWole_71'],
        ['smipoly_bEWole_72'],
        ['smipoly_bEWole_73'],
        ['smipoly_bEWole_74'],
        ['smipoly_bEWole_75'],
        ['smipoly_bEWole_76'],
        ['smipoly_bEWole_77'],
        ['smipoly_bEWole_78'],
        ['smipoly_bEWole_79'],
        ['smipoly_bEWole_80'],
        ['smipoly_bEWole_81'],
        ['smipoly_bEWole_82'],
        ['smipoly_bEWole_83'],
        ['smipoly_bEWole_84'],
        ['smipoly_bEWole_85'],
        ['smipoly_bEWole_86'],
        ['smipoly_bEWole_87'],
        ['smipoly_bEWole_88'],
        ['smipoly_bEWole_89'],
        ['smipoly_bEWole_90'],
        ['smipoly_bEWole_91'],
        ['smipoly_bEWole_92'],
        ['smipoly_bEWole_93'],
        ['smipoly_bEWole_94'],
        ['smipoly_bEWole_95'],
        ['smipoly_bEWole_96'],
        ['smipoly_bEWole_97'],
        ['smipoly_bEWole_98'],
        ['smipoly_bEWole_99'],
        ['smipoly_bEWole_100'],
        ['smipoly_bEWole_101'],
        ['smipoly_bEWole_102'],
        ['smipoly_bEWole_103'],
        ['smipoly_bEWole_104'],
        ['smipoly_bEWole_105'],
        ['smipoly_bEWole_106'],
        ['smipoly_bEWole_107'],
        ['smipoly_bEWole_108'],
        ['smipoly_bEWole_109'],
        ['smipoly_bEWole_110'],
        ['smipoly_bEWole_111'],
        ['smipoly_bEWole_112'],
        ['smipoly_bEWole_113'],
        ['smipoly_bEWole_114'],
        ['smipoly_bEWole_115'],
        ['smipoly_bEWole_116'],
        ['smipoly_bEWole_117'],
        ['smipoly_bEWole_118'],
        ['smipoly_bEWole_119'],
        ['smipoly_bEWole_120'],
        ['smipoly_bEWole_121'],
        ['smipoly_bEWole_122'],
        ['smipoly_bEWole_123'],
        ['smipoly_bEWole_124'],
        ['smipoly_bEWole_125'],
        ['smipoly_bEWole_126'],
        ['smipoly_bEWole_127'],
        ['smipoly_bEWole_128'],
        ['smipoly_bEWole_129'],
        ['smipoly_bEWole_130'],
        ['smipoly_bEWole_131'],
        ['smipoly_bEWole_132'],
        ['smipoly_bEWole_133'],
        ['smipoly_bEWole_134'],
        ['smipoly_bEWole_135'],
        ['smipoly_bEWole_136'],
        ['smipoly_bEWole_137'],
        ['smipoly_bEWole_138'],
        ['smipoly_bEWole_139'],
        ['smipoly_bEWole_140'],
        ['smipoly_bEWole_141'],
        ['smipoly_bEWole_142'],
        ['smipoly_bEWole_143'],
        ['smipoly_bEWole_144'],
        ['smipoly_bEWole_145'],
        ['smipoly_bEWole_146'],
        ['smipoly_bEWole_147'],
        ['smipoly_bEWole_148'],
        ['smipoly_bEWole_149'],
        ['smipoly_bEWole_150'],
        ['smipoly_bEWole_151'],
        ['smipoly_bEWole_152'],
        ['smipoly_bEWole_153'],
        ['smipoly_bEWole_154'],
        ['smipoly_bEWole_155'],
        ['smipoly_bEWole_156'],
        ['smipoly_cOle_1'],
        ['smipoly_cOle_2'],
        ['smipoly_conjdiene_1'],
        ['smipoly_conjdiene_2'],
        ['smipoly_conjdiene_3'],
        ['smipoly_conjdiene_4'],
        ['smipoly_conjdiene_5'],
        ['smipoly_conjdiene_6'],
        ['smipoly_haloCH_1'],
        ['smipoly_haloCH_2'],
        ['smipoly_haloCH_3'],
        ['smipoly_haloCH_4'],
        ['smipoly_haloCH_5'],
        ['smipoly_haloCH_6'],
        ['smipoly_haloCH_7'],
        ['smipoly_haloCH_8'],
        ['smipoly_haloCH_9'],
        ['smipoly_haloCH_10'],
        ['smipoly_malei_1'],
        ['smipoly_malei_2'],
        ['smipoly_styryl_1'],
        ['smipoly_styryl_2'],
        ['smipoly_styryl_3'],
        ['smipoly_styryl_4'],
        ['smipoly_styryl_5'],
        ['smipoly_styryl_6'],
        ['smipoly_styryl_7'],
        ['smipoly_styryl_8'],
        ['smipoly_styryl_9'],
        ['smipoly_styryl_10'],
        ['smipoly_styryl_11'],
        ['smipoly_styryl_12'],
        ['smipoly_styryl_13'],
        ['smipoly_styryl_14'],
        ['smipoly_styryl_15'],
        ['smipoly_styryl_16'],
        ['smipoly_styryl_17'],
        ['smipoly_styryl_18'],
        ['smipoly_styryl_19'],
        ['smipoly_styryl_20'],
        ['smipoly_styryl_21'],
        ['smipoly_styryl_22'],
        ['smipoly_styryl_23'],
        ['smipoly_styryl_24'],
        ['smipoly_styryl_25'],
        ['smipoly_styryl_26'],
        ['smipoly_styryl_27'],
        ['smipoly_styryl_28'],
        ['smipoly_styryl_29'],
        ['smipoly_styryl_30'],
        ['smipoly_styryl_31'],
        ['smipoly_styryl_32'],
        ['smipoly_styryl_33'],
        ['smipoly_styryl_34'],
        ['smipoly_styryl_35'],
        ['smipoly_styryl_36'],
        ['smipoly_styryl_37'],
        ['smipoly_styryl_38'],
        ['smipoly_styryl_39'],
        ['smipoly_styryl_40'],
        ['smipoly_styryl_41'],
        ['smipoly_styryl_42'],
        ['smipoly_styryl_43'],
        ['smipoly_tertcatCH_1'],
        ['smipoly_tertcatCH_2'],
        ['smipoly_vinyl_1'],
        ['smipoly_vinyl_2'],
        ['smipoly_vinyl_3'],
        ['smipoly_vinyl_4'],
        ['smipoly_vinyl_5'],
        ['smipoly_vinyl_6'],
        ['smipoly_vinylester_1'],
        ['smipoly_vinylester_2'],
        ['smipoly_vinylester_3'],
        ['smipoly_vinylester_4'],
        ['smipoly_vinylester_5'],
        ['smipoly_vinylester_6'],
        ['smipoly_vinylether_1'],
        ['smipoly_vinylether_2'],
        ['smipoly_vinylether_3'],
        ['smipoly_vinylether_4'],
        ['smipoly_vinylether_5'],
        ['smipoly_vinylether_6'],
        ['smipoly_vinylether_7'],
        ['smipoly_vinylether_8'],
        ['smipoly_vinylether_9'],
        ['acetylene'],
        ['smipoly_vinyl_1', 'smipoly_vinyl_1'],
        ['smipoly_vinyl_2', 'smipoly_vinyl_2'],
        ['smipoly_vinyl_3', 'smipoly_vinyl_3'],
        ['smipoly_vinyl_4', 'smipoly_vinyl_4'],
        ['smipoly_vinyl_5', 'smipoly_vinyl_5'],
        ['smipoly_vinyl_6', 'smipoly_vinyl_6'],
        ['smipoly_vinyl_1', 'smipoly_cOle_1'],
        ['smipoly_vinyl_1', 'smipoly_cOle_2'],
        ['smipoly_vinyl_2', 'smipoly_cOle_1'],
        ['smipoly_vinyl_2', 'smipoly_cOle_2'],
        ['smipoly_vinyl_3', 'smipoly_cOle_1'],
        ['smipoly_vinyl_3', 'smipoly_cOle_2'],
        ['smipoly_vinyl_4', 'smipoly_cOle_1'],
        ['smipoly_vinyl_4', 'smipoly_cOle_2'],
        ['smipoly_vinyl_5', 'smipoly_cOle_1'],
        ['smipoly_vinyl_5', 'smipoly_cOle_2'],
        ['smipoly_vinyl_6', 'smipoly_cOle_1'],
        ['smipoly_vinyl_6', 'smipoly_cOle_2'],
        ['smipoly_cOle_1', 'smipoly_cOle_1'],
        ['smipoly_cOle_2', 'smipoly_cOle_2'],
    ],
    "chain_growth_ring_opening": [
        ['smipoly_cAnhyd_1'],
        ['smipoly_cAnhyd_2'],
        ['smipoly_epo_1'],
        ['smipoly_epo_2'],
        ['smipoly_epo_3'],
        ['smipoly_epo_4'],
        ['smipoly_epo_5'],
        ['smipoly_lactam_1'],
        ['smipoly_lactam_2'],
        ['smipoly_lactam_3'],
        ['smipoly_lactone_1'],
        ['smipoly_lactone_2'],
        ['smipoly_lactone_3'],
        ['cyclic_ether'],
        ['cyclic_carbonate'],
        ['cyclic_sulfide'],
        ['smipoly_cAnhyd_1', 'smipoly_epo_1'],
        ['smipoly_cAnhyd_1', 'smipoly_epo_2'],
        ['smipoly_cAnhyd_1', 'smipoly_epo_3'],
        ['smipoly_cAnhyd_1', 'smipoly_epo_4'],
        ['smipoly_cAnhyd_1', 'smipoly_epo_5'],
        ['smipoly_cAnhyd_2', 'smipoly_epo_1'],
        ['smipoly_cAnhyd_2', 'smipoly_epo_2'],
        ['smipoly_cAnhyd_2', 'smipoly_epo_3'],
        ['smipoly_cAnhyd_2', 'smipoly_epo_4'],
        ['smipoly_cAnhyd_2', 'smipoly_epo_5'],
    ],
    "metathesis": [
        ['smipoly_cycCH_1'],
        ['terminal_diene'],
        ['conjugated_di_bromide'],
    ],
    "special": [
        ['smipoly_cycCH_1', 'smipoly_aliphCH_1'],
        ['smipoly_cycCH_1', 'smipoly_aliphCH_2'],
    ],
}

# ========== REACTION NUMBER MAPPING ==========
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

    print("\n### SMIPOLY VERSION (with smipoly_ prefix)")
    for mechanism, monomer_sets in smipoly_predefined_mechanism.items():
        print(f"\n{mechanism.upper().replace('_', ' ')}:")
        print(f"  Total combinations: {len(monomer_sets)}")
        for monomers in monomer_sets[:5]:  # Show first 5
            print(f"    - {' + '.join(monomers)}")
        if len(monomer_sets) > 5:
            print(f"    ... and {len(monomer_sets) - 5} more")

    print(f"\nTotal reaction numbers mapped: {len(smipoly_reaction_number_to_mechanism)}")
    print(f"Total monomer classes mapped: {len(smipoly_monomer_to_mechanism)}")
    print(f"Post-polymerization reactions: {len(smipoly_post_polymerization_reactions)}")

    print("\n" + "=" * 60)
    print("### COMPATIBILITY VERSION (without smipoly_ prefix)")
    for mechanism, monomer_sets in predefined_mechanism.items():
        print(f"\n{mechanism.upper().replace('_', ' ')}:")
        print(f"  Total combinations: {len(monomer_sets)}")
        for monomers in monomer_sets[:5]:  # Show first 5
            print(f"    - {' + '.join(monomers)}")
        if len(monomer_sets) > 5:
            print(f"    ... and {len(monomer_sets) - 5} more")
