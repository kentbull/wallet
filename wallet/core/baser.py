import logging

from keri.db import dbing
from keri.db.basing import HabitatRecord, KeyStateRecord

from wallet import walleting
from wallet.core import koming

logger = logging.getLogger('wallet')


class PartialBaser(dbing.LMDBer):
    """
    PartialBaser sets up the minimal version of PartialBaser needed to detect whether a
    database migration is needed.

    It sets up named sub databases with Habs and KERI Event Logs.
    Habs (habs) are required to be able to look state records (stts) up.

    Attributes:
        see superclass LMDBer for inherited attributes

        kevers (dict): Kever instances indexed by identifier prefix qb64
        prefixes (OrderedSet): local prefixes corresponding to habitats for this db

        .habs is named subDB instance of Komer that maps habitat names to habitat
            application state. Includes habitat identifier prefix
            key is habitat name str
            value is serialized HabitatRecord dataclass

        .states (stts) is named subDB instance of SerderSuber that maps a prefix
            to the latest keystate for that prefix. Used by ._kevers.db for read
            through cache of key state to reload kevers in memory


    """

    def __init__(self, headDirPath=None, reopen=False, **kwa):
        """
        Setup named sub databases.

        Parameters:
            name is str directory path name differentiator for main database
                When system employs more than one keri database, name allows
                differentiating each instance by name
            temp is boolean, assign to .temp
                True then open in temporary directory, clear on close
                Othewise then open persistent directory, do not clear on close
            headDirPath is optional str head directory pathname for main database
                If not provided use default .HeadDirpath
            mode is int numeric os dir permissions for database directory
            reopen (bool): True means database will be reopened by this init
        """
        super(PartialBaser, self).__init__(headDirPath=headDirPath, reopen=reopen, **kwa)

    def reopen(self, **kwa):
        """
        Open sub databases

        Notes:

        dupsort=True for sub DB means allow unique (key,pair) duplicates at a key.
        Duplicate means that is more than one value at a key but not a redundant
        copies a (key,value) pair per key. In other words the pair (key,value)
        must be unique both key and value in combination.
        Attempting to put the same (key,value) pair a second time does
        not add another copy.

        Duplicates are inserted in lexiocographic order by value, insertion order.

        """
        super(PartialBaser, self).reopen(**kwa)

        # Create by opening first time named sub DBs within main DB instance
        # Names end with "." as sub DB name must include a non Base64 character
        # to avoid namespace collisions with Base64 identifier prefixes.

        # habitat application state keyed by habitat name, includes prefix
        self.habs = koming.Komer(
            db=self,
            subkey='habs.',
            schema=HabitatRecord,
        )

        # Kever state
        self.nstates = koming.Komer(db=self, subkey='stts.', schema=KeyStateRecord)
        self.states = koming.Komer(db=self, subkey='stts.', schema=dict)

        return self.env

    def check_migration_state(self):
        """
        Reload stored prefixes and Kevers from .habs

        """
        for keys, data in self.habs.getItemIter():
            # will raise an OldKeystoreError if the keystore is old, as in has a
            # "dict" type instead of a KeyStateRecord type for the stts sub DB.
            try:
                self.nstates.get_expect_type(
                    keys=data.hid, klas=KeyStateRecord
                )  # This will not raise an error if the keystore is current
                return  # If no error, we're done
            except walleting.OldKeystoreError:
                self.states.get_expect_type(
                    keys=data.hid, klas=KeyStateRecord
                )  # This will raise the error if the keystore is old
