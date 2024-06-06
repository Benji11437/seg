import streamlit as st
from PIL import Image
import cv2
import numpy as np

# Fonction pour générer un masque à partir d'une image
def generate_mask(image):
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_image, 125, 255, cv2.THRESH_BINARY)
    return mask

# Titre de l'application
st.title("Affichage de l'image et de son masque")

# Charger l'image via l'interface de téléchargement
uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])  # streamlit run app.py

if uploaded_file is not None:
    # Afficher l'image originale
    image = Image.open(uploaded_file)
    st.image(image, caption='Image originale', use_column_width=True)

    # Générer et afficher le masque
    mask = generate_mask(image)
    st.image(mask, caption='Masque', use_column_width=True)
