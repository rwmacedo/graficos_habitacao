# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import dash_table
from dash_table.Format import Format, Scheme

pd.options.display.float_format = '{:.2f}'.format # show only two digits


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


## Bases de dados
df_total= pd.read_csv('df_total.csv')
df_deflacionada= pd.read_csv('df_deflacionada.csv')
df_por_renda= pd.read_csv('df_por_renda.csv')
df_porte_sup15= pd.read_csv('df_porte_sup15.csv')
df_ocupacao= pd.read_csv('df_ocupacao.csv')
df_tcb= pd.read_csv('df_tcb.csv')
df_sr= pd.read_csv('df_sr.csv')
df_regiao= pd.read_csv('df_regiao.csv')
df_contratacao= pd.read_csv('df_contratacao.csv')
df_ifdata= pd.read_csv('df_ifdata.csv')
df_percentual_instituicao= pd.read_csv('df_percentual_instituicao.csv')




        
##  Graficos
fig01 = px.line(df_total, x="data_base", y= 'carteira_ativa', title="Carteira Ativa")
fig02 = px.line(df_total, x="data_base", y= 'carteira_inadimplida_arrastada', title="Carteira Inadimplida Arrastada")
fig03 = px.line(df_deflacionada, x="data_base", y= 'carteira_ativa_deflacionada', title="Carteira Ativa Deflacionada")
fig04 = px.line(df_deflacionada, x="data_base", y= 'carteira_inadimplida_arrastada_deflacionada', title="Carteira Inadimplida Arrastada Deflacionada")
fig05 = px.line(df_deflacionada, x="data_base", y= 'inadimplencia', title="Inadimplencia Percentual")
fig06 = px.line(df_por_renda, x="data_base", y="carteira_ativa", color='renda', title="Carteira Ativa Por Renda")
fig07 = px.line(df_por_renda, x="data_base", y="carteira_inadimplida_arrastada", color='renda', title="carteira_inadimplida_arrastada por Renda")
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
'''fig16 = px.line(df_contratacao,
                x='Data',
                y='contratacao_pf_total',
                labels={'value':'Valor', 'variable':'Categorias'},
                title='Evolução do Crédito de Contratação')'''
fig17 = px.line(df_contratacao,
                x='Data', 
              y=['credito_contratacao_taxa_pf_comercial_br',
                 'credito_contratacao_taxa_pf_fgts_br',
                 'credito_contratacao_taxa_pf_home_equity_br',
                 'credito_contratacao_taxa_pf_livre_br',
                 'credito_contratacao_taxa_pf_sfh_br'],
              labels={'value':'Valor', 'variable':'Categorias'},
              title='Evolução da taxa de Juros')
fig18 = px.line(df_contratacao,
              x='Data', 
              y=['credito_contratacao_taxa_pf_comercial_br',
                 'credito_contratacao_taxa_pf_fgts_br',
                 'credito_contratacao_taxa_pf_home_equity_br',
                 'credito_contratacao_taxa_pf_livre_br',
                 'credito_contratacao_taxa_pf_sfh_br',
                'indices_selic_br'],
              labels={'value':'Valor', 'variable':'Categorias'},
              title='Evolução da taxa de Juros')
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
              labels={'value':'Valor', 'variable':'Categorias'},
              title='Estoque inadimplencia por tipo')
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
fig23 = px.line(df_ifdata, title="Carteira Habitacional por instituição")
fig24 = px.line(df_contratacao,
              x='Data', 
              y=['indices_imobiliario_pib_br'],
              labels={'value':'Percentual', 'variable':'Categorias'},
              title='Financiamento Habitacional SFH em relação ao PIB')


# Tabelas

#col = [{"name": i, "id": i} for i in df_percentual_instituicao.columns]
#tab1 = df.to_dict('records')


