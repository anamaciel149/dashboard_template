from dash import html, dcc

def create_main_layout():
    return html.Div([
        dcc.Location(id="url"),

        # Navbar simples
        html.Div([
            html.H2("Sistema de Gestão", style={"margin": "10px"}),
            html.Div([
                html.A("Menu", href="/", style={"margin": "10px"}),
                html.A("Produção", href="/producao", style={"margin": "10px"}),
                html.A("Admin", href="/admin", style={"margin": "10px"}),
            ])
        ], style={
            "backgroundColor": "#f5f5f5",
            "padding": "10px",
            "borderBottom": "1px solid #ddd"
        }),

        # Conteúdo dinâmico
        html.Div(id="page-content", style={"padding": "20px"})
    ])