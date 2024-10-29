import streamlit as st
import random

# Título de la aplicación
st.title("Ejercicios de la Segunda Ley de Newton")

# Generar un ejercicio
def generar_ejercicio():
    masa = random.randint(1, 10)  # Masa en kg
    aceleracion = random.randint(1, 10)  # Aceleración en m/s²
    fuerza_correcta = masa * aceleracion  # F = m * a
    return masa, aceleracion, fuerza_correcta

# Crear un nuevo ejercicio
masa, aceleracion, fuerza_correcta = generar_ejercicio()

# Mostrar el ejercicio al usuario
st.write(f"Una masa de **{masa} kg** está siendo acelerada a **{aceleracion} m/s²**.")
st.write("¿Cuál es la fuerza resultante aplicada sobre la masa? (F = m * a)")

# Campo de entrada para la respuesta del usuario
respuesta_usuario = st.number_input("Ingresa tu respuesta (en Newtons)", min_value=0.0)

# Botón para verificar la respuesta
if st.button("Verificar Respuesta"):
    if respuesta_usuario == fuerza_correcta:
        st.success("¡Correcto! La fuerza es de **{:.2f} N**.".format(fuerza_correcta))
    else:
        st.error("Incorrecto. La fuerza correcta es **{:.2f} N**.".format(fuerza_correcta))

# Botón para generar un nuevo ejercicio
if st.button("Generar Nuevo Ejercicio"):
    masa, aceleracion, fuerza_correcta = generar_ejercicio()
    st.experimental_rerun()
