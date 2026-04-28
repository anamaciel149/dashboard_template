import dash
from dash import html, dcc
from .layout.main_layout import create_main_layout
from .router.routes import register_routes

def create_app():
    app = dash.Dash(__name__, suppress_callback_exceptions=True)

    app.layout = create_main_layout()

    register_routes(app)

    return app