import streamlit as st


st.image("bomba.png",width=250)
st.title("Etanol x Gasolina")


gasolina = st.text_input("Preço Gasolina:")
etanol = st.text_input("Preço Etanol:")

a = gasolina
b = etanol

while a != "" and b != "":
    
    if a > b:
        st.write("Etanol está compensando mais que Gasolina!")
        break
    else:
        st.write("Gasolina está compensando mais que Etanol!")
        break