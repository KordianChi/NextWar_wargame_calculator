# SOF constants
RAID_RESULT_TABLE = [['1', '1', '-', '-', '-', '-', '-', '-', '-'],
                     ['2', '1', '1', '-', '-', '-', '-', '-', '-'],
                     ['2', '2', '1', '1', '-', '-', '-', '-', '-'],
                     ['X', '2', '2', '1', '1', '-', '-', '-', '-'],
                     ['X', 'X', '2', '2', '1', '1', '-', '-', '-'],
                     ['X', 'X', 'X', '2', '2', '1', '1', '-', '-'],
                     ['X', 'X', 'X', 'X', '2', '2', '1', '1', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-']]

RECON_RESULT_TABLE = [['D', 'D', '-', '-', '-', '-', '-', '-', '-'],
                      ['D', 'D', 'D', '-', '-', '-', '-', '-', '-'],
                      ['D', 'D', 'D', 'D', '-', '-', '-', '-', '-'],
                      ['D', 'D', 'D', 'D', 'D', '-', '-', '-', '-'],
                      ['D', 'D', 'D', 'D', 'D', 'D', '-', '-', '-'],
                      ['D', 'D', 'D', 'D', 'D', 'D', 'D', '-', '-']]

TARGETING_RESULT = ['T', 'T', 'T', 'T', 'T', '-', '-', '-', '-']

DETECTION_RESULT = ['-2', '-2', '-1', '-1', '-1', '-', '-', '-', '-']

TERRAIN_TYPES = ('Flat/Rough/Marsh', 'Flat Woods/Rough Wds',
                 'Highland/Highland Wds', 'Mountain/Urban/Jungle')

RECON_TYPES = ('HQ', 'SAM', 'Supply Depot', 'MSU', 'Ground Unit', 'Targeting')

RAID_TYPES = ('HQ', 'Supply Depot', 'Interdiction', 'Installation', 'Naval', 'Airfield', 'Helo',
              'MSU', 'Detection/SAM/Theater Weapon')

HQ_RECON_TARGET = {'Flat/Rough/Marsh': 3, 'Flat Woods/Rough Wds': 2,
                   'Highland/Highland Wds': 1, 'Mountain/Urban/Jungle': 0}
SAM_RECON_TARGET = {'Flat/Rough/Marsh': 3, 'Flat Woods/Rough Wds': 2,
                    'Highland/Highland Wds': 1, 'Mountain/Urban/Jungle': 0}
DEPOT_RECON_TARGET = {'Flat/Rough/Marsh': 4, 'Flat Woods/Rough Wds': 3,
                      'Highland/Highland Wds': 2, 'Mountain/Urban/Jungle': 1}
MSU_RECON_TARGET = {'Flat/Rough/Marsh': 5, 'Flat Woods/Rough Wds': 4,
                    'Highland/Highland Wds': 3, 'Mountain/Urban/Jungle': 2}
GROUND_UNIT_RECON_TARGET = {'Flat/Rough/Marsh': 5, 'Flat Woods/Rough Wds': 4,
                            'Highland/Highland Wds': 3, 'Mountain/Urban/Jungle': 2}
RECON_TABLE = {'HQ': HQ_RECON_TARGET, 'SAM': SAM_RECON_TARGET, 'Supply Depot': DEPOT_RECON_TARGET,
               'MSU': MSU_RECON_TARGET, 'Ground Unit': GROUND_UNIT_RECON_TARGET}

HQ_RAID_TARGET = {'Flat/Rough/Marsh': 0, 'Flat Woods/Rough Wds': 1,
                  'Highland/Highland Wds': 2, 'Mountain/Urban/Jungle': 3}
DEPOT_RAID_TARGET = {'Flat/Rough/Marsh': 0, 'Flat Woods/Rough Wds': 1,
                     'Highland/Highland Wds': 2, 'Mountain/Urban/Jungle': 3}
MSU_RAID_TARGET = {'Flat/Rough/Marsh': 3, 'Flat Woods/Rough Wds': 4,
                   'Highland/Highland Wds': 5, 'Mountain/Urban/Jungle': 6}
NAVAL_RAID_TARGET = {'Flat/Rough/Marsh': 1, 'Flat Woods/Rough Wds': 2,
                     'Highland/Highland Wds': 3, 'Mountain/Urban/Jungle': 4}
HELO_RAID_TARGET = {'Flat/Rough/Marsh': 2, 'Flat Woods/Rough Wds': 3,
                    'Highland/Highland Wds': 4, 'Mountain/Urban/Jungle': 5}
AIRFIELD_RAID_TARGET = {'Flat/Rough/Marsh': 2, 'Flat Woods/Rough Wds': 3,
                        'Highland/Highland Wds': 4, 'Mountain/Urban/Jungle': 5}
INSTALLATION_RAID_TARGET = {'Flat/Rough/Marsh': 1, 'Flat Woods/Rough Wds': 2,
                            'Highland/Highland Wds': 3, 'Mountain/Urban/Jungle': 4}
INTERDICTION_RAID_TARGET = {'Flat/Rough/Marsh': 7, 'Flat Woods/Rough Wds': 0,
                            'Highland/Highland Wds': 1, 'Mountain/Urban/Jungle': 2}
RAID_TABLE = {'HQ': HQ_RAID_TARGET, 'Supply Depot': DEPOT_RAID_TARGET, 'MSU': MSU_RAID_TARGET,
              'Naval': NAVAL_RAID_TARGET, 'Airfield': AIRFIELD_RAID_TARGET, 'Helo': HELO_RAID_TARGET,
              'Installation': INSTALLATION_RAID_TARGET, 'Interdiction': INTERDICTION_RAID_TARGET}

# Air Defense constants

DETECTION_TO_COLUMN = {'Local': 0, '0-1': 1, '2-3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
ADVANCED_DETECTION_TABLE = [['D', 'D', 'D', '-', '-', '-', '-', '-', '-', '-'],
                            ['ED', 'D', 'D', '-', '-', '-', '-', '-', '-', '-'],
                            ['ED', 'D', 'D', 'D', '-', '-', '-', '-', '-', '-'],
                            ['ED', 'ED', 'D', 'D', 'D', '-', '-', '-', '-', '-'],
                            ['ED', 'ED', 'D', 'D', 'D', 'D', '-', '-', '-', '-'],
                            ['ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-', '-', '-'],
                            ['ED', 'ED', 'ED', 'D', 'D', 'D', 'D', 'D', '-', '-'],
                            ['ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-', '-'],
                            ['ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', 'D', '-'],
                            ['ED', 'ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-']]

SAM_VALUE_TO_COLUMN = {'Local': 2, '0-1': 0, '2': 1, '3-4': 2, '5-6': 3, '7': 4, '8': 5, '9': 6, '10': 7}
ADVANCED_SAM_TABLE = [['A', '+1', '+1', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['A', '+2', '+1', '+1', '-', '-', '-', '-', '-', '-', '-'],
                      ['X', 'A', '+2', '+1', '+1', '-', '-', '-', '-', '-', '-'],
                      ['X', 'A', 'A', '+2', '+1', '+1', '-', '-', '-', '-', '-'],
                      ['X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-', '-'],
                      ['X', 'X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-'],
                      ['X', 'X', 'A', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-'],
                      ['X', 'X', 'X', 'A', 'A', 'A', '+2', '+2', '+1', '+1', '-']]

AAA_VALUE_TO_COLUMN = {'Local': 0, '0-1': 0, '2': 1, '3': 2}
ADVANCED_AAA_TABLE = [['+2', '+1', '+1', '-', '-', '-', '-', '-', '-', '-'],
                      ['A', '+2', '+2', '+1', '+1', '-', '-', '-', '-', '-'],
                      ['X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-']]
# Cyber Warfare constants

MISSION_TO_NUMBER = {'UN Resolution': 0, 'Electronic Detection': 1, 'Air Superiority': 2, 'Strike Phase': 3,
                     'Ground Combat': 4}
CYBER_WARFARE_TABLE = [[0, 2, 3, 4, 6, 7, 8, 9], [0, 2, 3, 4, 5, 7, 8, 9], [0, 1, 2, 4, 5, 6, 8, 9],
                       [0, 2, 4, 5, 6, 7, 8, 9], [0, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8]]

# Ground Combat constants

COMBAT_RESULT_TABLE = [['1/1R', '1/1', '1/1', '1/1', '1/-', '2/1', '2/1', '2/-',
                        '1/1', '2/-', '3/1', '3/-', '2/1', '4/-', '4/-', '4/-'],
                       ['1/1R', '1/1R', '1/1', '1/1', '1/1', '1/-', '2/1', '2/1',
                        '2/-', '2/-', '2/1', '3/1', '3/-', '3/-', '2/1', '4/-'],
                       ['-/1R', '1/1R', '1/1R', '1/1', '1/2', '1/1', '1/-', '2/1',
                        '2/1', '2/-', '2/-', '2/-', '3/1', '2/1', '3/-', '4/-'],
                       ['-/1R', '-/1R', '1/1R', '1/1R', '1/1', '1/-', '1/1', '1/-',
                        '2/1', '2/1', '1/1', '2/-', '2/-', '3/1', '2/1', '2/-'],
                       ['-/2R', '-/1R', '-/1R', '1/1R', '1/1R', '1/1', '1/1', '1/1',
                        '1/-', '2/1', '2/1', '2/-', '2/-', '2/-', '3/1', '3/-'],
                       ['/-2R', '1/2R', '-/1', '-/1R', '1/2', '1/1R', '1/1', '1/1',
                        '2/1', '1/-', '2/1', '2/1', '2/-', '1/1', '2/-', '3/1'],
                       ['-/2R', '-/2R', '1/2R', '-/1R', '-/1R', '1/1R', '1/2', '1/1',
                        '1/1', '1/-', '1/-', '2/1', '1/1', '2/-', '2/1', '2/-'],
                       ['-/3R', '-/2R', '-/2R', '1/2R', '-/1', '-/1R', '1/1R', '1/1R',
                        '1/2', '1/1', '1/1', '1/-', '2/1', '1/1', '2/-', '2/1'],
                       ['-/3R', '1/3R', '-/2R', '-/1R', '1/2R', '-/1R', '-/2', '1/1R',
                        '1/1R', '1/1', '1/2', '1/1', '1/-', '1/1', '2/1', '3/1'],
                       ['-/3R', '-/3R', '1/3R', '-/2R', '-/1R', '1/2R', '-/1R', '-/1R',
                        '1/2', '1/1R', '1/1R', '1/1', '2/1', '1/-', '2/1', '1/-'],
                       ['-/4R', '1/3R', '-/3R', '1/3R', '-/2', '-/2R', '1/2R', '-/1',
                        '-/1R', '-/1R', '1/2', '1/1R', '1/1', '1/1', '1/-', '2/1'],
                       ['-/4R', '1/4R', '-/3R', '1/2', '1/3R', '-/2R', '-/2', '1/2R',
                        '-/1R', '1/1', '-/1R', '1/1R', '1/1R', '1/1', '1/1', '2/1'],
                       ['-/4R', '-/4R', '1/4R', '1/3', '-/3R', '1/3R', '-/2', '-/2R',
                        '1/2R', '-/1R', '-/1', '-/1R', '1/1R', '1/1R', '1/-', '2/1']]

TERRAIN_TO_TYPE = {"Flat": 6, "Flat Woods": 6, "Rough": 7, "Rough Woods": 7, "Marsh": 7,
                   "Highlands": 8, "Jungle": 8, "Highland Woods": 8, "Mountain": 9, "Urban": 10}
TERRAIN_TO_SHIFT = {"Flat": 4, "Flat Woods": 4, "Rough": 3, "Rough Woods": 3, "Marsh": 3,
                    "Highlands": 2, "Jungle": 2, "Highland Woods": 2, "Mountain": 1, "Urban": 0}
ODDS_TO_COLUMN = {'1:3': 1, '1:2': 2, '1:1': 3, '1.5:1': 4, '2:1': 5, '3:1': 6, '4:1': 7,
                  '5:1': 8, '6:1': 9, '7:1': 10, '8:1': 11, '9:1': 12, '10:1': 13}

FRAC_TO_ORDER = {-3: -2, -2: -1, 1: 0, 1.5: 1, 2: 2, 3: 3, 4: 4,
                 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
ORDER_TO_FRAC = {-2: 3, -1: 2, 0: 1, 1: 1.5, 2: 2, 3: 3, 4: 4,
                 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
# Air 2 air combat constants

AIR_COMBAT_RESULT_DOGFIGHT = [['X', 'X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-'],
                              ['X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-'],
                              ['X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-'],
                              ['X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-'],
                              ['X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-', '-'],
                              ['X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-'],
                              ['DA', 'DA', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-', '-', '-'],
                              ['DA', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                              ['A', 'D', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

AIR_COMBAT_RESULT_LONG = [['X', 'X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-'],
                          ['X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-'],
                          ['X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-'],
                          ['X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-'],
                          ['X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-'],
                          ['X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-'],
                          ['DA', 'DA', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['DA', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['A', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

# Strike constants

ATTACKER_TYPES = ('Air Strike', 'Sup_HQ', 'US_HQ', 'other_HQ', 'Artillery',
                  'Helo 1', 'Helo 2', 'SCUD', 'Cruise', 'Wild Weasel')

TARGET_TYPES = ('Marsh/Flat', 'Rough/Rough Woods/Flat Woods', 'Highland/Highland Woods', 'Mountain',
                'Urban', 'Air Defense Track', 'Hardened Target')

AIR_STRIKE_TARGET_1 = {'Urban': 9, 'Mountain': 9, 'Highland/Highland Woods': 0,
                       'Rough/Rough Woods/Flat Woods': 1, 'Marsh/Flat': 2, 'Hardened Target': 9,
                       'Air Defense Track': 9}
AIR_STRIKE_TARGET_2 = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1,
                       'Rough/Rough Woods/Flat Woods': 2, 'Marsh/Flat': 3,
                       'Hardened Target': 0, 'Air Defense Track': 0}
AIR_STRIKE_TARGET_3 = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2,
                       'Rough/Rough Woods/Flat Woods': 3, 'Marsh/Flat': 4, 'Hardened Target': 1,
                       'Air Defense Track': 1}
AIR_STRIKE_TARGET_4 = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3,
                       'Rough/Rough Woods/Flat Woods': 4, 'Marsh/Flat': 5, 'Hardened Target': 2,
                       'Air Defense Track': 2}
AIR_STRIKE_TARGET_5 = {'Urban': 3, 'Mountain': 3, 'Highland/Highland Woods': 4,
                       'Rough/Rough Woods/Flat Woods': 5, 'Marsh/Flat': 6, 'Hardened Target': 3,
                       'Air Defense Track': 3}
AIR_STRIKE_TARGET_6 = {'Urban': 5, 'Mountain': 5, 'Highland/Highland Woods': 5,
                       'Rough/Rough Woods/Flat Woods': 6, 'Marsh/Flat': 6, 'Hardened Target': 4,
                       'Air Defense Track': 3}
SUP_HQ_TARGET = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1, 'Rough/Rough Woods/Flat Woods': 2,
                 'Marsh/Flat': 3, 'Hardened Target': 9, 'Air Defense Track': 9}
US_HQ_TARGET = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3, 'Rough/Rough Woods/Flat Woods': 4,
                'Marsh/Flat': 5, 'Hardened Target': 9, 'Air Defense Track': 9}
OTHER_HQ_TARGET = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2, 'Rough/Rough Woods/Flat Woods': 3,
                   'Marsh/Flat': 4, 'Hardened Target': 9, 'Air Defense Track': 9}
ARTILLERY_TARGET = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2, 'Rough/Rough Woods/Flat Woods': 3,
                    'Marsh/Flat': 4, 'Hardened Target': 9, 'Air Defense Track': 9}
HELO_2_TARGET = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3, 'Rough/Rough Woods/Flat Woods': 4,
                 'Marsh/Flat': 5, 'Hardened Target': 9, 'Air Defense Track': 9}
HELO_1_TARGET = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1, 'Rough/Rough Woods/Flat Woods': 2,
                 'Marsh/Flat': 3, 'Hardened Target': 9, 'Air Defense Track': 9}
SCUD_TARGET = {'Urban': 3, 'Mountain': 3, 'Highland/Highland Woods': 7, 'Rough/Rough Woods/Flat Woods': 7,
               'Marsh/Flat': 7, 'Hardened Target': 2, 'Air Defense Track': 9}
CRUISE_TARGET = {'Urban': 4, 'Mountain': 4, 'Highland/Highland Woods': 8, 'Rough/Rough Woods/Flat Woods': 8,
                 'Marsh/Flat': 8, 'Hardened Target': 3, 'Air Defense Track': 2}
WILD_WEASEL_TARGET = {'Urban': 9, 'Mountain': 9, 'Highland/Highland Woods': 9,
                      'Rough/Rough Woods/Flat Woods': 9, 'Marsh/Flat': 9, 'Hardened Target': 9,
                      'Air Defense Track': 4}
STRIKE_TABLE_NO_AIR = {'Sup_HQ': SUP_HQ_TARGET, 'US_HQ': US_HQ_TARGET,
                       'other_HQ': OTHER_HQ_TARGET, 'Artillery': ARTILLERY_TARGET, 'Helo 1': HELO_1_TARGET,
                       'Helo 2': HELO_2_TARGET, 'SCUD': SCUD_TARGET, 'Cruise': CRUISE_TARGET,
                       'Wild Weasel': WILD_WEASEL_TARGET}
STRIKE_TABLE_AIR_ONLY = {'1': AIR_STRIKE_TARGET_1, '2': AIR_STRIKE_TARGET_2, '3': AIR_STRIKE_TARGET_3,
                         '4': AIR_STRIKE_TARGET_4, '5': AIR_STRIKE_TARGET_5, '6': AIR_STRIKE_TARGET_6}

AIR_ATTACKER = ['Air Strike', 'Helo 1', 'Helo 2', 'SCUD', 'Cruise', 'Wild Weasel']

ADVANCED_STRIKE_TABLE = [['Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', '-', '-', '-', '-', '-', '-'],
                         ['Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1',
                          '-', '-', '-', '-'],
                         ['Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1',
                          '-', '-', '-'],
                         ['Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1',
                          'Strike 1', '-', '-'],
                         ['X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1',
                          'Strike 1', '-'],
                         ['X', 'X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1',
                          'Strike 1', '-'],
                         ['X', 'X', 'X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', '-'],
                         ['X', 'X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', '-', '-'],
                         ['X', 'X', 'X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', '-'],
                         ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

ADVANCED_STRIKE_TABLE_VS_AA = [['-1', '-1', '-1', '-1', '-', '-', '-', '-', '-', '-'],
                               ['-1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-', '-'],
                               ['-2', '-1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-'],
                               ['-2', '-2', '-1', '-1', '-1', '-1', '-1', '-1', '-', '-'],
                               ['-3', '-3', '-2', '-2', '-1', '-1', '-1', '-1', '-1', '-'],
                               ['-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-1', '-'],
                               ['-3', '-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-'],
                               ['-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-', '-'],
                               ['-3', '-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

COLLATERAL_DAMAGE_TABLE = [['Air', 'AmPt', '-', '-', '-', '-', '-', '-'],
                           ['Air*', 'Air', 'AmPt', '-', '-', '-', '-', '-'],
                           ['Air*', 'Air*', 'Air', 'AmPt', '-', '-', '-', '-'],
                           ['Air AmPt', 'Air AmPt', 'Air', 'Air', '-', '-', '-', '-'],
                           ['Air* Air AmPt', 'Air* AmPt', 'Air AmPt', 'Air', 'Air', '-', '-', '-'],
                           ['Air* Air AmPt', 'Air* Air AmPt', 'Air* AmPt', 'Air AmPt', 'Air', 'Air', 'Air',
                            '-'],
                           ['Step', 'Step', '-', '-', '-', '-', '-', '-'],
                           ['Elim', 'Step', 'Step', '-', '-', '-', '-', '-'],
                           ['Elim', 'Elim', 'Step', 'Step', '-', '-', '-', '-']]

# Naval Warfare

NAVAL_ATTACK_TYPE_TO_ROW = {'Air 2': 0, 'Air 3': 1, 'Air 4': 2, 'Air 5': 3, 'Air 6': 4, 'SCUD': 2, 'Cruise': 3,
                            'Naval 1': 2, 'Naval 2': 3, 'Naval 3': 4, 'Sub 7': 3, 'Sub 6': 3, 'Sub 5': 2, 'Sub 4': 2}

NAVAL_ATTACK_TYPE = ['Air 2', 'Air 3', 'Air 4', 'Air 5', 'Air 6', 'SCUD', 'Cruise', 'Naval 1', 'Naval 2',
                     'Naval 3', 'Sub 7', 'Sub 6', 'Sub 5', 'Sub 4']

AIR_ADV_SEA = {'-': 0, 'Allied Air Superiority': 1, 'Allied Air Supremacy': 2, 'Non-allied Air Superiority': -1,
               'Non-allied Air Supremacy': -2}