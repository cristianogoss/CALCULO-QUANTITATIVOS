import streamlit as st

st.subheader("Quantidade de concreto (Laje) ")

def calcular_concreto(area_um, area_dois, altura):
    medida = area_um * area_dois * (altura/100)
    return medida

area_um = st.number_input("Digite a área 1 (M)", min_value=0.0, format="%.2f")
area_dois = st.number_input("Digite a área 2 (M)", min_value=0.0, format="%.2f")
altura = st.number_input("Digite a altura (Cm)", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    if area_um > 0 and area_dois > 0 and altura > 0:
        resultado = calcular_concreto(area_um, area_dois, altura)
        st.success (f"Você precisará de {resultado: .2f} metros cúbicos de concreto") 
    else:
        st.error("Por favor insira valores maiores que zero")

