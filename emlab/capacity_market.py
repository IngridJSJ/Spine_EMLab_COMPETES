#
# The Capacity Market recreated from EM-Lab.
#
# Jim Hommes - 17-3-2021
#

import sys
import random
from repository import *
from spinedb import SpineDB

# Input DB
db_url = sys.argv[1]
db = SpineDB(db_url)
db_data = db.export_data()

reps = Repository(db_data)