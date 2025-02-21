from fasthtml.common import *

app, rt = fast_app(live=True)


@rt('/')
def get():
    return Titled("Contact Book", Div(
        H1('Hello world XXX'),
        P('This is a paragraph XXX'),
        Button("Click me", onclick="alert('Hello world')")

    )
    )


# serve()
uvicorn.run(app, host="0.0.0.0", port=10000)
