import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    data = pd.read_csv("sqdata.csv")
    return data


def coordinates():
    data = load_data()
    coords = data[['X', 'Y']]
    coords.columns = ['lon', 'lat']
    return coords

st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

st.dataframe(df, use_container_width=st.session_state.use_container_width)

mapdf = coordinates()

st.map(mapdf, size=6, color='#ff0000')