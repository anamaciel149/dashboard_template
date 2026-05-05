from dash import html, dcc
from app.layout.sidebar import create_sidebar
from app.layout.header import create_header

def create_main_layout():
    return html.Div(
        className="flex bg-[#F1F5F9] min-h-screen font-sans antialiased", # Fonte suave e fundo clean
        children=[
            create_sidebar(),

            html.Div(
                className="flex-1 p-12 overflow-y-auto",
                children=[
                    create_header("Performance Overview", "Data Intelligence Hub"),

                    html.Div(
                        id='page-content',
                        className="""
                        w-full max-w-7xl mx-auto
                        animate-in fade-in slide-in-from-bottom-4 duration-1000
                        """
                    ),

                    dcc.Location(id='url'),
                    dcc.Store(id='data-refresh-trigger')
                ]
            )
        ]
    )