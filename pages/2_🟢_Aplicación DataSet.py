import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    tab1, tab2, tab3 = st.tabs(["Análisis 1", "Análisis 2", "Análisis 3"])

    with tab1:
        st.write('Explicación de la función')
        
    with tab2:
        st.write('Explicación de la función')
       
    with tab3:
        st.write('Explicación de la función')
        

    


