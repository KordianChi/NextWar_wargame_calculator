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