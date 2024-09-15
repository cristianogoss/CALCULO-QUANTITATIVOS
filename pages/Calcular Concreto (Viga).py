import streamlit as st

st.subheader("Quantidade de concreto (Viga)")

def calcular_concreto(perimetro, altura, largura):
    medida = perimetro * (altura/100) * (largura/100)
    return medida

perimetro = st.number_input("Digite o perimetro da viga (M)", min_value=0.0, format= "%.2f")
altura = st.number_input("Digite a altura da viga (Cm)", min_value=0.0, format="%.2f")
largura = st.number_input("Digite a largura da viga (Cm)", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    if perimetro > 0 and altura > 0 and  largura > 0:
        resultado = calcular_concreto(perimetro, altura, largura)
        st.success(f"Você precisará de {resultado: .2f} metros cúbicos de concreto")
    else:
        st.error("Por favor insira valores maiores que zero")