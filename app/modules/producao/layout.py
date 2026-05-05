import dash
from dash import dcc, html, dash_table

def producao_layout():
    return html.Div(
        className="p-6 bg-slate-50 min-h-screen font-sans",
        children=[
            # CDN do Tailwind para garantir o estilo
            html.Script(src="https://cdn.tailwindcss.com"),
            
            html.H1("Painel Geral - Alto Padrão", className="text-3xl font-extrabold text-blue-900 mb-6"),
            
            html.Div(className="flex flex-col lg:flex-row gap-6", children=[
                # Sidebar de Navegação
                html.Div(className="w-full lg:w-64 flex flex-col gap-2", children=[
                    html.Label("Navegação", className="font-bold text-gray-500 uppercase text-xs"),
                    html.Button("Painel Geral", className="bg-blue-600 text-white p-3 rounded-lg text-left shadow-md"),
                ]),
                
                # Conteúdo Principal
                html.Div(className="flex-1 space-y-6", children=[
                    # Filtros e Tabela
                    html.Div(className="grid grid-cols-1 xl:grid-cols-2 gap-6", children=[
                        html.Div(className="bg-white p-6 rounded-xl shadow-sm border border-gray-100", children=[
                            html.Label("Projeto", className="block text-sm font-medium text-gray-700 mb-1"),
                            dcc.Dropdown(id='filtro-projeto', className="mb-4"),
                            html.Label("Semana", className="block text-sm font-medium text-gray-700 mb-1"),
                            dcc.Dropdown(id='filtro-semana'),
                            
                            html.H3("Acompanhamento por Disciplina", className="text-lg font-bold mt-6 mb-4"),
                            dash_table.DataTable(
                                id='tabela',
                                columns=[
                                    {'name': 'Disciplina', 'id': 'DISCIPLINA'},
                                    {'name': '% Concluída', 'id': 'PERCENT_CONCLUIDA', 'type': 'numeric', 'format': {'specifier': '.2%'}},
                                    {'name': '% Prevista', 'id': 'PERCENT_PREV_TAREFA', 'type': 'numeric', 'format': {'specifier': '.2%'}},
                                ],
                                style_header={'backgroundColor': '#f8fafc', 'fontWeight': 'bold'},
                                style_cell={'padding': '12px', 'fontFamily': 'Inter'}
                            )
                        ]),
                        
                        # KPIs e Gráfico
                        html.Div(className="space-y-6", children=[
                            html.Div(className="grid grid-cols-3 gap-4", children=[
                                html.Div(className="bg-blue-50 p-4 rounded-xl text-center", children=[
                                    html.Div("EXECUTADA", className="text-xs font-bold text-blue-600"),
                                    html.Div(id='executada-display', className="text-2xl font-black text-blue-900")
                                ]),
                                html.Div(className="bg-green-50 p-4 rounded-xl text-center", children=[
                                    html.Div("PREVISTA", className="text-xs font-bold text-green-600"),
                                    html.Div(id='prevista-display', className="text-2xl font-black text-green-900")
                                ]),
                                html.Div(className="bg-purple-50 p-4 rounded-xl text-center", children=[
                                    html.Div("ADERÊNCIA", className="text-xs font-bold text-purple-600"),
                                    html.Div(id='aderencia-display', className="text-2xl font-black text-purple-900")
                                ]),
                            ]),
                            html.Div(className="bg-white p-6 rounded-xl shadow-sm border border-gray-100", children=[
                                dcc.Graph(id='resumo-geral-chart', config={'displayModeBar': False})
                            ])
                        ])
                    ])
                ])
            ]),
            dcc.Store(id='producao-active-sub-dashboard-store', data='painel-geral'),
        ]
    )