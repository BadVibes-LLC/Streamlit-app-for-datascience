import streamlit as st


html = '''
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9369193555413965"
     crossorigin="anonymous"></script>
'''
def main():
    st.components.v1.html(html)

if __name__ == "__main__":
    main()
