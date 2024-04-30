import reflex as rx 
from portafolio.components.heading import heading

def about() -> rx.Component:
    return rx.vstack(
        heading("Sobre mi"),
        rx.text("Joven proactivo con habilidades destacadas en atención al detalle, trabajo en equipo y resolución de problemas. Capacidad para aprender rápidamente y adaptarse a entornos cambiantes. Experiencia en desarrollo web y soporte a aplicaciones. Apasionado por mejorar mis habilidades en el desarrollo de software y dispuesto a asumir desafíos para crecer profesionalmente.")
    )