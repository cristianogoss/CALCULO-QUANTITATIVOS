import streamlit as st

st.subheader('Quantidade de tijolos')

def calcular_tijolos(altura, largura, qtd_tijolos):
    quantidade = qtd_tijolos * (altura * largura)
    return quantidade

def mostrar_tipos_tijolos(altura, largura):
    st.write("**TIPOS DE TIJOLOS:**")
    tipos_tijolos = {
        "9x14x19 cm (6 furos)": 40,
        "9x19x19 cm (8 furos)": 28,
        "5x9x19 cm (Maciço)": 80
    }
    
    
    for tipo, qtd in tipos_tijolos.items():
        quantidade = calcular_tijolos(altura, largura, qtd)
        st.write(f"{tipo} = {qtd} tijolos por m² -> Total: {quantidade:.0f} tijolos")

altura = st.number_input('Digite a altura da Parede (m)', min_value=0.0, format="%.2f")
largura = st.number_input('Digite a largura da Parede (m)', min_value=0.0, format="%.2f")

if st.button('Calcular'):
    if altura > 0 and largura > 0:
        mostrar_tipos_tijolos(altura, largura)
    else:
        st.error('Por favor, insira valores maiores que zero para altura e largura.')