## Layout
app.layout = dbc.Container([
    html.H1('Credito Imobiliario', className='mt-5 mb-4 text-center'),
    
        html.H2('Financiamento Habitacional SFH em relação ao PIB', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Financiamento Habitacional SFH em relação ao PIB', figure=fig24),
            width=12
        )
    ]),    
    html.Hr(),
    
    html.H2('Carteira Ativa', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='carteira_ativa', figure=fig01),
            width=12
        )
    ]),    
    html.Hr(),
     
  html.H2('Carteira Inadimplida Arrastada', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Inadimplida Arrastada', figure=fig02),
            width=12
        )
    ]),    
    html.Hr(),
    
     html.H2('Carteira Ativa Deflacionada', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Ativa Deflacionada', figure=fig03),
            width=12
        )
    ]),    
    html.Hr(),
    
         html.H2('Carteira Inadimplida Arrastada Deflacionada', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Inadimplida Arrastada Deflacionada', figure=fig04),
            width=12
        )
    ]),    
    html.Hr(),
    
 html.H2('Inadimplencia Percentual', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Inadimplencia Percentual', figure=fig05),
            width=12
        )
    ]),    
    html.Hr(),
    
    html.H2('Carteira Ativa Por Renda', className='mb-3 text-center'),
      
    html.Div([          
       html.P("Divisão de classe de renda em:"), 
       html.P("Baixa:: até 3 salário mínimo,"), 
       html.P("média: de 3 até 10 salários mínimos,"),
       html.P("alta: acima de 10 salários mínimos.")    
    ]),
               
 #   html.H2('Carteira Ativa Por Renda', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Ativa Por Renda', figure=fig06),
            width=12
        )
    ]),    
    html.Hr(),
               
    html.H2('Carteira Inadimplida Arrastada por Renda', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Inadimplida Arrastada por Renda', figure=fig07),
            width=12
        )
    ]),    
    html.Hr(), 
   
    
            
    html.H2('Ticket Medio por Renda', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Ticket Medio por Renda', figure=fig08),
            width=12
        )
    ]),    
    html.Hr(), 
    
    html.H2('Carteira Ativa por ocupação', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Ativa por ocupação', figure=fig09),
            width=12
        )
    ]),    
    html.Hr(),
    
     html.H2('Carteira inadimplida por ocupação', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira inadimplida por ocupação', figure=fig10),
            width=12
        )
    ]),    
    html.Hr(),
     
     html.H2('Inadimplencia percentual por ocupação', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Inadimplencia percentual por ocupação', figure=fig11),
            width=12
        )
    ]),    
    html.Hr(), 

    
     html.H2('Carteira Ativa por Região', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Ativa por Região', figure=fig12),
            width=12
        )
    ]),    
    html.Hr(), 

        
     html.H2('Carteira Inadimplida por Região', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Inadimplida por Região', figure=fig13),
            width=12
        )
    ]),    
    html.Hr(), 
        
    html.H2('Inadimplencia por Região', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Inadimplencia por Região', figure=fig14),
            width=12
        )
    ]),    
    html.Hr(), 
    
        
       
            html.H1(children='Base Mercado Imobiliário', style={'text-align': 'center'}),
          
        html.H2('Evolução do Crédito de Contratação por Tipo', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Evolução do Crédito de Contratação por Tipo', figure=fig15),
            width=12
        )
    ]),    
    html.Hr(),       

        
        html.H2('Evolução da taxa de Juros', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Evolução da taxa de Juros', figure=fig17),
            width=12
        )
    ]),    
    html.Hr(),   
    
        html.H2('Estoque Carteira Ativa por tipo', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Estoque Carteira Ativa por tipo', figure=fig19),
            width=12
        )
    ]),    
    html.Hr(),    
    
            html.H2('Estoque inadimplencia por tipo', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Estoque inadimplencia por tipo', figure=fig20),
            width=12
        )
    ]),    
    html.Hr(),   
    
                html.H2('LTV por tipo', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='LTV por tipo', figure=fig21),
            width=12
        )
    ]),    
    html.Hr(),   
    
        html.H2('Mediana dos contratos por tipo', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Mediana dos contratos por tipo', figure=fig22),
            width=12
        )
    ]),    
    html.Hr(),     
    
                html.H1(children='Base IF Data', style={'text-align': 'center'}),      
        
            html.H2('Carteira Habitacional por instituição', className='mb-3 text-center'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Carteira Habitacional por instituição', figure=fig23),
            width=12
        )
    ]),    
    html.Hr(),      
     

  dash_table.DataTable(
    id='table',
    columns=[
        {"name": i, "id": i, "type": "numeric", "format": Format(precision=2, scheme=Scheme.fixed)}
        if df_percentual_instituicao[i].dtype in ['float64', 'float32', 'int64', 'int32'] else {"name": i, "id": i}
        for i in df_percentual_instituicao.columns
    ],
    data=df_percentual_instituicao.to_dict('records'),
    style_table={'overflowX': 'auto'},
)
        
], fluid=True)

with open("index.html", "w") as file:
    file.write(app.index())
     

if __name__ == '__main__':
    app.run_server(debug=True)
