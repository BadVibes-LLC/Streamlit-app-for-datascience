import streamlit as st

def main():
    st.components.v1.html('''
    <html>
    <head>
    <meta name="google-adsense-account" content="ca-pub-9369193555413965">
    </head>
    </html>
    ''')
    st.write("Testing page")

if __name__ == "__main__":
    main()
