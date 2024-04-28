import reflex as rx 
from portafolio.styles.styles import Size
from portafolio.components.heading import heading
from portafolio.components.media_links import media_links

def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(
            size = Size.BIG.value
        ),
        rx.vstack(
            heading("David Lopez", True),
            heading("Junior Developer"),
            rx.text(
                rx.icon("map-pin"),
                "Bogota, Colombia",
                display = "inherit"
            ),
            media_links(),
            spacing= Size.SMALL.value
        ),
        spacing= Size.DEFAULT.value
    )