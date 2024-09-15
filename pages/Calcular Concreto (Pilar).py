import streamlit as st

st.subheader("Quantidade de concreto (Pilar) ")

def calcular_concreto(qtd_pilares, altura, maior_dimensao, menor_dimensao):
    medida = qtd_pilares * altura * (maior_dimensao/100) * (menor_dimensao/100)
    return medida

qtd_pilares = st.number_input("Digite a quantidade de pilares", min_value=0.0, format="%.2f")
altura = st.number_input("Digite a altura do pilar (M)", min_value=0.0, format="%.2f")
maior_dimensao = st.number_input("Digite a área 1 (interior do pilar) (Cm)", min_value=0.0, format="%.2f")
menor_dimensao = st.number_input("Digite a área 2 (interior do pilar) (Cm)", min_value=0.0, format="%.2f" )

if st.button("Calcular"):
    if qtd_pilares > 0 and altura > 0 and maior_dimensao > 0 and menor_dimensao > 0:
        resultado = calcular_concreto(qtd_pilares, altura, maior_dimensao, menor_dimensao)
        st.success(f'Você precisará de {resultado: .2f} metros cúbicos de concreto')
    else:
        st.error('Por favor, insira valores maiores que zero.')

