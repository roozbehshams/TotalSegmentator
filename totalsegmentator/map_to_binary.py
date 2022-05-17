
# class_map = {
#     1: "organ_spleen",
#     2: "organ_right_kidney",
#     3: "organ_left_kidney",
#     4: "organ_gallbladder",
#     5: "organ_esophagus",
#     6: "organ_liver",
#     7: "organ_stomach",
#     8: "organ_aorta",
#     9: "organ_inferior_vena_cava",
#     10: "organ_portal_vein_and_splenic_vein",
#     11: "organ_pancreas",
#     12: "organ_right_adrenal_gland",
#     13: "organ_left_adrenal_gland",
# }

# class_map = {
#     1: "humerus_left", 
#     2: "humerus_right", 
#     3: "scapula_left", 
#     4: "scapula_right",
#     5: "clavicula_left", 
#     6: "clavicula_right", 
#     7: "femur_left", 
#     8: "femur_right",
#     9: "hip_left", 
#     10: "hip_right", 
#     11: "sacrum"
# }

class_map = {
    1: "spleen",
    2: "kidney_right",
    3: "kidney_left",
    4: "gallbladder",
    5: "liver",
    6: "stomach",
    7: "aorta",
    8: "inferior_vena_cava",
    9: "portal_vein_and_splenic_vein",
    10: "pancreas",
    11: "adrenal_gland_right",
    12: "adrenal_gland_left",
    13: "lung_upper_lobe_left",
    14: "lung_lower_lobe_left",
    15: "lung_upper_lobe_right",
    16: "lung_middle_lobe_right",
    17: "lung_lower_lobe_right",
    18: "vertebrae_L5",
    19: "vertebrae_L4",
    20: "vertebrae_L3",
    21: "vertebrae_L2",
    22: "vertebrae_L1",
    23: "vertebrae_T12",
    24: "vertebrae_T11",
    25: "vertebrae_T10",
    26: "vertebrae_T9",
    27: "vertebrae_T8",
    28: "vertebrae_T7",
    29: "vertebrae_T6",
    30: "vertebrae_T5",
    31: "vertebrae_T4",
    32: "vertebrae_T3",
    33: "vertebrae_T2",
    34: "vertebrae_T1",
    35: "vertebrae_C7",
    36: "vertebrae_C6",
    37: "vertebrae_C5",
    38: "vertebrae_C4",
    39: "vertebrae_C3",
    40: "vertebrae_C2",
    41: "vertebrae_C1",
    42: "esophagus",
    43: "trachea",
    44: "heart_myocardium",
    45: "heart_atrium_left",
    46: "heart_ventricle_left",
    47: "heart_atrium_right",
    48: "heart_ventricle_right",
    49: "pulmonary_artery",
    50: "brain",
    51: "iliac_artery_left",
    52: "iliac_artery_right",
    53: "iliac_vena_left",
    54: "iliac_vena_right",
    55: "small_bowel",
    56: "duodenum",
    57: "colon",
    58: "rib_left_1",
    59: "rib_left_2",
    60: "rib_left_3",
    61: "rib_left_4",
    62: "rib_left_5",
    63: "rib_left_6",
    64: "rib_left_7",
    65: "rib_left_8",
    66: "rib_left_9",
    67: "rib_left_10",
    68: "rib_left_11",
    69: "rib_left_12",
    70: "rib_right_1",
    71: "rib_right_2",
    72: "rib_right_3",
    73: "rib_right_4",
    74: "rib_right_5",
    75: "rib_right_6",
    76: "rib_right_7",
    77: "rib_right_8",
    78: "rib_right_9",
    79: "rib_right_10",
    80: "rib_right_11",
    81: "rib_right_12",
    82: "humerus_left",
    83: "humerus_right",
    84: "scapula_left",
    85: "scapula_right",
    86: "clavicula_left",
    87: "clavicula_right",
    88: "femur_left",
    89: "femur_right",
    90: "hip_left",
    91: "hip_right",
    92: "sacrum",
    93: "face",
    94: "gluteus_maximus_left",
    95: "gluteus_maximus_right",
    96: "gluteus_medius_left",
    97: "gluteus_medius_right",
    98: "gluteus_minimus_left",
    99: "gluteus_minimus_right",
    100: "autochthon_left",
    101: "autochthon_right",
    102: "iliopsoas_left",
    103: "iliopsoas_right",
    104: "urinary_bladder"
}


