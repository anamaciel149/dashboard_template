from dash import html

def admin_layout():
    return html.Div([
        html.H1("Painel de Administração"),
        html.P("Gestão do sistema.")
    ])