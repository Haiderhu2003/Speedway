import streamlit as st
import pandas as pd


#Titel van de webpagina
st.title("Het Milieudashboard")

#URL van dashboard op OneDrive 
url = 'https://onedrive.live.com/edit.aspx?resid=26914C219DF840E2!s0828b2b6487e4c1ba3c0270f863fab60&cid=26914c219df840e2&ithint=file%2Cpptx&nav=eyJzSWQiOjI1NiwiY0lkIjozMjExODU5NTQyfQ&redeem=aHR0cHM6Ly8xZHJ2Lm1zL3AvYy8yNjkxNGMyMTlkZjg0MGUyL0ViYXlLQWgtU0J0TW84QW5ENFlfcTJBQmZGcTVDeWVMdGw2aHJaTTBYX2IybFE_ZT0ybTBtbWwmbmF2PWV5SnpTV1FpT2pJMU5pd2lZMGxrSWpvek1qRXhPRFU1TlRReWZR&migratedtospo=true'

#Embed PowerPoint slide in een frame
st.components.v1.iframe(url, width=1000, height=750)