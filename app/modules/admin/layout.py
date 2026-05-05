from app.layout.components import create_card, create_button
from dash import html, dcc, dash_table
from app.core.constants import ALL_PAGES_OPTIONS

admin_layout = html.Div(
    className="flex flex-col gap-10",

    children=[

        # -------------------------------
        # TÍTULO
        # -------------------------------
        html.Div([
            html.H1("Administração", className="text-3xl font-black text-slate-900"),
            html.P("Gestão de usuários e permissões", className="text-sm text-slate-400")
        ]),

        # -------------------------------
        # TABELA DE USUÁRIOS
        # -------------------------------
        create_card(

            children=[

                dash_table.DataTable(
                    id='admin-user-table',

                    columns=[
                        {'name': 'ID', 'id': 'id'},
                        {'name': 'Usuário', 'id': 'username'},
                        {'name': 'Acessos', 'id': 'pages_access_display'},
                        {'name': 'Ações', 'id': 'actions', 'presentation': 'markdown'}
                    ],

                    data=[],
                    row_selectable='single',
                    selected_rows=[],

                    style_table={
                        'overflowX': 'auto',
                        'borderRadius': '20px'
                    },

                    style_cell={
                        'fontFamily': 'Inter',
                        'fontSize': 12,
                        'padding': '12px',
                        'border': 'none'
                    },

                    style_header={
                        'backgroundColor': 'transparent',
                        'fontWeight': 'bold',
                        'color': '#64748b',
                        'borderBottom': '1px solid #e2e8f0'
                    },

                    style_data_conditional=[
                        {
                            'if': {'row_index': 'odd'},
                            'backgroundColor': '#f8fafc'
                        },
                        {
                            'if': {'state': 'selected'},
                            'backgroundColor': '#e0f2fe',
                            'border': 'none'
                        },
                    ]
                )
            ],

            title="Usuários"
        ),

        # -------------------------------
        # CRIAR USUÁRIO
        # -------------------------------
        create_card(

            children=[

                html.Div(className="grid grid-cols-3 gap-6", children=[

                    # USERNAME
                    html.Div([
                        html.Label("Usuário", className="text-xs font-bold text-slate-400 uppercase"),
                        dcc.Input(
                            id='admin-new-username-input',
                            placeholder='Nome de usuário',
                            className="w-full mt-2 p-3 rounded-xl border border-slate-200 text-sm"
                        )
                    ]),

                    # SENHA
                    html.Div([
                        html.Label("Senha", className="text-xs font-bold text-slate-400 uppercase"),
                        dcc.Input(
                            id='admin-new-password-input',
                            type='password',
                            placeholder='Senha',
                            className="w-full mt-2 p-3 rounded-xl border border-slate-200 text-sm"
                        )
                    ]),

                    # PERMISSÕES
                    html.Div([
                        html.Label("Permissões", className="text-xs font-bold text-slate-400 uppercase"),
                        dcc.Dropdown(
                            id='admin-new-pages-access',
                            options=ALL_PAGES_OPTIONS,
                            multi=True,
                            placeholder="Selecionar",
                            className="mt-2"
                        )
                    ]),
                ]),

                html.Div(className="mt-6 flex justify-end", children=[
                    create_button("Criar usuário", "admin-create-user-button", "primary")
                ]),

                html.Div(id='admin-register-status', className="mt-4 text-sm")

            ],

            title="Novo usuário"
        ),

        # -------------------------------
        # STORES (mantém lógica)
        # -------------------------------
        dcc.Store(id='admin-table-refresh-store', data=0),
        dcc.Store(id='permissions-to-save-store', data={}),
        dcc.Store(id='selected-user-id-store', data=None)
    ]
)