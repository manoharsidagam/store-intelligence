import streamlit as st
import requests
import time

st.title("Store Dashboard")

placeholder = st.empty()

while True:
    data = requests.get("http://127.0.0.1:8000/metrics").json()

    with placeholder.container():
        st.metric("Entries", data["entries"])
        st.metric("Exits", data["exits"])
        st.metric("Occupancy", data["occupancy"])

    time.sleep(2)