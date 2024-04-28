import reflex as rx
from portafolio.styles.styles import STYLESHEETS, BASE_STYLE, Size,MAX_WIDTH, EmSize
from portafolio.views.header import header

class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="teal",
        radius="full"
    )
)
app.add_page(index)
