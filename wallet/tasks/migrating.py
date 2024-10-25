from keri import kering
from keri.db import basing

from wallet import walleting
from wallet.core.agenting import logger


async def migrate_keystore(name, base, bran):
    """Migrates a keystore from pre v1.1.19 to v1.1.19."""
    migrate(name, base, False)


def migrate(name, base, temp):
    hab_db = basing.Baser(name=name, base=base, temp=temp, reopen=False)
    try:
        hab_db.reopen()
    except kering.DatabaseError:
        pass

    logger.info(f'Migrating {name}...')
    hab_db.migrate()
    logger.info(f'Finished migrating {name}')
    hab_db.close()


async def check_migration(name, base, bran):
    """
    Check if the keystore needs to be migrated from roughly v1.0.0 to v1.1.14.
    """
    hab_db = basing.Baser(name=name, base=base, temp=False, reopen=False)
    try:
        hab_db.reopen()
        logger.info('Migration not needed for %s', name)
    except kering.DatabaseError as ex:
        raise walleting.OldKeystoreError(f'Migration needed for {name}') from ex
    finally:
        hab_db.close()
