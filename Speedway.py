import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Load assest
lottie_coding = load_lottieurl("https://lottie.host/28de30a2-ab35-442e-a91c-247a277e7d34/zNxEK8FdWD.json")

# Header section
with st.container():
    st.subheader("Speedway Dynamics :wave:")
    st.title("We Analyze data")
    st.write("we zijn gepassioneerd over het vinden van manieren om data te gebruiken om efficiënter en effectiever te zijn in de zakelijke omgeving.")
    st.write("[Zie hier meer >](https://data-semester-2023.github.io/SpeedwayDynamics/)")

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Wat we doen")
        st.write("##")
        st.write("We werken met data" )
        st.write("[Degree>](https://www.hu.nl/deeltijd-opleidingen/hbo-ict-business-it-en-management-deeltijd_bim/de-opleiding)")
        
    with right_column:
        st.lottie(lottie_coding, height=300, key="coding")
