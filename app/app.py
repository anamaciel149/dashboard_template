import dash
from dash import html

# Layout principal
from app.layout.main_layout import create_main_layout

# Router (navegação entre páginas)
from app.router.routes import register_routes


def create_app():
    # ------------------------------------------------------------------
    # Inicialização do Dash
    # ------------------------------------------------------------------
    app = dash.Dash(
        __name__,
        suppress_callback_exceptions=True,

        # Scripts externos (opcional)
        external_scripts=[
            {'src': 'https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js'}
        ],
    )

    app.title = "Sistema Global"

    # ------------------------------------------------------------------
    # Template HTML base (substitui o antigo index_string do dashboard.py)
    # ------------------------------------------------------------------
    app.index_string = """
    <!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}

            <!-- Tailwind CSS -->
            <script src="https://cdn.tailwindcss.com"></script>

            <!-- Fonte Inter -->
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

            <style>
                body {
                    font-family: 'Inter', sans-serif;
                    background-color: #f3f4f6;
                }

                .progress-container {
                    transition: opacity 0.3s ease-in-out;
                }

                .progress-bar {
                    transition: width 0.3s ease-in-out;
                }

                .btn-transition {
                    transition: all 0.2s ease-in-out;
                }
            </style>
        </head>

        <body>
            {%app_entry%}

            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
    """

    # ------------------------------------------------------------------
    # Layout principal
    # ------------------------------------------------------------------
    app.layout = create_main_layout()

    # ------------------------------------------------------------------
    # Registro de rotas (páginas)
    # ------------------------------------------------------------------
    register_routes(app)

    # ------------------------------------------------------------------
    # Callbacks globais
    # ------------------------------------------------------------------
    register_global_callbacks(app)

    return app


# ----------------------------------------------------------------------
# CALLBACKS GLOBAIS
# ----------------------------------------------------------------------
def register_global_callbacks(app):
    """
    Aqui entram callbacks que não pertencem a um módulo específico.

    Exemplos futuros:
    - controle global de loading
    - notificações (toast / alert)
    - controle de sidebar (collapse/expand)
    - tracking de navegação
    """
    pass