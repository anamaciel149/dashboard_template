import pandas as pd
from dash import Output, Input, callback
import plotly.express as px
from .service import get_data_from_sql_fake, get_options_fake

def cria_style_bar(column_id, color):
    """Sua função original para as barrinhas coloridas na tabela."""
    return [{
        'if': {'filter_query': f'{{{column_id}}} >= {i/100} && {{{column_id}}} < {(i+5)/100}', 'column_id': column_id},
        'background': f"linear-gradient(90deg, {color} {i}%, transparent {i}%)", 'color': 'black'
    } for i in range(0, 101, 5)]

@callback(
    [Output('filtro-projeto', 'options'), Output('filtro-projeto', 'value'),
     Output('filtro-semana', 'options'), Output('filtro-semana', 'value')],
    [Input('producao-active-sub-dashboard-store', 'data')]
)
def iniciar_filtros(_):
    _, proj, sem = get_options_fake()
    return proj, proj[0]['value'], sem, sem[0]['value']

@callback(
    [Output('tabela', 'data'),
     Output('tabela', 'style_data_conditional'),
     Output('executada-display', 'children'),
     Output('prevista-display', 'children'),
     Output('aderencia-display', 'children'),
     Output('resumo-geral-chart', 'figure')],
    [Input('filtro-projeto', 'value'),
     Input('filtro-semana', 'value')]
)
def atualizar_dashboard(projeto, semana):
    df = get_data_from_sql_fake('altopadrao', projeto=projeto, semana=semana)
    
    resumo = df[df['DISCIPLINA'] == 'RESUMO GERAL'].iloc[0]
    executada = resumo['PERCENT_EXECUTADO']
    prevista = resumo['PERCENT_PREVISTO']
    aderencia = executada / prevista if prevista > 0 else 0
    
    # Estilos de barra
    estilos = cria_style_bar('PERCENT_CONCLUIDA', '#bae6fd') + cria_style_bar('PERCENT_PREV_TAREFA', '#bbf7d0')
    
    # Gráfico
    chart_df = pd.DataFrame({
        'Métrica': ['EXECUTADO', 'PREVISTO'],
        'Valor': [executada, prevista],
        'Cor': ['#1e40af', '#166534']
    })
    fig = px.bar(chart_df, x='Valor', y='Métrica', orientation='h', text_auto='.2%',
                 color='Métrica', color_discrete_sequence=['#1e40af', '#166534'])
    fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=0, b=0), height=200)
    
    table_data = df[df['DISCIPLINA'] != 'RESUMO GERAL'].to_dict('records')
    
    return table_data, estilos, f"{executada:.1%}", f"{prevista:.1%}", f"{aderencia:.1%}", fig