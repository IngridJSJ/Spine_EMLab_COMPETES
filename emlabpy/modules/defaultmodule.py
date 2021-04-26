"""
The parent module class.
This class makes sure there is structure in the commits to the SpineDB.
Inside of every module the staging is done.
At the end of every module, there is a commit.

Jim Hommes - 25-3-2021
"""

from datetime import datetime
from util.repository import Repository


class DefaultModule:

    def __init__(self, name: str, reps: Repository):
        self.name = name
        self.reps = reps

    def act(self):
        pass

    def act_and_commit(self, current_tick: int):
        self.act()
        self.reps.dbrw.commit('Commit: ' + self.name + ' at ' + str(datetime.now()))
