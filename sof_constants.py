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