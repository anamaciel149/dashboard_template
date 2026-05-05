from dash import html
from app.layout.components import create_button

def create_header(title="Overview", subtitle="Última atualização: Hoje, 12:00"):
    return html.Div(
        className="flex justify-between items-center mb-12",
        children=[
            html.Div([
                html.H1(title, className="text-4xl font-black text-slate-900 tracking-tighter"),
                html.P(subtitle, className="text-xs font-medium text-slate-400 mt-1"),
            ]),

            html.Div(
                className="flex items-center gap-6",
                children=[
                    html.Div(className="h-10 w-[1px] bg-slate-200"), # Divisor vertical elegante
                    create_button("Relatórios", "send-update-email-button", "ghost"),
                    create_button("Atualizar", "force-update-dev-button", "primary"),
                ]
            )
        ]
    )