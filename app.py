import pandas as pd
import scipy.stats
import streamlit as st
import time

# Inicialización de las variables de estado
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'heads', 'tails', 'mean'])

st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    outcome_no = 0
    outcome_heads_count = 0
    outcome_tails_count = 0

    # Para almacenar la cantidad de caras obtenidas en cada paso
    heads_counts = []

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_heads_count += 1
        else:
            outcome_tails_count += 1
        
        # Calcular la media de caras hasta el momento
        mean = outcome_heads_count / outcome_no
        heads_counts.append(outcome_heads_count)  # Almacenar el conteo de caras
        chart.add_rows([mean])
        time.sleep(0.05)

    return outcome_heads_count, outcome_tails_count, mean

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    heads, tails, mean = toss_coin(number_of_trials)

    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            heads,
                            tails,
                            mean]],
                     columns=['no', 'iterations', 'heads', 'tails', 'mean'])
        ],
        axis=0)
    st.session_state['df_experiment_results'] = st.session_state['df_experiment_results'].reset_index(drop=True)

    # Mostrar los resultados
    st.write(st.session_state['df_experiment_results'])

    # Visualizar el conteo de caras y sellos
    st.bar_chart([heads, tails], height=300, use_container_width=True)

    # Mostrar la probabilidad de obtener cara
    st.write(f'Probabilidad de obtener cara después de {number_of_trials} lanzamientos: {mean:.2f}')
