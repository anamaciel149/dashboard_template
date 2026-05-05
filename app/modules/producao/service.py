import pandas as pd
import numpy as np

def get_data_from_sql_fake(dashboard_key, tipo=None, projeto=None, semana=None):
    # Simulação de Disciplinas de Alto Padrão
    disciplinas = ['RESUMO GERAL', 'MARCOS', 'AUTOMAÇÃO', 'REVESTIMENTOS', 'PAISAGISMO', 'ESTRUTURA']
    data = []
    
    for disc in disciplinas:
        # Gera valores fakes consistentes
        perf_concluido = np.random.uniform(0.3, 0.8)
        perf_previsto = np.random.uniform(0.4, 0.9)
        
        data.append({
            'DISCIPLINA': disc,
            'PROJETO': projeto or "Edifício Unique",
            'SEMANA': semana or 20,
            'PERCENT_CONCLUIDA': perf_concluido,
            'PERCENT_PREV_TAREFA': perf_previsto,
            'PERCENT_EXECUTADO': perf_concluido,
            'PERCENT_PREVISTO': perf_previsto,
            'NOME_DA_TAREFA': projeto if disc == 'RESUMO GERAL' else f"Fase {disc}",
            'TERMINO_REAL': '2026-12-20',
            'TERMINO_BASE': '2026-12-10',
            'INICIO_REAL': '2026-01-01',
            'INICIO_BASE': '2026-01-01',
            'DURACAO_BASE': 300,
            'DURACAO_REAL': 310,
            'LOCAL_DA_TAREFA': 'Torre A',
            'PESOS': 100
        })
    return pd.DataFrame(data)

def get_options_fake():
    return [{'label': 'Alto Padrão', 'value': 'altopadrao'}], [{'label': 'Edifício Unique', 'value': 'Unique'}], [{'label': '20', 'value': 20}]