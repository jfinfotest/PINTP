import streamlit as st 
import pandas as pd  
import firebase_admin  
from firebase_admin import credentials, firestore  

# Verificar si ya existe una instancia de la aplicación
if not firebase_admin._apps:  
    # Cargar las credenciales de Firebase desde los secretos de Streamlit
    firebase_credentials = st.secrets["FIREBASE_CREDENTIALS"]  
    # Convertir las credenciales a un diccionario Python
    secrets_dict = firebase_credentials.to_dict()  
    # Crear un objeto de credenciales usando el diccionario 
    cred = credentials.Certificate(secrets_dict)  
    # Inicializar la aplicación de Firebase con las credenciales
    app = firebase_admin.initialize_app(cred)

# Obtener el cliente de Firestore
db = firestore.client()

# Obtener datos de una colección de Firestore
users = db.collection('users').stream()
# Convertir datos a una lista de diccionarios
users_data = [doc.to_dict() for doc in users]
# Crear DataFrame
df = pd.DataFrame(users_data)

st.write(df)  # Mostrar el DataFrame en la interfaz web de Streamlit