import streamlit as st
import requests
import re

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"

video_url = st.text_input("url")
res = requests.get(video_url, headers={"User-Agent":ua})
st.code(res.text)
match = re.search(r"video_url: '(.*?)', ", res.text, re.I|re.M)
vid = match.group(1)
st.code(vid)
res = requests.get(vid, headers={"User-Agent":ua}, allow_redirects=False)
next = res.headers.get('Location')
st.code(next)
res = requests.get(next, headers={"User-Agent":ua}, allow_redirects=False)
st.code(res.headers.get('Location'))

