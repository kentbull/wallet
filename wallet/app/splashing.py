import flet as ft

from wallet.app import colouring
from wallet.app.assets import Assets


class Splash(ft.Column):
    def __init__(self, app):
        self.app = app

        super(Splash, self).__init__(
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                Assets().logo_splash,
                                expand=True,
                            )
                        ],
                    ),
                    padding=ft.padding.only(0, -100, 0, 0),
                    alignment=ft.alignment.center,
                    expand=True,
                )
            ],
            spacing=25,
            expand=True,
        )

    def did_mount(self):
        self.page.run_task(self.app.toggle_drawer, None)
