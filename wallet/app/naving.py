import flet as ft

from wallet.app import colouring


class Navbar(ft.Stack):
    IDENTIFIERS = 0
    CONTACTS = 1
    SETTINGS = 2

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        destinations = [
            ft.NavigationRailDestination(
                icon=ft.icons.DATASET_LINKED,
                selected_icon=ft.icons.DATASET_LINKED_OUTLINED,
                label='Identifiers',
                padding=ft.padding.all(10),
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.PEOPLE),
                selected_icon_content=ft.Icon(ft.icons.PEOPLE_OUTLINE),
                label='Contacts',
                padding=ft.padding.all(10),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text('Settings'),
                padding=ft.padding.all(10),
            ),
        ]

        self.rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            destinations=destinations,
            on_change=self.nav_change,
            expand=True,
        )

    def build(self):
        return self.rail

    async def nav_change(self, e):
        index = e if (type(e) is int) else e.control.selected_index
        self.rail.selected_index = index
        if index == self.IDENTIFIERS:
            self.page.route = '/identifiers'
        elif index == self.CONTACTS:
            self.page.route = '/contacts'
        elif index == self.SETTINGS:
            self.page.route = '/settings'

        await self.page.update_async()
