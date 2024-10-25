from typing import List

from keri.app.cli.commands.multisig.rotate import GroupMultisigRotate
from keri.app.habbing import Habery

from wallet.core.agenting import run_hio_task


async def multisig_rotate(
    hby: Habery,
    alias: str,
    smids: List[str] | None,
    rmids: List[str] | None,
    wits: List[str] | None,
    cuts: List[str] | None,
    adds: List[str] | None,
    isith: int | str,
    nsith: int | str,
    toad: int | str,
    data: List[dict] | None,
):
    """Rotates a multisig identifier."""
    rot_doer = GroupMultisigRotate(
        hby=hby,
        alias=alias,
        smids=smids,
        rmids=rmids,
        wits=wits,
        cuts=cuts,
        adds=adds,
        isith=isith,
        nsith=nsith,
        toad=toad,
        data=data,
    )
    await run_hio_task([rot_doer])
