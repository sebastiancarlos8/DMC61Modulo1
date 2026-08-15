import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Sebastian Carlos")

st.image("Python_logo.png, width = 50)

modulos = st.sidebar.selectbox("Seleccione un módulo",["Módulo Listas","Módulo Arreglos","Módulo Funciones"])

if modulos == "Módulo Listas":
  st.write("Bienvenido al módulo de Listas")

  valor_inicial = st.number_input("Ingrese el valor inicial")
  valor_final = st.number_input("Ingrese el valor final")
  
  lista_numeros = list(range(int(valor_inicial),int(valor_final)))
  st.write(lista_numeros)

elif modulos == "Módulo Arreglos":
  st.write("Bienvenido al módulo de Arreglos")
else:
  st.write("Bienvenido al módulo de Funciones")
