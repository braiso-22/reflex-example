import reflex as rx


def index() -> rx.Component:
    return rx.box(
        rx.heading(
            "Hello, world!",
            as_="h1",
        ),
        rx.text("This is a test."),
        rx.text("This is another test."),
    )


app = rx.App()
app.add_page(index)
app.compile()
