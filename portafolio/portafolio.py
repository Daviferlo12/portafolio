import reflex as rx
from portafolio.styles.styles import STYLESHEETS, BASE_STYLE, Size,MAX_WIDTH, EmSize
from portafolio.views.header import header
from portafolio.views.about import about
from portafolio.views.tech_stack import tech_stack
from portafolio.views.info import info
from portafolio.views.extra import extra
from portafolio.views.footer import footer

# DATA JSON
from portafolio.models.data_all import data


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(data),
            about(data.about),
            rx.divider(),
            tech_stack(data.technologies),
            info("Experiencia", data.experience),
            info("Proyectos", data.projects),
            info("Formacion", data.training),
            extra(data.extras),
            rx.divider(),
            footer(data.media),
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
        accent_color="cyan",
        radius="full"
    )
)
app.add_page(
        index,
        title= data.title,
        description= data.description,
        image= data.image,
        meta=[
            {"name": "og:title", "content": data.title},
            {"name": "og:description", "content": data.description},
            {"name": "og:image", "content": data.image}
        ]
    )
