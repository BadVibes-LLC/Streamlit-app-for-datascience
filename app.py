import streamlit as st


html = "pages/test.html"

def main():
    st.html(html)
    st.write("Testing page")

if __name__ == "__main__":
    main()
