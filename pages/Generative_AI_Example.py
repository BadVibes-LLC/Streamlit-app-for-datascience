import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def main():
  st.title("Generative AI Example using OpenAI and LangChain")
  input = st.text_input("Ask me anything!", key="input")

  if input:
    stream = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are an helpful assistant."},
        {"role": "user", "content": input},
        ],
      stream=True
    )

    for response in stream:
      if response.choices[0].delta.content is not None:
        st.write_stream(response.choices[0].delta.content, end="")

if __name__ == "__main__":
  main()