# Ground Combat constants

combat_result_table = [['1/1R', '1/1', '1/1', '1/1', '1/-', '2/1', '2/1', '2/-',
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

terrain_to_type = {"Flat": 6, "Flat Woods": 6, "Rough": 7, "Rough Woods": 7, "Marsh": 7,
                   "Highlands": 8, "Jungle": 8, "Highland Woods": 8, "Mountain": 9, "Urban": 10}
terrain_to_shift = {"Flat": 4, "Flat Woods": 4, "Rough": 3, "Rough Woods": 3, "Marsh": 3,
                    "Highlands": 2, "Jungle": 2, "Highland Woods": 2, "Mountain": 1, "Urban": 0}
odds_to_column = {'1:3': 1, '1:2': 2, '1:1': 3, '1.5:1': 4, '2:1': 5, '3:1': 6, '4:1': 7,
                  '5:1': 8, '6:1': 9, '7:1': 10, '8:1': 11, '9:1': 12, '10:1': 13}

frac_to_order = {-3: -2, -2: -1, 1: 0, 1.5: 1, 2: 2, 3: 3, 4: 4,
                 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
order_to_frac = {-2: 3, -1: 2, 0: 1, 1: 1.5, 2: 2, 3: 3, 4: 4,
                 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

# SOF constants
raid_result_table = [['1', '1', '-', '-', '-', '-', '-', '-', '-'],
                     ['2', '1', '1', '-', '-', '-', '-', '-', '-'],
                     ['2', '2', '1', '1', '-', '-', '-', '-', '-'],
                     ['X', '2', '2', '1', '1', '-', '-', '-', '-'],
                     ['X', 'X', '2', '2', '1', '1', '-', '-', '-'],
                     ['X', 'X', 'X', '2', '2', '1', '1', '-', '-'],
                     ['X', 'X', 'X', 'X', '2', '2', '1', '1', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-']]

recon_result_table = [['D', 'D', '-', '-', '-', '-', '-', '-', '-'],
                      ['D', 'D', 'D', '-', '-', '-', '-', '-', '-'],
                      ['D', 'D', 'D', 'D', '-', '-', '-', '-', '-'],
                      ['D', 'D', 'D', 'D', 'D', '-', '-', '-', '-'],
                      ['D', 'D', 'D', 'D', 'D', 'D', '-', '-', '-'],
                      ['D', 'D', 'D', 'D', 'D', 'D', 'D', '-', '-']]

targeting_result = ['T', 'T', 'T', 'T', 'T', '-', '-', '-', '-']

detection_result = ['-2', '-2', '-1', '-1', '-1', '-', '-', '-', '-']

terrain_types = ('Flat/Rough/Marsh', 'Flat Woods/Rough Wds',
                 'Highland/Highland Wds', 'Mountain/Urban/Jungle')

recon_types = ('HQ', 'SAM', 'Supply Depot', 'MSU', 'Ground Unit', 'Targeting')

raid_types = ('HQ', 'Supply Depot', 'Interdiction', 'Installation', 'Naval', 'Airfield', 'Helo',
              'MSU', 'Detection/SAM/Theater Weapon')

hq_recon_target = {'Flat/Rough/Marsh': 3, 'Flat Woods/Rough Wds': 2,
                   'Highland/Highland Wds': 1, 'Mountain/Urban/Jungle': 0}
sam_recon_target = {'Flat/Rough/Marsh': 3, 'Flat Woods/Rough Wds': 2,
                    'Highland/Highland Wds': 1, 'Mountain/Urban/Jungle': 0}
depot_recon_target = {'Flat/Rough/Marsh': 4, 'Flat Woods/Rough Wds': 3,
                      'Highland/Highland Wds': 2, 'Mountain/Urban/Jungle': 1}
msu_recon_target = {'Flat/Rough/Marsh': 5, 'Flat Woods/Rough Wds': 4,
                    'Highland/Highland Wds': 3, 'Mountain/Urban/Jungle': 2}
ground_unit_recon_target = {'Flat/Rough/Marsh': 5, 'Flat Woods/Rough Wds': 4,
                            'Highland/Highland Wds': 3, 'Mountain/Urban/Jungle': 2}
recon_table = {'HQ': hq_recon_target, 'SAM': sam_recon_target, 'Supply Depot': depot_recon_target,
               'MSU': msu_recon_target, 'Ground Unit': ground_unit_recon_target}

hq_raid_target = {'Flat/Rough/Marsh': 0, 'Flat Woods/Rough Wds': 1,
                  'Highland/Highland Wds': 2, 'Mountain/Urban/Jungle': 3}
depot_raid_target = {'Flat/Rough/Marsh': 0, 'Flat Woods/Rough Wds': 1,
                     'Highland/Highland Wds': 2, 'Mountain/Urban/Jungle': 3}
msu_raid_target = {'Flat/Rough/Marsh': 3, 'Flat Woods/Rough Wds': 4,
                   'Highland/Highland Wds': 5, 'Mountain/Urban/Jungle': 6}
naval_raid_target = {'Flat/Rough/Marsh': 1, 'Flat Woods/Rough Wds': 2,
                     'Highland/Highland Wds': 3, 'Mountain/Urban/Jungle': 4}
helo_raid_target = {'Flat/Rough/Marsh': 2, 'Flat Woods/Rough Wds': 3,
                    'Highland/Highland Wds': 4, 'Mountain/Urban/Jungle': 5}
airfield_raid_target = {'Flat/Rough/Marsh': 2, 'Flat Woods/Rough Wds': 3,
                        'Highland/Highland Wds': 4, 'Mountain/Urban/Jungle': 5}
installation_raid_target = {'Flat/Rough/Marsh': 1, 'Flat Woods/Rough Wds': 2,
                            'Highland/Highland Wds': 3, 'Mountain/Urban/Jungle': 4}
interdiction_raid_target = {'Flat/Rough/Marsh': 7, 'Flat Woods/Rough Wds': 0,
                            'Highland/Highland Wds': 1, 'Mountain/Urban/Jungle': 2}
raid_table = {'HQ': hq_raid_target, 'Supply Depot': depot_raid_target, 'MSU': msu_raid_target,
              'Naval': naval_raid_target, 'Airfield': airfield_raid_target, 'Helo': helo_raid_target,
              'Installation': installation_raid_target, 'Interdiction': interdiction_raid_target}

# Air Defense constants

detection_to_column = {'Local': 0, '0-1': 1, '2-3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
advanced_detection_table = [['D', 'D', 'D', '-', '-', '-', '-', '-', '-', '-'],
                            ['ED', 'D', 'D', '-', '-', '-', '-', '-', '-', '-'],
                            ['ED', 'D', 'D', 'D', '-', '-', '-', '-', '-', '-'],
                            ['ED', 'ED', 'D', 'D', 'D', '-', '-', '-', '-', '-'],
                            ['ED', 'ED', 'D', 'D', 'D', 'D', '-', '-', '-', '-'],
                            ['ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-', '-', '-'],
                            ['ED', 'ED', 'ED', 'D', 'D', 'D', 'D', 'D', '-', '-'],
                            ['ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-', '-'],
                            ['ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', 'D', '-'],
                            ['ED', 'ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-']]

sam_value_to_column = {'Local': 2, '0-1': 0, '2': 1, '3-4': 2, '5-6': 3, '7': 4, '8': 5, '9': 6, '10': 7}
advanced_sam_table = [['A', '+1', '+1', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['A', '+2', '+1', '+1', '-', '-', '-', '-', '-', '-', '-'],
                      ['X', 'A', '+2', '+1', '+1', '-', '-', '-', '-', '-', '-'],
                      ['X', 'A', 'A', '+2', '+1', '+1', '-', '-', '-', '-', '-'],
                      ['X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-', '-'],
                      ['X', 'X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-'],
                      ['X', 'X', 'A', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-'],
                      ['X', 'X', 'X', 'A', 'A', 'A', '+2', '+2', '+1', '+1', '-']]

aaa_value_to_column = {'Local': 0, '0-1': 0, '2': 1, '3': 2}
advanced_aaa_table = [['+2', '+1', '+1', '-', '-', '-', '-', '-', '-', '-'],
                      ['A', '+2', '+2', '+1', '+1', '-', '-', '-', '-', '-'],
                      ['X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-']]

# Strike constants

attacker_types = ('Air Strike', 'Sup_HQ', 'US_HQ', 'other_HQ', 'Artillery',
                  'Helo 1', 'Helo 2', 'SCUD', 'Cruise', 'Wild Weasel')

target_types = ('Marsh/Flat', 'Rough/Rough Woods/Flat Woods', 'Highland/Highland Woods', 'Mountain',
                'Urban', 'Air Defense Track', 'Hardened Target')

air_strike_target_1 = {'Urban': 9, 'Mountain': 9, 'Highland/Highland Woods': 0,
                       'Rough/Rough Woods/Flat Woods': 1, 'Marsh/Flat': 2, 'Hardened Target': 9,
                       'Air Defense Track': 9}
air_strike_target_2 = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1,
                       'Rough/Rough Woods/Flat Woods': 2, 'Marsh/Flat': 3,
                       'Hardened Target': 0, 'Air Defense Track': 0}
air_strike_target_3 = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2,
                       'Rough/Rough Woods/Flat Woods': 3, 'Marsh/Flat': 4, 'Hardened Target': 1,
                       'Air Defense Track': 1}
air_strike_target_4 = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3,
                       'Rough/Rough Woods/Flat Woods': 4, 'Marsh/Flat': 5, 'Hardened Target': 2,
                       'Air Defense Track': 2}
air_strike_target_5 = {'Urban': 3, 'Mountain': 3, 'Highland/Highland Woods': 4,
                       'Rough/Rough Woods/Flat Woods': 5, 'Marsh/Flat': 6, 'Hardened Target': 3,
                       'Air Defense Track': 3}
air_strike_target_6 = {'Urban': 5, 'Mountain': 5, 'Highland/Highland Woods': 5,
                       'Rough/Rough Woods/Flat Woods': 6, 'Marsh/Flat': 6, 'Hardened Target': 4,
                       'Air Defense Track': 3}
sup_hq_target = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1, 'Rough/Rough Woods/Flat Woods': 2,
                 'Marsh/Flat': 3, 'Hardened Target': 9, 'Air Defense Track': 9}
us_hq_target = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3, 'Rough/Rough Woods/Flat Woods': 4,
                'Marsh/Flat': 5, 'Hardened Target': 9, 'Air Defense Track': 9}
other_hq_target = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2, 'Rough/Rough Woods/Flat Woods': 3,
                   'Marsh/Flat': 4, 'Hardened Target': 9, 'Air Defense Track': 9}
artillery_target = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2, 'Rough/Rough Woods/Flat Woods': 3,
                    'Marsh/Flat': 4, 'Hardened Target': 9, 'Air Defense Track': 9}
helo_2_target = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3, 'Rough/Rough Woods/Flat Woods': 4,
                 'Marsh/Flat': 5, 'Hardened Target': 9, 'Air Defense Track': 9}
helo_1_target = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1, 'Rough/Rough Woods/Flat Woods': 2,
                 'Marsh/Flat': 3, 'Hardened Target': 9, 'Air Defense Track': 9}
