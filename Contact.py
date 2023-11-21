import streamlit as st

# Instellingen voor de paginaconfiguratie
st.set_page_config(page_title="Contact Us", page_icon=":email:", layout="wide")

# Header pagina
st.title("Contact Us")

# Voeg een formulier toe voor contactgegevens
st.write("Vul het onderstaande formulier in om contact met ons op te nemen:")

# Voeg invoervelden toe voor naam, e-mailadres en bericht
naam = st.text_input("Naam")
email = st.text_input("E-mailadres")
bericht = st.text_area("Bericht", height=200)

# Voeg een knop toe om het bericht te verzenden
if st.button("Verzend bericht"):
    if naam and email and bericht:
        # Hier kun je de logica toevoegen om het bericht te verzenden, bijvoorbeeld via e-mail of een database
        st.success("Bedankt voor je bericht! We nemen zo snel mogelijk contact met je op.")
    else:
        st.warning("Vul alle velden in voordat je het bericht verzendt.")

# Voetnoot
st.write("Voor dringende vragen kun je ons ook telefonisch bereiken op [telefoonnummer].")

