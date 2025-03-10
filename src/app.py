import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


listings = pd.read_csv('data/raw/listings.csv')

print(listings.isnull().sum())

listings_clean = listings.drop(columns=['coluna1', 'coluna2'])

listings_clean.to_csv('data/processed/listings_clean.csv', index=False)

sns.histplot(listings_clean['price'], bins=50, kde=True)
plt.title('Distribuição de Preços das Listagens')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()


# Título do aplicativo
st.title("Análise do Airbnb em Nova York")

# Carregar dados
listings = pd.read_csv('data/processed/listings_clean.csv')

# Filtro interativo para bairros
neighbourhoods = listings['neighbourhood'].unique()
selected_neighbourhood = st.selectbox("Selecione um bairro", neighbourhoods)

# Filtrar dados
filtered_data = listings[listings['neighbourhood'] == selected_neighbourhood]

# Gráfico interativo
fig = px.scatter(
    filtered_data,
    x='longitude',
    y='latitude',
    color='price',
    size='number_of_reviews',
    hover_name='name',
    title=f'Listagens em {selected_neighbourhood}'
)

# Exibir gráfico
st.plotly_chart(fig)

# Mostrar estatísticas
st.write(f"Preço médio: ${filtered_data['price'].mean():.2f}")
st.write(f"Número de listagens: {len(filtered_data)}")