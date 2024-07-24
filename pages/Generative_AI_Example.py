import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def process_stream(stream):
  for response in stream:
    content = response["choices"][0]["delta"].get("content")
  if content:
    return content
  else:
    return ""

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

    st.write_stream(process_stream(stream))

if __name__ == "__main__":
  main()