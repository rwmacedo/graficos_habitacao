# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import streamlit as st
import plotly.express as px
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt


pd.options.display.float_format = '{:.2f}'.format # show only two digits

## Bases de dados
df_total= pd.read_csv('df_total.csv')
df_deflacionada= pd.read_csv('df_deflacionada.csv')
df_por_renda= pd.read_csv('df_por_renda.csv')
df_por_faixa= pd.read_csv('df_por_faixa.csv')
df_porte_sup15= pd.read_csv('df_porte_sup15.csv')
df_sup15_faixa= pd.read_csv('df_sup15_faixa.csv')
df_ocupacao= pd.read_csv('df_ocupacao.csv')
df_tcb= pd.read_csv('df_tcb.csv')
df_sr= pd.read_csv('df_sr.csv')
df_regiao= pd.read_csv('df_regiao.csv')
df_contratacao= pd.read_csv('df_contratacao.csv')
df_ifdata= pd.read_csv('df_ifdata.csv')
df_percentual_instituicao= pd.read_csv('df_percentual_instituicao.csv')
df_funding=pd.read_csv('df_funding.csv')
df_sup15_ocupacao= pd.read_csv('df_sup15_ocupacao.csv')
df_sup15_regiao= pd.read_csv('df_sup15_regiao.csv')
        
##  Graficos
fig01 = px.line(df_total, x="data_base", y= 'carteira_ativa', title="Carteira Ativa")
fig02 = px.line(df_total, x="data_base", y= 'carteira_inadimplida_arrastada', title="Carteira Inadimplida Arrastada")
fig03 = px.line(df_deflacionada, x="data_base", y= 'carteira_ativa_deflacionada', title="Carteira Ativa Deflacionada")
fig04 = px.line(df_deflacionada, x="data_base", y= 'carteira_inadimplida_arrastada_deflacionada', title="Carteira Inadimplida Arrastada Deflacionada")
fig05 = px.line(df_deflacionada, x="data_base", y= 'inadimplencia', title="Inadimplencia Percentual")
fig06 = px.line(df_por_renda, x="data_base", y="carteira_ativa", color='renda', title="Carteira Ativa Por Renda")
fig07 = px.line(df_por_renda, x="data_base", y="inadimplencia", color='renda', title="Inadimplencia por Renda")
fig08 = px.line(df_porte_sup15, x="data_base", y="ticket_medio", color='renda', title="Ticket Medio por Renda")
fig09 = px.line(df_ocupacao, x="data_base", y="carteira_ativa", color='ocupacao', title="Carteira Ativa por ocupação")
fig10 = px.line(df_ocupacao, x="data_base", y="carteira_inadimplida_arrastada", color='ocupacao', title="Carteira inadimplida por ocupação")
fig11 = px.line(df_ocupacao, x="data_base", y="inadimplencia", color='ocupacao', title="Inadimplencia percentual por ocupação")
fig12 = px.line(df_regiao, x="data_base", y="carteira_ativa", color='regiao', title="Carteira Ativa por Região")
fig13 = px.line(df_regiao, x="data_base", y="carteira_inadimplida_arrastada", color='regiao', title="Carteira Inadimplida por Região")
fig14 = px.line(df_regiao, x="data_base", y="inadimplencia", color='regiao', title="Inadimplencia por Região")

fig15 = px.line(df_contratacao,
              x='Data', 
              y=['credito_contratacao_contratado_pf_comercial_br', 'credito_contratacao_contratado_pf_fgts_br',
                 'credito_contratacao_contratado_pf_home_equity_br', 'credito_contratacao_contratado_pf_livre_br',  'credito_contratacao_contratado_pf_sfh_br'],
              labels={'value':'Valor', 'variable':'Categorias'},
              title='Evolução do Crédito de Contratação por Tipo')
fig16 = px.line(df_contratacao, x="Data", y= 'contratacao_pf_total', title="Total de Contratação Habitacional PF")

fig17 = px.line(df_contratacao,
                x='Data', 
              y=['credito_contratacao_taxa_pf_comercial_br',
                 'credito_contratacao_taxa_pf_fgts_br',
                 'credito_contratacao_taxa_pf_home_equity_br',
                 'credito_contratacao_taxa_pf_livre_br',
                 'credito_contratacao_taxa_pf_sfh_br',              
                 'indices_selic_br'],
              labels={'value':'Valor', 'variable':'Categorias'},
              title='Evolução da taxa de Juros')
fig18 =px.line(df_funding,
              x='ano', 
              y=['fontes_cri_br', 'fontes_lci_br', 'fontes_lh_br', 'fontes_lig_br', 'fontes_sbpe_saldo_br', 'fgts'],
                labels={'value':'Valor', 'variable':'Categorias'},
              title='Evolução das Fontes de recursos')
