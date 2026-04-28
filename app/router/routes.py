from dash import html
from dash.dependencies import Input, Output

from app.modules.menu.layout import menu_layout
from app.modules.producao.layout import producao_layout
from app.modules.admin.layout import admin_layout

def register_routes(app):

    @app.callback(
        Output("page-content", "children"),
        Input("url", "pathname")
    )
    def render_page(pathname):

        if pathname == "/producao":
            return producao_layout()

        elif pathname == "/admin":
            return admin_layout()

        else:
            return menu_layout()