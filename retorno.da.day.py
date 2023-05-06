retorno_dia = dados_fechamento.pct_change().dropna()
retorno_mes = dados_fechamento_mensal.pct_change().dropna()
retorno_ano = dados_fechamento_anual.pct_change().dropna()

retorno_dia.head()