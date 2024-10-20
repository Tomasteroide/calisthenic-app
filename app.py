import streamlit as st
import random

st.header('Lanzar una moneda')

# Función para lanzar la moneda
def lanzar_moneda():
    return random.choice(['Cara', 'Cruz'])

# Botón para lanzar la moneda
if st.button('Lanzar moneda'):
    resultado = lanzar_moneda()
    st.write(f'¡Has obtenido: {resultado}!')