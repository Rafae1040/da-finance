# Análise de Fechamento do Mercado Financeiro



## Introdução: 

----


### Objetivo:

O objetivo deste projeto é fornecer aos usuários uma análise detalhada do fechamento do mercado financeiro em um determinado dia, mês e ano. Com essa análise, os usuários poderão obter insights valiosos sobre a performance da ação, índice ou ETF selecionado.

Além disso, o projeto envia automaticamente um relatório detalhado para o diretor, permitindo que ele fique informado sobre o desempenho dos ativos financeiros e tome decisões estratégicas com base nos insights fornecidos.

Com este projeto, você terá uma ferramenta poderosa para analisar o mercado financeiro e manter sua equipe atualizada sobre as tendências e desempenhos do mercado.

### Benefícios:
Os principais benefícios são:

* Análise detalhada do fechamento do mercado financeiro em um determinado dia, mês e ano;
* Insights valiosos sobre o desempenho da ação, índice ou ETF selecionado;
* Envio automático de relatórios detalhados para o diretor;
* Ferramenta poderosa para analisar o mercado financeiro e tomar decisões estratégicas informadas.

Com esses benefícios, este projeto é uma ferramenta essencial para investidores, analistas financeiros e gerentes de investimentos que buscam uma maneira eficiente de analisar o mercado financeiro e tomar decisões informadas com base nos dados.

---

## Metodologia:

Para a obtenção dos dados foi a coleta de informações no Yahoo Finance, por meio da biblioteca yfinance do Python. Os dados foram manipulados por meio da biblioteca Pandas, permitindo a seleção e exclusão de informações relevantes, bem como a criação de tabelas com outros timeframes, como o fechamento mensal e anual.

O código também inclui a localização do fechamento do dia anterior, bem como o cálculo dos retornos do mês e do ano dos ativos. Essas informações são importantes para investidores, corretoras, gerentes financeiros e qualquer pessoa interessada em monitorar a performance desses ativos.

Por fim, o projeto inclui a geração de gráficos que mostram a performance dos ativos no último ano. A estética desses gráficos foi configurada com o estilo cyberpunk, fornecido pela biblioteca mplcyberpunk do Python. Além disso, o código também inclui o envio automático de um relatório para um destinatário via e-mail.

---

## Conclusão:

O projeto oferece uma análise completa e automatizada do fechamento do mercado financeiro do índice Bovespa e da cotação do dólar em relação ao real, com informações úteis para investidores, corretoras, gerentes financeiros e outras pessoas interessadas em acompanhar a performance desses ativos.

No final de todo o processo foi enviado o e-mail para o diretor e constou o seguinte resultado:

Bolsa:

No ano Ibovespa está tendo uma rentabilidade de -5.4%,
enquanto no mês a rentabilidade é de 0.13%.

No último dia útil, o fechamento do ibovespa foi de -0.24%

Dólar:

No ano o Dólar está tendo uma rentabilidade de -4.44%,
enquanto no mês a rentabilidade é de 0.69%.

No último dia útil, o fechamento do Dólar foi de 2.91%.

