# Libraries
import openai as op
import streamlit as st
import requests as rq
import os
import base64
op.api_key = "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"
# -------------------------------------------------------------------------------------------------------------------
# Streamlit settings
st.set_page_config(page_title='Crea imagen', initial_sidebar_state="collapsed", page_icon='🔴', layout="wide")
# -------------------------------------------------------------------------------------------------------------------
st.title("Creador de imagenes")
st.write("***")
st.subheader("Solicita tú imagen")
solicitud = st.text_input("Describe la imagen que deseas crear: ")
btn = st.button("Enviar solicitud")

if btn:
    respuesta = op.Image.create(
        prompt=solicitud,
        n=1,
        size='512x512',
        response_format="b64_json"
    )
    st.subheader('Imagen creada')
    
    img=respuesta['data'][0]['b64_json']
    img2=base64.b64decode(img)
    st.image(img2)
    
    st.download_button(
        "Descargar imagen",
        data=img2,
        file_name=f"{solicitud}.png",
        mime="image/png"
    )
    
# ----------------------------------------------------------------------------------------------------------------------
st.sidebar.header("Acerca de la App")
st.sidebar.markdown("**15/05/2023**")
