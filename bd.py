import streamlit as st
import requests

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"

video_url = st.text_input("url")
res = requests.get(video_url, headers={"User-Agent":ua})
st.code(res.text, language="html")