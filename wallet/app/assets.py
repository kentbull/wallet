import flet as ft


class Assets:
    def __init__(self):
        self.logo_path = 'keri-swirl.png'
        self._logo_icon = None
        self._logo_splash = None

    @property
    def logo_icon(self):
        if self._logo_icon is None:
            self._logo_icon = ft.Image(src='keri-swirl-transparent-bg.png', width=60)
        return self._logo_icon

    @property
    def logo_splash(self) -> ft.Image:
        if self._logo_splash is None:
            self._logo_splash = ft.Image(src='keri-swirl-transparent-bg.png', width=200)
        return self._logo_splash
