import flet as ft


class Colouring:
    PRIMARY = 'primary'
    ON_PRIMARY = 'on_primary'
    SECONDARY = 'secondary'
    ON_SECONDARY = 'on_secondary'
    SURFACE = 'surface'
    ON_SURFACE = 'on_surface'
    BACKGROUND = 'background'
    ON_BACKGROUND = 'on_background'
    RED = 'red'

    # Class-level variable to store the theme mode
    _theme_mode = None

    class Light(ft.Theme):
        RED = '#b00020'
        PRIMARY = '#61783e'
        ON_PRIMARY = '#ffffff'
        SECONDARY = '#a1c64d'
        ON_SECONDARY = '#000000'
        SURFACE = '#f5f5f5'
        BACKGROUND = '#ffffff'
        ON_BACKGROUND = '#000000'
        ON_SURFACE = '#000000'

        def __init__(self):
            super().__init__(
                primary_color=self.PRIMARY,
                color_scheme=ft.ColorScheme(
                    primary=self.PRIMARY,
                    on_primary=self.ON_PRIMARY,
                    secondary=self.SECONDARY,
                    on_secondary=self.ON_SECONDARY,
                    surface=self.SURFACE,
                    on_surface=self.ON_SURFACE,
                    background=self.BACKGROUND,
                    on_background=self.ON_BACKGROUND,
                ),
            )

        class FloatingActionButtonTheme(ft.FloatingActionButtonTheme):
            def __init__(self):
                super().__init__(
                    bgcolor='#61783e',
                    foreground_color='#ffffff',
                )

    class Dark(ft.Theme):
        RED = '#b00020'
        PRIMARY = '#b4d070'
        ON_PRIMARY = '#000000'
        SECONDARY = '#819f49'
        ON_SECONDARY = '#ffffff'
        SURFACE = '#1e1e1e'
        BACKGROUND = '#121212'
        ON_BACKGROUND = '#ffffff'
        ON_SURFACE = '#ffffff'

        def __init__(self):
            super().__init__(
                primary_color=self.PRIMARY,
                color_scheme=ft.ColorScheme(
                    primary=self.PRIMARY,
                    on_primary=self.ON_PRIMARY,
                    secondary=self.SECONDARY,
                    on_secondary=self.ON_SECONDARY,
                    surface=self.SURFACE,
                    on_surface=self.ON_SURFACE,
                    background=self.BACKGROUND,
                    on_background=self.ON_BACKGROUND,
                ),
            )

        class FloatingActionButtonTheme(ft.FloatingActionButtonTheme):
            def __init__(self):
                super().__init__(
                    bgcolor='#b4d070',
                    foreground_color='#000000',
                )

    @classmethod
    def set_theme(cls, theme_mode):
        if theme_mode in [ft.Brightness.LIGHT.name, ft.Brightness.DARK.name]:
            cls._theme_mode = theme_mode
        else:
            raise ValueError("Theme mode must be ft.Brightness.LIGHT.name or 'dark'")

    @classmethod
    def get(cls, color):
        """Get the color based on the set theme mode."""
        if cls._theme_mode is None:
            raise Exception("Theme mode is not set. Use 'set_theme' to set it first.")

        match color:
            case cls.PRIMARY:
                return cls.Light.PRIMARY if cls._theme_mode == ft.Brightness.LIGHT.name else cls.Dark.PRIMARY
            case cls.ON_PRIMARY:
                return cls.Light.ON_PRIMARY if cls._theme_mode == ft.Brightness.LIGHT.name else cls.Dark.ON_PRIMARY
            case cls.SECONDARY:
                return cls.Light.SECONDARY if cls._theme_mode == ft.Brightness.LIGHT.name else cls.Dark.SECONDARY
            case cls.ON_SECONDARY:
                return cls.Light.ON_SECONDARY if cls._theme_mode == ft.Brightness.LIGHT.name else cls.Dark.ON_SECONDARY
            case cls.SURFACE:
                return cls.Light.SURFACE if cls._theme_mode == ft.Brightness.LIGHT.name else cls.Dark.SURFACE
            case cls.ON_SURFACE:
                return cls.Light.ON_SURFACE if cls._theme_mode == ft.Brightness.LIGHT.name else cls.Dark.ON_SURFACE
            case cls.BACKGROUND:
                return cls.Light.BACKGROUND if cls._theme_mode == ft.Brightness.LIGHT.name else cls.Dark.BACKGROUND
            case cls.ON_BACKGROUND:
                return cls.Light.ON_BACKGROUND if cls._theme_mode == ft.Brightness.LIGHT.name else cls.Dark.ON_BACKGROUND
            case cls.RED:
                return '#b00020'
            case _:
                return '#000000'