class_map_5_parts = {

    # 17 classes
    "class_map_part_organs": {
        1: "spleen",
        2: "kidney_right",
        3: "kidney_left",
        4: "gallbladder",
        5: "liver",
        6: "stomach",
        7: "aorta",
        8: "inferior_vena_cava",
        9: "portal_vein_and_splenic_vein",
        10: "pancreas",
        11: "adrenal_gland_right",
        12: "adrenal_gland_left",
        13: "lung_upper_lobe_left",
        14: "lung_lower_lobe_left",
        15: "lung_upper_lobe_right",
        16: "lung_middle_lobe_right",
        17: "lung_lower_lobe_right"
    },

    # 24 classes
    "class_map_part_vertebrae": {
        1: "vertebrae_L5",
        2: "vertebrae_L4",
        3: "vertebrae_L3",
        4: "vertebrae_L2",
        5: "vertebrae_L1",
        6: "vertebrae_T12",
        7: "vertebrae_T11",
        8: "vertebrae_T10",
        9: "vertebrae_T9",
        10: "vertebrae_T8",
        11: "vertebrae_T7",
        12: "vertebrae_T6",
        13: "vertebrae_T5",
        14: "vertebrae_T4",
        15: "vertebrae_T3",
        16: "vertebrae_T2",
        17: "vertebrae_T1",
        18: "vertebrae_C7",
        19: "vertebrae_C6",
        20: "vertebrae_C5",
        21: "vertebrae_C4",
        22: "vertebrae_C3",
        23: "vertebrae_C2",
        24: "vertebrae_C1"
    },

    # 18
    "class_map_part_cardiac": {
        1: "esophagus",
        2: "trachea",
        3: "heart_myocardium",
        4: "heart_atrium_left",
        5: "heart_ventricle_left",
        6: "heart_atrium_right",
        7: "heart_ventricle_right",
        8: "pulmonary_artery",
        9: "brain",
        10: "iliac_artery_left",
        11: "iliac_artery_right",
        12: "iliac_vena_left",
        13: "iliac_vena_right",
        14: "small_bowel",
        15: "duodenum",
        16: "colon",
        17: "urinary_bladder",
        18: "face"
    },

    # 21
    "class_map_part_muscles": {
        1: "humerus_left",
        2: "humerus_right",
        3: "scapula_left",
        4: "scapula_right",
        5: "clavicula_left",
        6: "clavicula_right",
        7: "femur_left",
        8: "femur_right",
        9: "hip_left",
        10: "hip_right",
        11: "sacrum",
        12: "gluteus_maximus_left",
        13: "gluteus_maximus_right",
        14: "gluteus_medius_left",
        15: "gluteus_medius_right",
        16: "gluteus_minimus_left",
        17: "gluteus_minimus_right",
        18: "autochthon_left",
        19: "autochthon_right",
        20: "iliopsoas_left",
        21: "iliopsoas_right"
    },

    # 24 classes
    # 12. ribs start from vertebrae T12
    # Small subset of population (roughly 8%) have 13. rib below 12. rib
    #  (would start from L1 then)
    #  -> this has label rib_12
    # Even smaller subset (roughly 1%) has extra rib above 1. rib   ("Halsrippe")
    #  (the extra rib would start from C7)
    #  -> this has label rib_1
    #
    # Quite often only 11 ribs (12. ribs probably so small that not found). Those 
    # cases often wrongly segmented. 
    "class_map_part_ribs": {
        1: "rib_left_1",
        2: "rib_left_2",
        3: "rib_left_3",
        4: "rib_left_4",
        5: "rib_left_5",
        6: "rib_left_6",
        7: "rib_left_7",
        8: "rib_left_8",
        9: "rib_left_9",
        10: "rib_left_10",
        11: "rib_left_11",
        12: "rib_left_12",
        13: "rib_right_1",
        14: "rib_right_2",
        15: "rib_right_3",
        16: "rib_right_4",
        17: "rib_right_5",
        18: "rib_right_6",
        19: "rib_right_7",
        20: "rib_right_8",
        21: "rib_right_9",
        22: "rib_right_10",
        23: "rib_right_11",
        24: "rib_right_12"
    }

}

map_taskid_to_partname = {
    251: "class_map_part_organs",
    252: "class_map_part_vertebrae",
    253: "class_map_part_cardiac",
    254: "class_map_part_muscles",
    255: "class_map_part_ribs"
}

# pprint({idx:v for idx, (k, v) in enumerate(a.items())}, sort_dicts=False)
