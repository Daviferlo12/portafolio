import reflex as rx 
from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detaill
from portafolio.styles.styles import Size

# DATA JSON
from portafolio.models.info import Info



def info(title : str, info : list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detaill(item)
                for item in info 
            ],
            spacing= Size.DEFAULT.value,
            width="100%"
        ),
        spacing= Size.DEFAULT.value,
        width="100%"
    )