scud_target = {'Urban': 3, 'Mountain': 3, 'Highland/Highland Woods': 7, 'Rough/Rough Woods/Flat Woods': 7,
               'Marsh/Flat': 7, 'Hardened Target': 2, 'Air Defense Track': 9}
cruise_target = {'Urban': 4, 'Mountain': 4, 'Highland/Highland Woods': 8, 'Rough/Rough Woods/Flat Woods': 8,
                 'Marsh/Flat': 8, 'Hardened Target': 3, 'Air Defense Track': 2}
wild_weasel_target = {'Urban': 9, 'Mountain': 9, 'Highland/Highland Woods': 9,
                      'Rough/Rough Woods/Flat Woods': 9, 'Marsh/Flat': 9, 'Hardened Target': 9,
                      'Air Defense Track': 4}
strike_table_no_air = {'Sup_HQ': sup_hq_target, 'US_HQ': us_hq_target,
                       'other_HQ': other_hq_target, 'Artillery': artillery_target, 'Helo 1': helo_1_target,
                       'Helo 2': helo_2_target, 'SCUD': scud_target, 'Cruise': cruise_target,
                       'Wild Weasel': wild_weasel_target}
strike_table_air_only = {'1': air_strike_target_1, '2': air_strike_target_2, '3': air_strike_target_3,
                         '4': air_strike_target_4, '5': air_strike_target_5, '6': air_strike_target_6}

