import reflex as rx 
from portafolio.components.link_button import link_icon_button
from portafolio.components.icon_badge import icon_badge
from portafolio.styles.styles import Size, IMAGE_HEIGHT, EmSize

# DATA JSON
from portafolio.models.info import Info



def info_detaill(info : Info) -> rx.Component:
    return  rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                rx.cond(
                    info.technologies,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=technology.icon),
                                technology.name,
                                color_scheme="gray"
                            )
                            for technology in info.technologies
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        link_icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        link_icon_button(
                            "github",
                            info.github
                        )
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.cond(
            info.image != "",
            rx.image(
                src=info.image,
                height=IMAGE_HEIGHT,
                width="auto",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover"
            )
        ),
        rx.vstack(
            rx.cond(
                info.date != "",
                rx.badge(info.date)
            ),
            rx.cond(
                info.certificate != "",
                link_icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )