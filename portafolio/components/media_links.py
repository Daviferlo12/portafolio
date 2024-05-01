import reflex as rx 
from portafolio.components.link_button import link_icon_button
from portafolio.styles.styles import Size

# DATA JSON
from portafolio.models.media import Media

def media_links(data: Media) -> rx.Component:
    return rx.flex(
        link_icon_button(
            "mail",
            f'mailto:{data.email}',
            data.email,
            True
        ),
        rx.hstack(
            link_icon_button(
                "file-text",
                data.cv
            ),
            link_icon_button(
                "github",
                data.github
            ),
            link_icon_button(
                "linkedin",
                data.likedin
            ),
            spacing= Size.SMALL.value
        ),
        spacing= Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )