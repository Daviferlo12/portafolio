import reflex as rx 
from portafolio.styles.styles import Size
from portafolio.components.heading import heading
from portafolio.components.media_links import media_links

# DATA JSON
from portafolio.models.data_all import Data


def header(data : Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src= data.avatar,
            size = Size.BIG.value,
            border = "solid 4px",
            border_color = "#00a2c7"
        ),
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display = "inherit"
            ),
            media_links(data.media),
            spacing= Size.SMALL.value
        ),
        spacing= Size.DEFAULT.value
    )