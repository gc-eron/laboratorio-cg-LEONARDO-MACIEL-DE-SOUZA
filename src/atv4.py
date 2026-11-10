import numpy as np
import streamlit as st
from PIL import Image
import cv2
st.title("Atv 4: RGB")

st.header("1. Leitura da foto")

foto = Image.open("image/foto.jpg")
img = np.array(foto)

st.image(img)
col1, col2 = st.columns(2)
st.text(img.shape)

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)

col1.image(img[:, :, 0], caption="R")

so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
col2.image(so_r, caption="só R")


# 3. Cubo e BGR
# 3. Cubo e BGR
st.header("3. Cubo e BGR")

col1, col2 = st.columns(2)

# Criar um quadrado amarelo
quadrado = np.zeros((100, 100, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 0)

col1.image(quadrado, caption="Amarelo (RGB)")

# Converter RGB para BGR
img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

col2.image(img_bgr, caption="Imagem convertida para BGR")


# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)
r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="média")