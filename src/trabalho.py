import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("1. Saturação")
foto = Image.open("image/foto.jpg")
img = np.array(foto)
fator_s = st.slider("Fator de saturação", 0.0, 2.0, 1.0)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
s = hsv[:, :, 1].astype(float) * fator_s
hsv[:, :, 1] = np.clip(s, 0, 255)
saturada = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
st.image(saturada, caption="saturação alterada")

st.header("2. Brilho")
foto = Image.open("image/foto.jpg")
img = np.array(foto)
soma_v = st.slider("Quanto somar no brilho (V)", -100, 100, 0)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
v = hsv[:, :, 2].astype(int) + soma_v
hsv[:, :, 2] = np.clip(v, 0, 255)
clara = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
st.image(clara, caption="brilho alterado")

st.header("3. Matiz girada")
foto = Image.open("image/foto.jpg")
img = np.array(foto)
giro = st.slider("Giro da matiz (graus)", 0, 360, 0)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hsv[:, :, 0] = (hsv[:, :, 0].astype(int) + giro // 2) % 180
girada = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
st.image(girada, caption="matiz girada")

st.header("8. Negativo")
foto = Image.open("image/foto.jpg")
img = np.array(foto)
negativo = 255 - img
st.image(negativo, caption="negativo")

st.header("9. Recorte")
foto = Image.open("image/foto.jpg")
img = np.array(foto)
a, l = img.shape[0], img.shape[1]
lado = st.slider("Lado do quadrado", 10, min(a, l) // 2, min(a, l) // 4)
linha = st.slider("Linha do canto de cima", 0, a - lado, 0)
coluna = st.slider("Coluna do canto da esquerda", 0, l - lado, 0)
recorte = img[linha:linha + lado, coluna:coluna + lado]
st.image(recorte, caption="recorte")

st.header("11. Espelhamento")
foto = Image.open("image/foto.jpg")
img = np.array(foto)
horizontal = img[:, ::-1]
vertical = img[::-1, :]
st.image(horizontal, caption="espelhada na horizontal")
st.image(vertical, caption="espelhada na vertical")
