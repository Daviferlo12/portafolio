import reflex as rx 
from portafolio.components.media_links import media_links
from portafolio.styles.styles import Size

#DATA JSON
from portafolio.models.media import Media

def footer(data : Media) -> rx.Component:
    return rx.vstack(
        rx.text("Contacto"),
        media_links(data),
        spacing= Size.SMALL.value
    )