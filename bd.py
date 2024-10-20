import streamlit as st
import requests
import re

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"

video_url = st.text_input("url")
res = requests.get(video_url, headers={"User-Agent":ua})
match = re.search(r"video_url: '(.*)'", res.text, re.I|re.M)
st.code(match.group(1), language="html")
res.close()