air_attacker = ['Air Strike', 'Helo 1', 'Helo 2', 'SCUD', 'Cruise', 'Wild Weasel']

advanced_strike_table = [['Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', '-', '-', '-', '-', '-', '-'],
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

advanced_strike_table_vs_aa = [['-1', '-1', '-1', '-1', '-', '-', '-', '-', '-', '-'],
                               ['-1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-', '-'],
                               ['-2', '-1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-'],
                               ['-2', '-2', '-1', '-1', '-1', '-1', '-1', '-1', '-', '-'],
                               ['-3', '-3', '-2', '-2', '-1', '-1', '-1', '-1', '-1', '-'],
                               ['-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-1', '-'],
                               ['-3', '-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-'],
                               ['-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-', '-'],
                               ['-3', '-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

collateral_damage_table = [['Air', 'AmPt', '-', '-', '-', '-', '-', '-'],
                           ['Air*', 'Air', 'AmPt', '-', '-', '-', '-', '-'],
                           ['Air*', 'Air*', 'Air', 'AmPt', '-', '-', '-', '-'],
                           ['Air AmPt', 'Air AmPt', 'Air', 'Air', '-', '-', '-', '-'],
                           ['Air* Air AmPt', 'Air* AmPt', 'Air AmPt', 'Air', 'Air', '-', '-', '-'],
                           ['Air* Air AmPt', 'Air* Air AmPt', 'Air* AmPt', 'Air AmPt', 'Air', 'Air', 'Air',
                            '-'],
                           ['Step', 'Step', '-', '-', '-', '-', '-', '-'],
                           ['Elim', 'Step', 'Step', '-', '-', '-', '-', '-'],
                           ['Elim', 'Elim', 'Step', 'Step', '-', '-', '-', '-']]

# Air 2 air combat constants


Air_Combat_Result_dogfight = [['X', 'X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-'],
                              ['X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-'],
                              ['X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-'],
                              ['X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-'],
                              ['X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-', '-'],
                              ['X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-'],
                              ['DA', 'DA', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-', '-', '-'],
                              ['DA', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                              ['A', 'D', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

Air_Combat_Result_long = [['X', 'X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-'],
                          ['X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-'],
                          ['X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-'],
                          ['X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-'],
                          ['X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-'],
                          ['X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-'],
                          ['DA', 'DA', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['DA', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['A', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

# cyber warfare constants


mission_to_number = {'UN Resolution': 0, 'Electronic Detection': 1, 'Air Superiority': 2, 'Strike Phase': 3,
                     'Ground Combat': 4}
cyber_warfare_table = [[0, 2, 3, 4, 6, 7, 8, 9], [0, 2, 3, 4, 5, 7, 8, 9], [0, 1, 2, 4, 5, 6, 8, 9],
                       [0, 2, 4, 5, 6, 7, 8, 9], [0, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8]]