import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def main():
  st.title("Generative AI Example using OpenAI and LangChain")
  
  input = st.text_input("Ask me anything!", key="input")

  if input:
    st.session_state["input"] = ""
    st.write_stream(stream = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are an helpful assistant."},
        {"role": "user", "content": input},
        ],
      stream=True
    ))

if __name__ == "__main__":
  main()