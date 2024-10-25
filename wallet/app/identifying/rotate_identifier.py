"""
rotate_identifier.py
"""

import logging

import flet as ft
from flet_core import FontWeight

from wallet.app.identifying.identifier import IdentifierBase

logger = logging.getLogger('wallet')


class RotateIdentifierPanel(IdentifierBase):
    def __init__(self, app, hab):
        self.app = app
        self.hab = hab

        kever = self.hab.kever

        self.isith = ft.TextField(
            value=kever.tholder.sith,
        )
        self.nsith = ft.TextField(
            value=kever.ntholder.sith,
        )
        self.ncount = ft.TextField(
            value=f'{len(kever.ndigers)}',
        )
        self.toad = ft.TextField(
            value=kever.toader.num,
        )
        super(RotateIdentifierPanel, self).__init__(
            app,
            self.panel(),
            ft.Row(
                controls=[
                    ft.Container(
                        ft.Text(value=f'Alias: {self.hab.name}', size=24),
                        padding=ft.padding.only(10, 0, 10, 0),
                    ),
                    ft.Container(
                        ft.IconButton(icon=ft.icons.CLOSE, on_click=self.cancel),
                        alignment=ft.alignment.top_right,
                        expand=True,
                        padding=ft.padding.only(0, 0, 10, 0),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    async def rotateee(self, _):
        self.hab.rotate(
            isith=self.isith.value,
            nsith=self.nsith.value,
            ncount=int(self.ncount.value),
            toad=self.toad.value,
        )

        if self.hab.delpre:
            self.app.agent.anchors.push(dict(sn=self.hab.kever.sner.num))
            await self.app.snack(f'Rotating {self.hab.pre}, waiting for delegation approval...')

        elif len(self.hab.kever.wits) > 0:
            self.app.agent.witners.push(dict(serder=self.hab.kever.serder))
            await self.app.snack(f'Rotating {self.hab.pre}, waiting for witness receipts...')

        self.app.page.route = '/identifiers'
        await self.app.page.update_async()

    async def cancel(self, _):
        self.app.page.route = '/identifiers'
        await self.app.page.update_async()

    async def back_to_identifier(self, e):
        self.app.page.route = f'/identifiers/{self.hab.pre}/view'
        await self.app.page.update_async()

    def panel(self):
        kever = self.hab.kever

        return ft.Container(
            content=ft.Column(
                [
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.Text('Prefix:', weight=ft.FontWeight.BOLD),
                            ft.Text(self.hab.pre, font_family='monospace'),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Text('Sequence Number:', weight=ft.FontWeight.BOLD, width=175),
                            ft.Text(kever.sner.num),
                        ]
                    ),
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(
                                                'Current signing threshold',
                                                weight=FontWeight.BOLD,
                                                width=175,
                                            ),
                                            self.isith,
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Text(
                                                'Next signing threshold',
                                                weight=FontWeight.BOLD,
                                                width=175,
                                            ),
                                            self.nsith,
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Text(
                                                'Count',
                                                weight=FontWeight.BOLD,
                                                width=175,
                                            ),
                                            self.ncount,
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Text(
                                                'Toad',
                                                weight=FontWeight.BOLD,
                                                width=175,
                                            ),
                                            self.toad,
                                        ]
                                    ),
                                ]
                            ),
                        ]
                    ),
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                'Rotate',
                                on_click=self.rotateee,
                            ),
                            ft.ElevatedButton(
                                'Cancel',
                                on_click=self.cancel,
                            ),
                        ]
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            expand=True,
            alignment=ft.alignment.top_left,
        )
