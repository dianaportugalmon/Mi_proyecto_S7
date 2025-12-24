import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header("Análisis exploratorio de datos de vehículos")

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Casillas de verificación
build_histogram = st.checkbox('Mostrar histograma del kilometraje')
build_scatter = st.checkbox('Mostrar gráfico de dispersión (kilometraje vs precio)')

# Histograma
if build_histogram:
    st.write('Histograma del kilometraje de los vehículos')
    
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del kilometraje"
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
if build_scatter:
    st.write('Gráfico de dispersión entre kilometraje y precio')
    
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre kilometraje y precio"
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)