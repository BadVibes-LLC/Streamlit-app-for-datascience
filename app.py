import streamlit as st


html = ""
with open("/pages/test.html","r") as f:
    html = f

def main():
    st.components.v1.html(html)
    st.write("Testing page")

if __name__ == "__main__":
    main()
