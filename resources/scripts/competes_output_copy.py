"""
This script prepares the COMPETES output files for import by Spine Toolbox.
This means that the most recent output file from COMPETES/Results will be copied to a output file without year,
as defined in Spine Toolbox.

Jim Hommes - 21-6-2021
"""
from spinedb import *
import sys
from shutil import copyfile

print('===== Starting COMPETES Output Preparation script =====')
print('Loading Databases...')
db_emlab = SpineDB(sys.argv[1])

try:
    db_emlab_data = db_emlab.export_data()
    print('Done loading Databases.')

    print('Loading current EM-Lab tick...')
    current_emlab_tick = max(
        [int(i[3]) for i in db_emlab_data['object_parameter_values'] if i[0] == i[1] == 'SystemClockTicks' and
         i[2] == 'ticks'])
    current_competes_tick = 2020 + round(current_emlab_tick / 5) * 5
    print('Current EM-Lab tick is ' + str(current_emlab_tick) +
          ', which translates to COMPETES tick ' + str(current_competes_tick))

    print('Copying files...')
    copyfile('../../COMPETES/Results/Output_Dynamic_Gen&Trans_?.xlsx'.replace('?', str(current_competes_tick)),
             '../../COMPETES/Results/current_Gen&Trans.xlsx')

    print('Done')
except Exception as e:
    print('Exception occurred: ' + str(e))
finally:
    print('Closing database connection...')
    db_emlab.close_connection()
    print('===== End of COMPETES Output Preparation script =====')