fig19 = px.line(df_contratacao,
              x='Data', 
              y=['credito_estoque_carteira_credito_pf_comercial_br',
                 'credito_estoque_carteira_credito_pf_fgts_br',
                 'credito_estoque_carteira_credito_pf_home_equity_br',
                 'credito_estoque_carteira_credito_pf_livre_br',
                 'credito_estoque_carteira_credito_pf_sfh_br'],
              labels={'value':'Valor', 'variable':'Categorias'},
              title='Estoque Carteira Ativa por tipo')
fig20 = px.line(df_contratacao,
              x='Data', 
              y=['credito_estoque_inadimplencia_pf_comercial_br',
                 'credito_estoque_inadimplencia_pf_fgts_br',
                 'credito_estoque_inadimplencia_pf_home_equity_br',
                 'credito_estoque_inadimplencia_pf_livre_br',
                 'credito_estoque_inadimplencia_pf_sfh_br'],
              labels={'value':'Percentual', 'variable':'Categorias'},
              title='Inadimplencia por tipo')
fig21 = px.line(df_contratacao,
              x='Data', 
              y=['credito_contratacao_ltv_pf_comercial_br',
                 'credito_contratacao_ltv_pf_fgts_br',
                 'credito_contratacao_ltv_pf_home_equity_br',
                 'credito_contratacao_ltv_pf_livre_br',
                 'credito_contratacao_ltv_pf_sfh_br'],
              labels={'value':'Valor', 'variable':'Categorias'},
              title='LTV por tipo')
fig22 = px.line(df_contratacao,
              x='Data', 
              y=['credito_contratacao_contratado_mediana_pf_comercial', 
                'credito_contratacao_contratado_mediana_pf_fgts', 
                'credito_contratacao_contratado_mediana_pf_home_equity', 
                'credito_contratacao_contratado_mediana_pf_livre', 
                'credito_contratacao_contratado_mediana_pf_sfh'],
              labels={'value':'Valor', 'variable':'Categorias'},
              title='Mediana dos contratos por tipo')
#fig23 = px.line(df_ifdata, title="Carteira Habitacional por instituição")
#fig23 = px.line(df_percentual_instituicao, title="Carteira Habitacional por instituição")
df_long = df_percentual_instituicao.melt(id_vars=['Data'], var_name='Instituição', value_name='Percentual')
fig23 = px.line(df_long, x='Data', y='Percentual', color='Instituição', title='Carteira Habitacional por Instituição')

fig40 = px.line(df_ifdata, title="Carteira Habitacional por instituição")


fig24 = px.line(df_contratacao,
              x='Data', 
              y=['indices_imobiliario_pib_br'],
              labels={'value':'Percentual', 'variable':'Categorias'},
              title='Financiamento Habitacional (%PIB)')
fig24.update_traces(showlegend=False)
fig25 = px.line(df_por_faixa, x="data_base", y="carteira_ativa", color='faixa', title="Carteira Ativa Por Faixa")
fig26 = px.line(df_por_faixa, x="data_base", y="inadimplencia", color='faixa', title="Inadimplencia por Faixa")
fig27 = px.line(df_sup15_faixa, x="data_base", y="ticket_medio", color='faixa', title="Ticket Medio por Faixa")

df_specific_date = df_por_faixa[df_por_faixa['data_base'] == '2023-12-01']
fig_28 = px.pie(df_specific_date, names='faixa', values='carteira_ativa', title='Carteira Ativa 2023')
fig_29 = px.pie(df_specific_date, names='faixa', values='inadimplencia', title='Inadimplencia 2023')

df_specific_date = df_ocupacao[df_ocupacao['data_base'] == '2023-12-01']
fig_30 = px.pie(df_specific_date, names='ocupacao', values='carteira_ativa', title='Carteira Ativa por Ocupação 2023')
fig_31 = px.pie(df_specific_date, names='ocupacao', values='inadimplencia', title='Inadimplencia por Ocupação 2023')

df_specific_date = df_regiao[df_regiao['data_base'] == '2023-12-01']
fig_32 = px.pie(df_specific_date, names='regiao', values='carteira_ativa', title='Carteira Ativa por Região 2023')
fig_33 = px.pie(df_specific_date, names='regiao', values='inadimplencia', title='Inadimplencia por Região 2023')

df_filtered = df_funding[df_funding['Data'] == '2023-12-31']
df_filtered =df_filtered[['fontes_cri_br', 'fontes_lci_br', 'fontes_lh_br', 'fontes_lig_br', 'fontes_sbpe_saldo_br', 'fgts']]
df_melted = pd.melt(df_filtered, var_name='Fontes', value_name='Valores')
df_melted = df_melted[df_melted['Fontes'] != 'data']
fig34 = px.pie(df_melted, names='Fontes', values='Valores', title='Distribuição de Fontes de Financiamento disponíveis em 20231')

df_filtered = df_contratacao[df_contratacao['Data'] == '2023-12-31']

