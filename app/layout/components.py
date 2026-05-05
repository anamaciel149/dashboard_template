from dash import html

def create_button(text, id, variant="primary"):
    styles = {
        "primary": "bg-slate-900 text-white shadow-[0_10px_20px_rgba(0,0,0,0.15)] hover:shadow-[0_15px_30px_rgba(0,0,0,0.2)] hover:-translate-y-0.5",
        "ghost-green": "text-emerald-700 bg-emerald-50/30 border border-emerald-100/50 hover:bg-emerald-100/50",
        "ghost-red": "text-rose-700 bg-rose-50/30 border border-rose-100/50 hover:bg-rose-100/50",
        "ghost": "text-slate-400 hover:text-slate-900"
    }

    return html.Button(
        text,
        id=id,
        className=f"""
        {styles[variant]}
        px-8 py-3 rounded-2xl text-[11px] font-black uppercase tracking-[0.2em]
        transition-all duration-500 cubic-bezier(0.4, 0, 0.2, 1)
        active:scale-95
        """
    )

def create_card(children, title=None):
    return html.Div(
        className="""
            bg-white/40 backdrop-blur-xl border border-white/60 
            p-10 rounded-[3rem] shadow-[0_20px_50px_rgba(0,0,0,0.02)]
            hover:shadow-[0_40px_80px_rgba(0,0,0,0.05)] transition-all duration-700
        """,
        children=[
            html.Div(className="flex items-center gap-3 mb-8", children=[
                html.Div(className="w-1.5 h-6 bg-slate-900 rounded-full") if title else None,
                html.H3(title, className="text-slate-900 text-xs font-black uppercase tracking-widest") if title else None,
            ]),
            html.Div(children)
        ]
    )