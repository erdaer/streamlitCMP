# Main file for selection of streamlit apps to be run

import streamlit as st

st.set_page_config(page_title="MVV-Vatten Apps")

import importlib

def main():
    st.sidebar.title('MVV-Vatten Apps')
    st.sidebar.write('Data analysis by Daniel Erdal')
    apps = {
        "Choose an app to run!": "app1",
        "Source Tracing App": "SourceTraceApp.analyzePFAS",
        "Wavelet Denoising App": "waveletbasicsApp.waveletBasic",
    }

    app_choice = st.sidebar.selectbox("Choose the app", list(apps.keys()))
    st.sidebar.write('==================')
    app_module = importlib.import_module(apps[app_choice])
    app_module.main()
    
    

        


if __name__ == "__main__":
    main()