import streamlit as st
import streamlit.components.v1 as components
from constant import *

# page config ----------------------------------------------------------------
st.set_page_config(page_title="Portofolio", page_icon="🎨", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
   menu()

   st.header("🎨 Portfolio",divider='rainbow')

   # page functions ----------------------------------------------------------------
   def Portfolio_component(header, content):
      st.subheader(header, divider='grey')
      st.write(content)

   Portfolio_component(Portfolio[1][0], Portfolio[1][1])
   st.link_button("Go to :green[Website]", "https://seminaraiptit.streamlit.app/")

   Portfolio_component(Portfolio[2][0], Portfolio[2][1])
   st.link_button("Go to :blue[Website]", "https://smart-assistant.streamlit.app/")