df_filtered =df_filtered[['credito_estoque_carteira_credito_pf_comercial_br',
                 'credito_estoque_carteira_credito_pf_fgts_br',
                 'credito_estoque_carteira_credito_pf_home_equity_br',
                 'credito_estoque_carteira_credito_pf_livre_br',
                 'credito_estoque_carteira_credito_pf_sfh_br']]
df_melted = pd.melt(df_filtered, var_name='Fontes', value_name='Valores')
df_melted = df_melted[df_melted['Fontes'] != 'data']
fig35 = px.pie(df_melted, names='Fontes', values='Valores', title='Carteira Ativa por tipo em 2023')

df_filtered = df_percentual_instituicao[df_percentual_instituicao['Data'] == 'set/23']
df_melted = pd.melt(df_filtered, var_name='Fontes', value_name='Valores')
df_melted = df_melted[df_melted['Fontes'] != 'data']
fig36 = px.pie(df_melted, names='Fontes', values='Valores', title='Crédito habitacional por instituição set/2023')

#Decomposição
result = seasonal_decompose(df_total['carteira_inadimplida_arrastada'], model='additive', period=12)
trend = result.trend.reset_index()
fig37 = result.plot()
plt.tight_layout()

fig38 = px.line(df_sup15_ocupacao, x="data_base", y="ticket_medio", color='ocupacao', title="Ticket Medio por Ocupação")

fig39 = px.line(df_sup15_regiao, x="data_base", y="ticket_medio", color='regiao', title="Ticket Medio por Região")





# Tabelas
#col = [{"name": i, "id": i} for i in df_percentual_instituicao.columns]
#tab1 = df.to_dict('records')


## Layout
with open("styles.css") as estilo:
   st.markdown(f"<style>{estilo.read()}</style>", unsafe_allow_html=True)
   

st.title('Credito Imobiliario')
st.subheader('Credito Imobiliario por Renda 2023')
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_28, use_container_width=True)
with col2:
    st.plotly_chart(fig_29, use_container_width=True)
    
st.subheader('Credito Imobiliario por Ocupação 2023')
st.plotly_chart(fig_30, use_container_width=True)
st.plotly_chart(fig_31, use_container_width=True)

st.subheader('Credito Imobiliario por Região 2023')
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_32, use_container_width=True)
with col2:
    st.plotly_chart(fig_33, use_container_width=True)

st.subheader('Fontes de Recursos')
st.plotly_chart(fig34, use_container_width=True)

st.subheader('Carteira Ativa por Tipo 2023')
st.plotly_chart(fig35, use_container_width=True)

st.subheader('Crédito Habitacional por Instituição set/2023')
st.plotly_chart(fig36, use_container_width=True)

st.title('Evolução')
st.subheader('Carteira Total')
st.plotly_chart(fig24, use_container_width=True)
st.plotly_chart(fig01, use_container_width=True)  
st.plotly_chart(fig02, use_container_width=True) 
st.pyplot(fig37,use_container_width=True)

 
st.plotly_chart(fig05, use_container_width=True)

st.subheader('Carteira Total Deflacionada')
st.plotly_chart(fig03, use_container_width=True)   
st.subheader('Carteira Por Renda') 
st.plotly_chart(fig06, use_container_width=True) 
st.plotly_chart(fig07, use_container_width=True)    
st.plotly_chart(fig08, use_container_width=True)
st.subheader('Carteira Por Faixa de Renda de acordo com o MCMV') 
st.plotly_chart(fig25, use_container_width=True) 
st.plotly_chart(fig26, use_container_width=True)    
st.plotly_chart(fig27, use_container_width=True)
st.subheader('Carteira Por Ocupação') 
st.plotly_chart(fig09, use_container_width=True)
st.plotly_chart(fig10, use_container_width=True)
st.plotly_chart(fig11, use_container_width=True)
st.plotly_chart(fig38, use_container_width=True)

st.subheader('Carteira Por Região') 
st.plotly_chart(fig12, use_container_width=True)
st.plotly_chart(fig13, use_container_width=True)
st.plotly_chart(fig14, use_container_width=True)
st.plotly_chart(fig39, use_container_width=True)

st.subheader('Contratação') 
st.plotly_chart(fig15, use_container_width=True)
st.plotly_chart(fig16, use_container_width=True) 
st.plotly_chart(fig17, use_container_width=True)
st.plotly_chart(fig18, use_container_width=True)

st.subheader('Carteira (estoque) por Tipo') 
st.plotly_chart(fig19, use_container_width=True)
st.plotly_chart(fig20, use_container_width=True)
st.subheader('LTV') 
st.plotly_chart(fig21, use_container_width=True)   
st.subheader('Mediana') 
st.plotly_chart(fig22, use_container_width=True)
st.subheader('Por Instituição') 
st.plotly_chart(fig23, use_container_width=True)
st.plotly_chart(fig40, use_container_width=True)


 

