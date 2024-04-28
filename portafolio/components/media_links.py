import reflex as rx 
from portafolio.components.link_button import link_icon_button
from portafolio.styles.styles import Size
import portafolio.constanst as constant

def media_links() -> rx.Component:
    return rx.flex(
        link_icon_button(
            "mail",
            f'mailto:{constant.EMAIL}',
            constant.EMAIL,
            True
        ),
        rx.hstack(
            link_icon_button(
                "file-text",
                constant.CV
            ),
            link_icon_button(
                "github",
                constant.GITHUB
            ),
            link_icon_button(
                "linkedin",
                constant.LINKEDIN
            ),
            spacing= Size.SMALL.value
        ),
        spacing= Size.SMALL.value
    )