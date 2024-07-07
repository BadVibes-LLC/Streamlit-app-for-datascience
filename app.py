import streamlit as st

def main():
    st.components.v1.iframe("https://web-games.streamlit.app/ads.txt")
    st.write("Testing page")

if __name__ == "__main__":
    main()
