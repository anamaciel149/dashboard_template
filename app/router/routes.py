from dash import html
from dash.dependencies import Input, Output

from app.modules.menu.layout import menu_layout
from app.modules.producao.layout import producao_layout
from app.modules.admin.layout import admin_layout

from dash import Input, Output
from app.core.constants import MODULES

MODULE_LAYOUTS = {
    "admin": admin_layout,
    "producao": producao_layout,
    "menu": menu_layout
}


def register_routes(app):

    @app.callback(
        Output("page-content", "children"),
        Input("url", "pathname")
    )
    def render_page(pathname):

        for module in MODULES:
            if pathname == module["route"]:
                return MODULE_LAYOUTS.get(module["key"], "Página não encontrada")

        return "Página não encontrada"