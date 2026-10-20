import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira Alamanha")
img2 = np.zeros([6, 9, 3], dtype=np.uint8)
img2[0:2, :] = (0, 0, 0)
img2[2:4, :] = (220, 0, 0)
img2[4:6, :] = (255, 206, 0)
st.image(ampliar(img2), width=450)


