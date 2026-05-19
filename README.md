# Vehicles US — Dashboard

Dashboard web interativo para exploração do dataset `vehicles_us.csv`, com anúncios de venda de veículos usados nos Estados Unidos. Projeto desenvolvido como parte da Sprint 5 do programa de Ciência de Dados da TripleTen.

## Demo

Acesse o app em produção: [https://vehicles-dashboard.onrender.com](https://vehicles-dashboard.onrender.com)

> O link acima será atualizado após o deploy no Render.

## Tecnologias

- Python 3
- Pandas
- Plotly Express
- Streamlit
- Render (deploy)

## Funcionalidades

- Visualização de histograma da coluna `odometer`.
- Gráfico de dispersão entre `odometer` e `price`.
- Interface simples com checkboxes para alternar os gráficos.

## Como rodar localmente

```bash
# clonar repositorio
git clone https://github.com/Matheus-Dev-01/vehicles-dashboard.git
cd vehicles-dashboard

# criar e ativar ambiente virtual (Windows)
python -m venv venv-vehicles
.\venv-vehicles\Scripts\Activate.ps1

# instalar dependencias
pip install -r requirements.txt

# rodar o app
streamlit run app.py
```

## Estrutura do projeto
