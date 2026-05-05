from dash import html, dcc
from app.core.constants import MODULES


def create_sidebar():
    return html.Div(
        className="h-[96vh] w-80 bg-slate-50/50 m-[2vh] rounded-[3.5rem] flex flex-col border border-white p-4",
        children=[

            # HEADER
            html.Div(
                className="pt-12 pb-16 px-8",
                children=[
                    html.H2("CENTRAL", className="text-3xl font-black text-slate-900"),
                    html.P("Engenharia", className="text-[10px] text-slate-400 font-bold uppercase tracking-[0.3em]")
                ]
            ),

            # MENU DINÂMICO
            html.Div(
                className="flex flex-col gap-2 px-4",
                children=[
                    create_nav_item(m["name"], m["route"], m["icon"])
                    for m in MODULES if m["show_in_sidebar"]
                ]
            ),
        ]
    )


def create_nav_item(label, href, index):
    return dcc.Link(
        html.Div(
            className="group flex items-center justify-between px-8 py-4 rounded-[2rem] hover:bg-white hover:shadow-md transition-all duration-500",
            children=[
                html.Span(label, className="text-sm font-bold text-slate-500 group-hover:text-slate-900"),
                html.Span(index, className="text-[10px] font-black text-slate-200 group-hover:text-slate-400")
            ]
        ),
        href=href
    )