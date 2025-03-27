import streamlit as st

import requests

api_url = "http://api.weatherapi.com/v1/current.json?"
api_key = "0c969b83b3324359b5685710250303"

st.title("Weather App")

city = st.text_input("Enter a city name:")

if city:
    url = api_url + "key=" + api_key + "&q=" + city
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        st.write(f"The current Temperature in {city} is : {data['current']['temp_c']} °C")
        st.write(data['current'])
    else:
        st.write("City not found")

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
