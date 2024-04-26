import streamlit as st
import pandas as pd
import requests

def load_data():
    url = "https://sheetdb.io/api/v1/g9phfrqztsmub"
    response = requests.get(url)
    data = pd.DataFrame(response.json())
    return data

def main():
    st.title('API Data Display')
    st.write('This app displays data from an API in a DataFrame format.')

    data = load_data()
    st.dataframe(data)

if __name__ == "__main__":
    main()
